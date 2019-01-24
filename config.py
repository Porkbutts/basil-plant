import sys, os
import yaml

def load(file='config.yaml'):
  abs_path = os.path.dirname(os.path.abspath(__file__))
  with open('{}/{}'.format(abs_path, file), 'r') as stream:
    config = yaml.safe_load(stream)
  return config

if __name__ == '__main__':
  if len(sys.argv) > 1:
    print load(sys.argv[1])
  else:
    print load()
