import os
from os.path import join, dirname, realpath
from PIL import Image


def piktures(file, path):
    size = (300, 350)
    #path = join(dirname(realpath(__file__)), 'static', file.filename)
    with Image.open(file) as f:
        f.thumbnail(size)
        f.save(path)
