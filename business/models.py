from django.db import models
from django.conf import settings
from django.utils import timezone

UK_COUNTRY_CHOICES = ((0, 'England'), (1, 'Scotland'),
                      (2, 'Wales'), (4, 'Northern Irealand'))

# Create your models here.


class Sector(models.Model):
    _id = models.IntegerField(primary_key=True, auto_created=True)
    name = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.name}'


class Business(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL,
                                on_delete=models.CASCADE)
    name = models.CharField(default='business', null=True,
                            blank=True, max_length=255)
    runs_online = models.BooleanField(default=False)
    runs_locally = models.BooleanField(default=False)
    sector = models.ForeignKey(Sector, on_delete=models.CASCADE)
    website = models.CharField(null=True, blank=True, max_length=255)
    country = models.IntegerField(
        default=0, choices=UK_COUNTRY_CHOICES, null=True, blank=True)
    address = models.CharField(null=True, blank=True, max_length=255)
    city = models.CharField(null=True, blank=True, max_length=255)
    postcode = models.CharField(null=True, blank=True, max_length=255)

    def __str__(self):
        return f'{self.name} at {self.address}, {self.city} {self.postcode}'

    def give_address(self):
        return f'{self.address}, {self.city} - {self.postcode}'


class USP(models.Model):
    ID = models.CharField(auto_created=True, primary_key=True, max_length=255)
    description = models.TextField(blank=True, null=True)
    business = models.ForeignKey(Business, on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=timezone.now)
    last_updated_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'{self.description}'


class Goals(models.Model):
    ID = models.CharField(auto_created=True, primary_key=True, max_length=255)
    goal = models.TextField(blank=True, null=True)
    business = models.ForeignKey(Business, on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=timezone.now)
    update_at = models.DateTimeField(default=timezone.now)


    def __str__(self):
        return f'{self.goal}'