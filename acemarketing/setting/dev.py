from acemarketing.settings import *



SECRET_KEY = os.environ.get('ACENMARK_SECURITY_KEY')

DEBUG = True

ALLOWED_HOSTS = []

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': os.environ.get('DB_NAME'),
        'USER': os.environ.get('DB_USER'),
        'PASSWORD': os.environ.get('DB_PASSWORD'),
        'HOST': os.environ.get('DB_HOST'),
    }
}




STRIPE_PUBLIC_KEY = os.environ.get('STRIPE_PUBLIC_KEY')
STRIPE_KEY_SECRET = os.environ.get('STRIPE_KEY_SECRET')



DOMAIN = 'http://localhost:8000'

SENDGRID_API_KEY = os.environ.get['SENDGRID_API_KEY']
EMAIL_VERIFICATION_TEMPLATE_ID = os.environ.get('EMAIL_VERIFICATION_TEMPLATE_ID')
PASSWORD_RESET_TEMPLATE_ID = os.environ.get('PASSWORD_RESET_TEMPLATE_ID')

ACENMARK_EMAIL = os.environ.get('ACENMARK_EMAIL')