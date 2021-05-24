from django.db import models
from django.conf import settings
from django.utils import timezone

User = settings.AUTH_USER_MODEL

TRANSACTION_STATUS = ((0, 'Initiaited'), (1, 'Pending'),
                      (2, 'Completed'), (3, 'Failed'))
# Create your models here.


class Wallet(models.Model):
    ID = models.CharField(auto_created=True, primary_key=True, max_length=255)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    currency = models.CharField(max_length=255, default='Pound sterling')
    balanceamt = models.FloatField(default=0.0)
    amt_str = models.CharField(default='0.0k', max_length=255)
    created_at = models.DateTimeField(default=timezone.now)
    update_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'{self.user.first_name}- wallet balance-{self.balanceamt}'


class transaction(models.Model):
    ID = models.CharField(
        auto_created=True, primary_key=True, max_length=255, )
    wallet = models.ForeignKey(Wallet, on_delete=models.CASCADE)
    amount = models.FloatField(default=0.0)
    status = models.IntegerField(default=0, choices=TRANSACTION_STATUS)
    def __str__(self):
        return f'{self.ID} - amount-added = {self.amount}'
