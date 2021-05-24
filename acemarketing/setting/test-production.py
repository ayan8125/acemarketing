from acemarketing.settings import *

SECRET_KEY = os.environ.get('ACENMARK_SECURITY_KEY')

DEBUG = True

ALLOWED_HOSTS = []

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': config('DB_NAME'),
        'USER': config('DB_USER'),
        'PASSWORD': config('DB_PASSWORD'),
        'HOST': config('DB_HOST'),
    }
}



STRIPE_PUBLIC_KEY = os.environ.get('STRIPE_PUBLIC_KEY')
STRIPE_KEY_SECRET = os.environ.get('STRIPE_KEY_SECRET')



DOMAIN = 'http://localhost:8000'


EMAIL_VERIFICATION_TEMPLATE_ID = os.environ.get('EMAIL_VERIFICATION_TEMPLATE_ID')
PASSWORD_RESET_TEMPLATE_ID = os.environ.get('PASSWORD_RESET_TEMPLATE_ID')

ACENMARK_EMAIL = os.environ.get('ACENMARK_EMAIL')


AWS_ACCESS_KEY_ID = config('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = config('AWS_SECRET_ACCESS_KEY')
AWS_STORAGE_BUCKET_NAME = config('AWS_STORAGE_BUCKET_NAME')
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