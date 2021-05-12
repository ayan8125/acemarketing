from django.db import models
from business.models import Business
from phonenumber_field.modelfields import PhoneNumberField
from django.utils.translation import ugettext_lazy as _
from django.utils import timezone
# Create your models here.

CAMPAIGN_TYPE = (
                (0, 'Sales'), (1, 'Leads'),
                (2, 'Web Traffic'), (3, 'Product and Brand consederation'),
                (4, 'Reach and Brand Awarness'), (5, 'App Promotion'),
                (6, 'Local Store Visits and Promotions')
)

EMAIL_STATUS_CHOICE = ((0, 'Not Sended'), (1, 'Sended'))

CAMPAIGN_STATUS_CHOICES = ((1, 'Running'), (2, 'Stoped'), (3, 'Terminated'))

PLAT_FORM_TYPE = ((0, 'Serch Engine'), (1, 'SocialMedia'))

class MarketingPlatform(models.Model):
    ID = models.IntegerField(primary_key=True, auto_created=True)
    platform_type = models.IntegerField(default=1, choices=PLAT_FORM_TYPE)
    name = models.CharField(null=True, blank=True, max_length=255)
    color = models.CharField(max_length=255, default='rgba(0,0,0,1)')
    avatar = models.ImageField(
        upload_to='marketingplatform', null=True, blank=True)

    def __str__(self):
        return f'{self.name}'


class CampaignType(models.Model):
    ID = models.IntegerField(primary_key=True, auto_created=True)
    name = models.CharField(null=True, blank=True, max_length=255)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return f'{self.name}'

# this model will act as root campaign for every campaign from diffrent platforms ex - googgle, facebook ,etc
class CampaignRoot(models.Model):
    ID = models.IntegerField(primary_key=True, auto_created=True)
    business = models.ForeignKey(Business, on_delete=models.CASCADE)
    status = models.IntegerField(default=1, choices=CAMPAIGN_STATUS_CHOICES)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'{self.business} campaign'

class Campaign(models.Model):
    ID = models.IntegerField(primary_key=True, auto_created=True)
    name = models.CharField(null=True, blank=True, max_length=255)
    platform = models.ForeignKey(MarketingPlatform, on_delete=models.CASCADE)
    ctype = models.ForeignKey(CampaignType, on_delete=models.CASCADE)
    reach = models.CharField(null=True, blank=True,
                             default='0.0k', max_length=255)
    click = models.CharField(null=True, blank=True,
                             default='0.0k', max_length=255)
    cost = models.FloatField(default=0.0)
    budget = models.FloatField(default=0.0)
    status = models.IntegerField(default=1, choices=CAMPAIGN_STATUS_CHOICES)
    campaign_root = models.ForeignKey(
        CampaignRoot, on_delete=models.CASCADE, default=1)

    def __str__(self):
        return f'{self.name} at {self.platform}  got {self.click} clicks and {self.reach} '



class Leads(models.Model):
    campaign = models.ForeignKey(Campaign, on_delete=models.CASCADE)
    first_name = models.CharField(null=True, blank=True, max_length=255)
    last_name = models.CharField(null=True, blank=True, max_length=255)
    email = models.EmailField(_('email address'))
    phone_number = PhoneNumberField(unique=True, default='+44')

    def __str__(self):
        return f'{self.first_name} {self.last_name} of Campaign {self.campaign}'


class Reachs(models.Model):
    no_of_reach = models.IntegerField(default=0)
    date = models.DateTimeField(default=timezone.now)
    campaign = models.ForeignKey(Campaign, on_delete=models.CASCADE)


class Clicks(models.Model):
    no_of_clicks = models.IntegerField(default=0)
    date = models.DateTimeField(default=timezone.now)
    campaign = models.ForeignKey(Campaign, on_delete=models.CASCADE)


class EmailMarketingCampaign(models.Model):
    _id = models.IntegerField(primary_key=True, auto_created=True)
    name = models.CharField(null=True, blank=True, max_length=255)
    business = models.ForeignKey(Business, on_delete=models.CASCADE)
    no_of_mail_send = models.IntegerField(default=0)
    reach = models.CharField(null=True, blank=True,
                             default='0.0k', max_length=255)
    click = models.CharField(null=True, blank=True,
                             default='0.0k', max_length=255)
    cost = models.FloatField(default=0.0)
    budget = models.FloatField(default=0.0)

    def __str__(self):
        return f'{self.name} , noofmail_sended = {self.no_of_mail_send} , reach = {self.reach}, engageduser={self.click}'

# bssiness owners customer
class Customer(models.Model):
    first_name = models.CharField(null=True, blank=True, max_length=255)
    last_name = models.CharField(null=True, blank=True, max_length=255)
    email = models.EmailField(_('email address'))
    business = models.ForeignKey(Business, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.first_name} {self.last_name} - {self.business}'


class UsersforEmailCampaign(models.Model):
    email_campaign = models.ForeignKey(
        EmailMarketingCampaign, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    mail_status = models.IntegerField(default=0, choices=EMAIL_STATUS_CHOICE)

    def __str__(self):
        return f'{self.email_campaign} {self.customer} mail_status = {self.mail_status}'
