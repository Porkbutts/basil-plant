import os
import shutil
from config import load
ROOT_DIR = load()['root_directory']

if __name__ == '__main__':
  archive_dirpath = '{}/{}'.format(ROOT_DIR, 'Archive')
  if not os.path.isdir(archive_dirpath):
    print 'Creating directory {}'.format(archive_dirpath)
    os.mkdir(archive_dirpath)

  subdirs = [name for name in os.listdir(ROOT_DIR) 
             if os.path.isdir(os.path.join(ROOT_DIR, name))
             and name != 'Archive']
  
  print 'Directories found: {}'.format(subdirs)
  for subdir in subdirs:
    gif_filename = '{}.gif'.format(subdir)
    gif_subdir = '{}/{}'.format(ROOT_DIR, subdir)
    gif_abspath = '{}/{}'.format(gif_subdir, gif_filename)

    print 'Archiving {}'.format(gif_abspath)
    shutil.copyfile(gif_abspath, '{}/Archive/{}'.format(ROOT_DIR, gif_filename))

    print 'Deleting folder {}'.format(gif_subdir)
    shutil.rmtree(gif_subdir)
