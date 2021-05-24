from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth import get_user_model
from .models import Wallet
from business.utils import generate_unique_id

User = get_user_model()

@receiver(post_save, sender=User)
def create_user_wallet(sender, instance, created, **kwargs):
    if created:
        Wallet.objects.create(ID=generate_unique_id(Wallet), user=instance)

@receiver(post_save, sender=User)
def save_user_wallet(sender, instance, **kwargs):
    instance.wallet.save()