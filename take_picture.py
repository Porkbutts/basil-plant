import os
import subprocess
from datetime import datetime
from config import load

conf = load()
ROOT_DIR = conf['root_directory']
RESOLUTION = conf.get('resolution', '640x480')
DISPLAY_BANNER = conf.get('display_banner', True)

if __name__ == '__main__':
  now = str(datetime.now().replace(microsecond=0))
  dirname = now.split(' ')[0]
  filename = now.replace(' ', '_').replace(':', '-') + '.jpg'

  abs_dirpath = '{}/{}'.format(ROOT_DIR, dirname)
  abs_filepath = '{}/{}'.format(abs_dirpath, filename)

  if not os.path.isdir(abs_dirpath):
    print 'Creating directory {}'.format(abs_dirpath)
    os.mkdir(abs_dirpath)

  print 'Saving image to {}'.format(abs_filepath)

  args = ['fswebcam', '-r', RESOLUTION]

  if not DISPLAY_BANNER:
    args.append('--no-banner')

  args.append(abs_filepath)
  subprocess.call(args)
  

