## World of Aiports
This project is a small Python script which uses a publicly available **Cloudant** database that contain all airports in 
the world. The script will find airports sorted by distance in an user defined radius of a latitudinal-longitudinal 
point.

## Code style
[![PEP8](https://img.shields.io/badge/code%20style-pep8-orange.svg)](https://www.python.org/dev/peps/pep-0008/)
 
 
## Tech/framework used
<b>Built with</b>
- [Python 3.7](https://www.python.org/downloads/release/python-370/)

The script was developed with Python 3.7, but it should work with other Python 3 versions as well.


## Code Example
Show what the library does as concisely as possible, developers should be able to figure out **how** your project solves their problem by looking at the code example. Make sure the API you are showing off is obvious, and that your code is short and concise.


## Installation
Provide step by step series of examples and explanations about how to get a development env running.


## API Reference
Depending on the size of the project, if it is small and simple enough the reference docs can be added to the README. For medium size to larger projects it is important to at least provide a link to where the API reference docs live.


## Tests
No tests are available yet.


## How to use?
There is two ways to use the script:
1. By running the script with 3 optional arguments:
```
python airport_finder.py --longitude 21.9189 --latitude 47.0465 --radius 100000
```
- **longitude**: must be a float value, which is longitudinal part of the center coordinate of the area
- **latitude**: must be a float value, which is latitudinal part of the center coordinate of the area
- **radius**: must be a float value, is the radius which defines the area of the search area with center defined by the 
longitude-latitude coordinate

If the arguments are float values than the script will fail to start and a help message will be printed.
To print manual of the CLI, use the following command:
```
python airport_finder.py -h
```
If one of the arguments is not provided than the script will wait for input from the user. (case nr 2.)

2. By running the script without arguments:
```
python airport_finder.py
```
In this case the script will wait for longitude, latitude and radius inputs from the user.
For example:
```
Please provide the following information (radius in meters):
Longitude: 21.9189
Latitude: 47.0465
Radius: 100000
```
If the input values are not float values than the scrip will ask for input again until the values are not valid.
To stop the script press: `CTRL + C`.

#### Example input
- longitude: 21.9189, latitude: 47.0465, radius: any arbitrary number (in meters) - **Nagyvárad** (Oradea), Romania (my home town :) )
- longitude: 19.0402, latitude: 47.4979, radius: any arbitrary number (in meters) - **Budapest**, Hungary (where I live :) )


## Contribute
Please feel free to fork the project.


## License
Copyright 2019 Zsolt Bokor

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.


MIT © [Zsolt Bokor](https://github.com/zsoman)
