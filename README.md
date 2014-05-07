# clementine-info

Python script to extract current track information from Clementine Music Player ( http://www.clementine-player.org/ )

## Features and requirements:

* Using DBUS to query clementine metadata
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
