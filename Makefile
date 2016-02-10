PREFIX ?= ~/.local/space_wallpaper
PICTURE_NAME = $(PREFIX)/earth-image.png
SET_WALLPAPER = $(PREFIX)/set_wallpaper
GENERATE_WALLPAPER = $(PREFIX)/generate_wallpaper.py


INSTALL_TARGETS = install-dir install-package clean

install: $(INSTALL_TARGETS)

install-dir:
	install -d $(PREFIX)

install-package: 
	install ./set_wallpaper $(SET_WALLPAPER)
	install ./generate_wallpaper.py $(GENERATE_WALLPAPER)
	echo "*/1 * * * * SHELL=/bin/bash/ python3 $(GENERATE_WALLPAPER) -o $(PICTURE_NAME); $(SET_WALLPAPER) $(PICTURE_NAME)" > crontab.tmp
	crontab crontab.tmp
	@echo 'Wallpaper successfully installed'

uninstall:
	-rm $(PICTURE_NAME) $(GENERATE_WALLPAPER) $(SET_WALLPAPER)
	-rm -d $(PREFIX)
	-crontab -r

clean:
	rm crontab.tmp