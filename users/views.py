from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from business.models import Business, USP
from django.conf import settings
from marketing.models import *
from django.http import JsonResponse, HttpResponse
from django.db.models import Sum
from django.utils.translation import ugettext
from .utils import *

# Create your views here.

User = settings.AUTH_USER_MODEL


def dashboard(request):
    return render(request, 'users/dashboard.html')


def campaign_reach(request):
    data = {'stats': []}
    timePeriods = [timezone.now() - timezone.timedelta(x)
                   for x in range(6, 0, -1)]
    user_business = Business.objects.filter(user=request.user).first()
    if user_business is not None:
        active_campaign_root = CampaignRoot.objects.filter(
            business=user_business, status=1).first()
        if active_campaign_root is not None:
            ads_campaign = Campaign.objects.filter(
                campaign_root=active_campaign_root)

            for timeperiod in timePeriods:

                dataset = {'label': '', 'data': [], 'backgroundColor': [],  # skeleton for dataset
                           'borderColor': [], 'barThickness': 10, 'borderWidth': 1, 'borderRadius': 15}
                colors, reachs = [], []

                for campaign in ads_campaign:
                    reach = Reachs.objects.filter(campaign=campaign, date__day=27,
                                                  date__month=4, date__year=2021).first()
                    reachs.append(reach.no_of_reach)
                    colors.append(campaign.platform.color)

                dataset['data'] = reachs
                dataset['backgroundColor'] = colors
                dataset['borderColor'] = colors
                dataset['label'] = campaign.platform.name
                data['stats'].append(dataset)

    return JsonResponse(data)


def get_social_and_engine_reachs(request):
    data = {}
    user_business = Business.objects.get(user=request.user)
    if user_business is not None:
        active_campaign_root = CampaignRoot.objects.get(
            business=user_business, status=1)
        if active_campaign_root is not None:
            search_engine_platform = MarketingPlatform.objects.filter(
                platform_type=0)
            social_media_platform = MarketingPlatform.objects.filter(
                platform_type=1)

            search_engine_platform_ads_campaign = Campaign.objects.filter(
                campaign_root=active_campaign_root, platform__in=search_engine_platform)
            social_media_platform_ads_campaign = Campaign.objects.filter(
                campaign_root=active_campaign_root, platform__in=social_media_platform)

            serach_engine_reachs = Reachs.objects.filter(
                campaign__in=search_engine_platform_ads_campaign).aggregate(total_reach=Sum('no_of_reach'))
            social_media_reachs = Reachs.objects.filter(
                campaign__in=social_media_platform_ads_campaign).aggregate(total_reach=Sum('no_of_reach'))
            data['serach_engine_reachs'] = serach_engine_reachs
            data['social_media_reachs'] = social_media_reachs
    return JsonResponse(data)


def get_social_and_engine_clicks(request):
    data = {}
    user_business = Business.objects.get(user=request.user)
    if user_business is not None:
        active_campaign_root = CampaignRoot.objects.get(
            business=user_business, status=1)
        if active_campaign_root is not None:
            search_engine_platform = MarketingPlatform.objects.filter(
                platform_type=0)
            social_media_platform = MarketingPlatform.objects.filter(
                platform_type=1)

            search_engine_platform_ads_campaign = Campaign.objects.filter(
                campaign_root=active_campaign_root, platform__in=search_engine_platform)
            social_media_platform_ads_campaign = Campaign.objects.filter(
                campaign_root=active_campaign_root, platform__in=social_media_platform)

            serach_engine_clicks = Clicks.objects.filter(
                campaign__in=search_engine_platform_ads_campaign).aggregate(total_clicks=Sum('no_of_clicks'))
            social_media_clicks = Clicks.objects.filter(
                campaign__in=social_media_platform_ads_campaign).aggregate(total_clicks=Sum('no_of_clicks'))
            data['serach_engine_clicks'] = serach_engine_clicks
            data['social_media_clicks'] = social_media_clicks
    return JsonResponse(data)


