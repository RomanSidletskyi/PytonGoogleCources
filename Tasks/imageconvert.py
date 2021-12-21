#!/usr/bin/env python3

import os,sys

from PIL import Image
from glob import glob

for file in glob('images/ic_*'):
  try:
    image = Image.open(file).convert('RGB')
    ##  print(image.format,image.size,image.mode)

    path,filename = os.path.split(file)
    filename = os.path.splitext(filename)[0]
    ##print(path,filename,file)

    image.rotate(90).resize((128,128)).save('/opt/icons/{}.jpeg'.format(filename))

  except OSError:
    print("cannot convert", file)
