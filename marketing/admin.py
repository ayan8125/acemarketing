from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(MarketingPlatform)
admin.site.register(CampaignType)
admin.site.register(Campaign)
admin.site.register(CampaignRoot)
admin.site.register(Reachs)
admin.site.register(Clicks)
admin.site.register(Leads)
admin.site.register(EmailMarketingCampaign)
admin.site.register(Customer)
admin.site.register(UsersforEmailCampaign)

