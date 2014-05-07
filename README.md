# clementine-info

Python script to extract current track information from Clementine Music Player ( http://www.clementine-player.org/ )

## Features and requirements:

* Using DBUS to query clementine metadata (package `python-dbus` is required)
* User can define a custom pattern with tags (see Tags)
* Unicode support

## Usage:

#### Tags:

* %a : artist
* %t : title
* %b : album
* %g : genre
* %p : position
* %P : percent
* %l : time
* %i : arturl
* %f : location

### Run:

    ./clementine-info.py "♪ %t - %a"

## License

GPL v2

## About me

Author: GustavoKatel

* GitHub: [GustavoKatel](http://github.com/GustavoKatel "Github")
* Twitter: [GustavoKatel](http://twitter.com/GustavoKatel "Twitter")
* Email: [gbritosampaio [at] gmail.com](mailto:gbritosampaio@gmail.com "Email")
