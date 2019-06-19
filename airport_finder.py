import argparse
import json
import math
from functools import lru_cache
from urllib.parse import urlencode
from urllib.request import urlopen


class AirportService:

    def __init__(self, longitude, latitude):
        self.location = MapCoordinate(longitude, latitude)

    def get_nearest_airports_in_radius(self, radius):
        offset_coo1 = self.location.get_offset_coordinate_by_distance(radius)
        offset_coo2 = self.location.get_offset_coordinate_by_distance(-1 * radius)
        airport_data = CloudantService.get_airports_in_coordinate_box(offset_coo2.longitude, offset_coo1.longitude,
                                                                      offset_coo2.latitude, offset_coo1.latitude)
        airports = []
        for airport_dict in airport_data['rows']:
            airports.append(
                Airport(airport_dict['fields']['lon'], airport_dict['fields']['lat'], airport_dict['fields']['name']))
        return sorted(airports, key=lambda airport: self.location.distance_from_coordinate(airport.location))


class Airport:

    def __init__(self, longitude, latitude, name):
        self.location = MapCoordinate(longitude, latitude)
        self.name = name

    def __str__(self):
        return f'{self.name} - {self.location}'


class MapCoordinate:
    EARTH_RADIUS = 6378137
    _RADIAN = 180 / math.pi

    def __init__(self, longitude, latitude):
        self.longitude = longitude
        self.latitude = latitude

    def __str__(self):
        return f'(longitude: {self.longitude}, latitude: {self.latitude})'

    def get_offset_coordinate_by_distance(self, longitudinal_distance, latitudinal_distance=None):
        if latitudinal_distance is None:
            latitudinal_distance = longitudinal_distance

        return MapCoordinate(self._calculate_longitude_offset_by_distance(longitudinal_distance),
                             self._calculate_latitude_offset_by_distance(latitudinal_distance))

    @lru_cache(maxsize=128)
    def distance_from_coordinate(self, other):
        """Haversine formula"""
        longitudinal_distance = math.radians(other.longitude - self.longitude)
        latitudinal_distance = math.radians(other.latitude - self.latitude)

        a = math.sin(latitudinal_distance / 2) ** 2 + math.cos(math.radians(self.latitude)) \
            * math.cos(math.radians(other.latitude)) * math.sin(longitudinal_distance / 2) ** 2
        c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
        return self.EARTH_RADIUS * c

    def _calculate_longitude_offset_by_distance(self, distance):
        return self.longitude + (distance / self.EARTH_RADIUS) * self._RADIAN / math.cos(math.pi * self.latitude / 180)

    def _calculate_latitude_offset_by_distance(self, distance):
        return self.latitude + (distance / self.EARTH_RADIUS) * self._RADIAN


class CloudantService:
    CLOUDANT_REST_API_URL = 'https://mikerhodes.cloudant.com/airportdb/_design/view1/_search/geo'

    @staticmethod
    def get_airports_in_coordinate_box(lon1, lon2, lat1, lat2):
        cloudant_response = urlopen(CloudantService._build_url(lon1, lon2, lat1, lat2))
        data = cloudant_response.read()
        data_encoding = cloudant_response.info().get_content_charset('utf-8')
        return json.loads(data.decode(data_encoding))

    @staticmethod
    def _build_url(lon1, lon2, lat1, lat2):
        if lon1 > lon2:
            lon1, lon2 = lon2, lon1

        if lat1 > lat2:
            lat1, lat2 = lat2, lat1

        values = {'q': f'lon:[{lon1} TO {lon2}] AND lat:[{lat1} TO {lat2}]'}
        data = urlencode(values)
        return f'{CloudantService.CLOUDANT_REST_API_URL}?{data}'


def get_input_from_user(text):
    while True:
        try:
            value = float(input(f'{text}: '))
        except ValueError:
            print(f'{text} must be an float value!')
        else:
            return value


def get_input_data():
    print('Please provide the following information (radius in meters):')
    longitude = get_input_from_user('Longitude')
    latitude = get_input_from_user('Latitude')
    radius = get_input_from_user('Radius')
    return longitude, latitude, radius


def main():
    parser = argparse.ArgumentParser(description='Find the closest airports in a radius of a coordinate.')
    parser.add_argument('--longitude', type=float, help='a float value for the longitudinal part of the coordinate')
    parser.add_argument('--latitude', type=float, help='a float value for the latitudinal part of the coordinate')
    parser.add_argument('--radius', type=float,
                        help='a float value that represents the radius of the search area in meters')
    args = parser.parse_args()

    if args.longitude is None or args.latitude is None or args.radius is None:
        longitude, latitude, radius = get_input_data()
    else:
        longitude, latitude, radius = args.longitude, args.latitude, args.radius
    print(f'Finding airports sorted by distance in a radius of {radius:,.0f} meters from the coordinate '
          f'longitude: {longitude}, latitude: {latitude}')

    airport_service = AirportService(longitude, latitude)
    airports = airport_service.get_nearest_airports_in_radius(radius)
    for airport in airports:
        print(f'{airport}: {airport_service.location.distance_from_coordinate(airport.location):,.0f} meter')


if __name__ == "__main__":
    main()
