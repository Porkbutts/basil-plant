import boto3
from datetime import datetime
from config import load
ROOT_DIR = load()['root_directory']
BUCKET_NAME = 'atengam-rpi3-photos'

s3 = boto3.resource('s3')
bucket = s3.Bucket(BUCKET_NAME)

if __name__ == '__main__':
  date = str(datetime.now()).split(' ')[0]
  abs_filepath = '{0}/{1}/{1}.gif'.format(ROOT_DIR, date)
  print 'Uploading file "{}" to S3 Bucket "{}"'.format(abs_filepath, BUCKET_NAME)
  bucket.upload_file(abs_filepath, '{}.gif'.format(date))

