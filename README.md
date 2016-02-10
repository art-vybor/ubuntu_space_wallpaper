Ubuntu space wallpaper
======================

Dynamic wallpaper for ubuntu which generate fresh picture from earth satelite and update it automatically.

Based on script of @avbop: https://gist.github.com/avbop/58a84da10b7c37f129a2

Some linked sources:
* http://epic.gsfc.nasa.gov/
* https://gist.github.com/IJMacD/c4cd803ab5b09eaa53dd
* https://github.com/boramalper/himawaripy


How to install
--------------

To install just type `make install` in project folder, be carefull, this script replace your crontab file. In one minute you wallpaper will be changed.

To uninstall type `make uninstall` in project folder. This script remove your crontab file and all wallpaper data, but don't reset wallpaper back to system.


Problems in installing
----------------------

If you are using not Ubuntu distribution check variable FONT_FILE in generate_wallpaper.py, font file should be exist.

Also you maybe should to adapt set_wallpaper script (it's works only in gnome)