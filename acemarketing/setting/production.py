"""
    PRODUCTION SETTINGS
    
"""

from acemarketing.settings import *
import json
with open('/etc/config.json') as config_file:
    config = json.load(config_file)

SECRET_KEY = config['SECRET_KEY']


DEBUG = True

ALLOWED_HOSTS = ['35.177.222.122','www.acenmark.co.uk', 'acenmark.co.uk']



DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': config['DB_NAME'],
        'USER': config['DB_USER'],
        'PASSWORD': config['DB_PASSWORD'],
        'HOST': config['DB_HOST'],
    }
}

DOMAIN = 'https://acenmark.co.uk'

STRIPE_PUBLIC_KEY = config['STRIPE_PUBLIC_KEY']
STRIPE_KEY_SECRET = config['STRIPE_KEY_SECRET']

SENDGRID_API_KEY = config['SENDGRID_API_KEY']
EMAIL_VERIFICATION_TEMPLATE_ID = config['EMAIL_VERIFICATION_TEMPLATE_ID']
PASSWORD_RESET_TEMPLATE_ID = config['PASSWORD_RESET_TEMPLATE_ID']

ACENMARK_EMAIL = config['ACENMARK_EMAIL']



AWS_ACCESS_KEY_ID = config['AWS_ACCESS_KEY_ID']
AWS_SECRET_ACCESS_KEY = config['AWS_SECRET_ACCESS_KEY']
AWS_STORAGE_BUCKET_NAME = config['AWS_STORAGE_BUCKET_NAME']
AWS_DEFAULT_ACL = 'public-read'
AWS_S3_CUSTOM_DOMAIN = f'{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com'
AWS_S3_OBJECT_PARAMETERS = {'CacheControl': 'max-age=86400'}
# s3 static settings
STATICFILES_LOCATION   = 'static'
STATIC_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{STATICFILES_LOCATION}/'
STATICFILES_STORAGE = 'acemarketing.custom_storages.StaticStorage'




#s3 media settings
MEDIAFILES_LOCATION = 'media'
MEDIA_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{MEDIAFILES_LOCATION}/'
DEFAULT_FILE_STORAGE = 'acemarketing.custom_storages.MediaStorage'
