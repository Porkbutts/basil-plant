import os, sys
import imageio
from datetime import datetime
from config import load
ROOT_DIR = load()['root_directory']

def files(path):  
  for file in os.listdir(path):
    if os.path.isfile(os.path.join(path, file)):
      yield file

if __name__ == '__main__':
  if len(sys.argv) > 1:
    date = sys.argv[1]
  else:
    date = str(datetime.now()).split(' ')[0]

  abs_path = '{}/{}'.format(ROOT_DIR, date)
  print 'Reading images from folder "{}"'.format(abs_path)

  images = []
  for file in files(abs_path):
    if file.endswith('.jpg'):
      images.append(imageio.imread('{}/{}'.format(abs_path, file)) )

  gif_abs_path = '{}/{}.gif'.format(abs_path, date)
  print 'Saving GIF to "{}"'.format(gif_abs_path)
  imageio.mimsave(gif_abs_path, images, duration=0.1)
  