def get_campaign_reach_clicks_info(request):
    context = {}
    user_business = Business.objects.get(user=request.user)
    if user_business is not None:
        active_campaign_root = CampaignRoot.objects.get(
            business=user_business, status=1)
        if active_campaign_root is not None:
            ads_campaign = Campaign.objects.filter(
                campaign_root=active_campaign_root)
            campaign_stats = []
            for campaign in ads_campaign:
                camp_Data = {
                    'platform_avatar': campaign.platform.avatar.url,
                    'reach': campaign.reach, 'click': campaign.click
                }
                campaign_stats.append(camp_Data)
            context['campaigns_stats'] = campaign_stats
    return render(request, 'users/campaign_reach_clicks.html', context=context)


def leads(request):
    context = {}
    user_bussines = Business.objects.get(user=request.user)
    campaign_root = CampaignRoot.objects.get(business=user_bussines, status=1)
    camtype = CampaignType.objects.get(pk=2)
    campaign = Campaign.objects.filter(
        campaign_root=campaign_root, ctype=camtype)
    if user_bussines is not None and campaign_root is not None and campaign is not None:
        campaign_leads = Leads.objects.filter(campaign__in=campaign)
        if len(campaign_leads) > 0:
            context['leads'] = campaign_leads
        if len(campaign) > 0:
            context['campaign'] = campaign
        context['camapaign_Id'] = campaign_root._id
    return render(request, 'users/leads.html', context=context)


def get_social_and_engine_leads_reach_clicks(request):
    data = {}
    user_business = Business.objects.get(user=request.user)
    if user_business is not None:
        active_campaign_root = CampaignRoot.objects.get(
            business=user_business, status=1)
        if active_campaign_root is not None:
            search_engine_platform = MarketingPlatform.objects.filter(
                platform_type=0)
            social_media_platform = MarketingPlatform.objects.filter(
                platform_type=1)

            camtype = CampaignType.objects.get(pk=2)

            search_engine_platform_leads_campaign = Campaign.objects.filter(
                campaign_root=active_campaign_root, platform__in=search_engine_platform, ctype=camtype)
            social_media_platform_leads_campaign = Campaign.objects.filter(
                campaign_root=active_campaign_root, platform__in=social_media_platform, ctype=camtype)

            serach_engine_leads_clicks = Leads.objects.filter(
                campaign__in=search_engine_platform_leads_campaign)
            social_media_leads_clicks = Leads.objects.filter(
                campaign__in=social_media_platform_leads_campaign)

            serach_engine_leads_reach = Reachs.objects.filter(
                campaign__in=search_engine_platform_leads_campaign).aggregate(total_reachs=Sum('no_of_reach'))
            social_media_leads_reach = Reachs.objects.filter(
                campaign__in=social_media_platform_leads_campaign).aggregate(total_reachs=Sum('no_of_reach'))

            data['serach_engine_leads_reachs'] = serach_engine_leads_reach['total_reachs']
            data['social_media_leads_reachs'] = social_media_leads_reach['total_reachs']
            data['serach_engine_leads_clicks'] = len(
                serach_engine_leads_clicks)
            data['social_media_leads_clicks'] = len(social_media_leads_clicks)

    return JsonResponse(data)


def dowload_Xls(request, campaignid):
    camp_root = CampaignRoot.objects.get(pk=campaignid)
    if camp_root:
        campaigns = Campaign.objects.filter(campaign_root=camp_root)
        leads = Leads.objects.filter(campaign__in=campaigns)
        filename = f'Leads-{camp_root.business.name}-{camp_root.business.user.first_name}-{camp_root.business.user.last_name}-{camp_root.business.user.id}-{camp_root._id}.xlsx'
        camp_name = f'{camp_root.business.name} Marketing Campaign ID - {camp_root._id}'
        xlsx_data = WriteToExcel(leads, camp_name)
        response = HttpResponse(
            xlsx_data,
            content_type='application/vnd.ms-excel'
        )
        response['Content-Disposition'] = 'attachment; filename=%s' % filename
        return response
    return None


def give_date(request):
    today_date = timezone.now()
    date_string = f'{today_date.strftime("%A")} {today_date.strftime("%d")}, {today_date.strftime("%B")} {today_date.strftime("%Y")}'
    return JsonResponse({'date': date_string})
