import configparser

config = configparser.ConfigParser()
config.read('config.ini')

DATABASE_URI = config.get('postgresql', 'database_uri')
AWS_REGION = config.get('aws', 'aws_region')
S3_BUCKET_NAME = config.get('aws', 's3_bucket_name')
S3_OUTPUT_FILE = 'output/joined_data.csv'
