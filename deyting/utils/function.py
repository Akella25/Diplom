import os
from os.path import join, dirname, realpath
from PIL import Image


def piktures(file, path):
    size = (200, 200)
    with Image.open(file) as f:
        f.thumbnail(size)
        f.save(path)
