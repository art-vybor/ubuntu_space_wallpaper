#!/usr/bin/env python3

# http://epic.gsfc.nasa.gov/
# https://gist.github.com/IJMacD/c4cd803ab5b09eaa53dd
# https://github.com/boramalper/himawaripy

from io import BytesIO
from json import loads
from datetime import datetime, timedelta
from time import strptime
from subprocess import call
from os import makedirs
from os.path import expanduser, split
from urllib.request import urlopen
from PIL import Image, ImageDraw, ImageFont
import argparse

# URL with JSON info about images. Expects date=YYYY-MM-DD.
JSON_URL = 'http://epic.gsfc.nasa.gov/api/images.php?date={:04d}-{:02d}-{:02d}'
# URL to download images. Expects an image name parsed out of the JSON.
IMG_URL = 'http://epic.gsfc.nasa.gov/epic-archive/jpg/{}.jpg'
# The format of time strings in the JSON data (for strptime).
TIME_FORMAT = '%Y-%m-%d %H:%M:%S'
# The font to use to write the date.
FONT_FILE = '/usr/share/fonts/truetype/ubuntu-font-family/UbuntuMono-B.ttf'
# The font size to use to write the date.
FONT_SIZE = 30

def main():
    parser = argparse.ArgumentParser(description='Space wallpaper downloader CLI')
    parser.add_argument('-o', metavar='filename', dest='output_file', required=True, help='output file')
    args = parser.parse_args()

    OUTPUT = args.output_file

    # Get the JSON data. Work backward in time if there's nothing yet for today.
    print('Getting JSON data...')
    dt = 0
    json = []
    while len(json) < 1:
        urldate = datetime.now() + timedelta(days = dt)
        with urlopen(JSON_URL.format(urldate.year, urldate.month, urldate.day)) as data:
            json = loads(data.read().decode('utf-8'))
            dt -= 1

    # Pick the most recent image.
    print('Parsing JSON...')
    newest_img = json[0]
    for img in json:
        if strptime(img['date'], TIME_FORMAT) > strptime(newest_img['date'], TIME_FORMAT):
            newest_img = img
    print('Latest image is from {}.'.format(newest_img['date']))

    # Download the image file.
    print('Downloading image...')
    with urlopen(IMG_URL.format(newest_img['image'])) as imagedata:
        bg = Image.open(BytesIO(imagedata.read()))

    # Add text with the current date and save.
    print('Formatting image...')
    w, h = bg.size
    draw = ImageDraw.Draw(bg)
    font = ImageFont.truetype(FONT_FILE, size = FONT_SIZE)
    draw.text((0, h - FONT_SIZE * 2), newest_img['date'], font = font)
    print('Saving image...')
    makedirs(split(OUTPUT)[0], exist_ok=True)
    bg.save(OUTPUT, 'png')

    print("Done!")

if __name__ == "__main__":
  main()