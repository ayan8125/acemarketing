from __future__ import unicode_literals

from django.db import models
from django.core.mail import send_mail
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import AbstractBaseUser
from django.utils.translation import ugettext_lazy as _
from django.conf import settings
from .managers import UserManager
from phonenumber_field.modelfields import PhoneNumberField
from django.utils import timezone
from marketing.utils import SendDynamic
from django.conf  import settings 


UK_COUNTRY_CHOICES = ((0, 'England'), (1, 'Scotland'),
                      (2, 'Wales'), (4, 'Northern Irealand'))


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(_('email address'), unique=True)
    phone_number = PhoneNumberField(unique=True, default='+44')
    first_name = models.CharField(_('first name'), max_length=30, blank=True)
    last_name = models.CharField(_('last name'), max_length=30, blank=True)
    avatar = models.ImageField(
        upload_to='users/', null=True, blank=True, default='default.png')
    is_email_verified = models.BooleanField(default=False)
    is_phonenumber_verified = models.BooleanField(default=False)
    date_joined = models.DateTimeField(_('date joined'), auto_now_add=True)
    is_active = models.BooleanField(_('active'), default=True)
    is_staff = models.BooleanField(_('staff status'), default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')

    def get_full_name(self):
        '''
        Returns the first_name plus the last_name, with a space in between.
        '''
        full_name = '%s %s' % (self.first_name, self.last_name)
        return full_name.strip()

    def get_short_name(self):
        '''
        Returns the short name for the user.
        '''
        return self.first_name

    def email_user(self, **kwargs):
        if kwargs['email_type'] == 'email_verification':
            TEMPLATE_ID = settings.EMAIL_VERIFICATION_TEMPLATE_ID
        if kwargs['email_type'] == 'password_reset':
            TEMPLATE_ID = settings.PASSWORD_RESET_TEMPLATE_ID
        response_status = SendDynamic(settings.ACENMARK_EMAIL,self.email,TEMPLATE_ID,kwargs['dynamic_data'])
        if response_status == 202:
            return 1
        return 0



