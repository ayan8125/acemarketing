from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from business.models import Business, USP
from django.conf import settings
from marketing.models import *
from django.http import JsonResponse, HttpResponse
from django.db.models import Sum
from django.utils.translation import ugettext
from .utils import *
from django.db.models import Q
from .forms import *
from django.contrib.auth import get_user_model
from django.views import View
from users.token import token as Token
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode

# Create your views here.
User = get_user_model() 
leads_camp_ID = 2

@login_required
def dashboard(request):
    context = {}
    active_campaign = CampaignRoot.objects.filter(business=request.user.business, status = 1).first()
    if active_campaign:
        ctype = CampaignType.objects.filter(~Q(ID=leads_camp_ID))
        camps = Campaign.objects.filter(ctype__in=ctype,campaign_root=active_campaign)
        has_reach = Reachs.objects.filter(campaign__in=camps, no_of_reach__gte=1).exists()
        has_clicks = Clicks.objects.filter(campaign__in=camps, no_of_clicks__gte=1).exists()
        if len(camps) > 0:
            context['active_camp'] = True 
        if has_reach:
            context['has_reach'] = True
        if has_clicks:
            context['has_clicks'] = True
    context['dashboard'] = True
    return render(request, 'users/dashboard.html', context=context)


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
        active_campaign_root = CampaignRoot.objects.filter(
            business=user_business, status=1).first()
        if active_campaign_root is not None:
            search_engine_platform = MarketingPlatform.objects.filter(
                platform_type=0)
            social_media_platform = MarketingPlatform.objects.filter(
                platform_type=1)

            search_engine_platform_ads_campaign = Campaign.objects.filter(
                 ~Q(ctype=leads_camp_ID), campaign_root=active_campaign_root, platform__in=search_engine_platform)
            social_media_platform_ads_campaign = Campaign.objects.filter(
                 ~Q(ctype=leads_camp_ID), campaign_root=active_campaign_root, platform__in=social_media_platform)

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
        active_campaign_root = CampaignRoot.objects.filter(
            business=user_business, status=1).first()
        if active_campaign_root is not None:
            search_engine_platform = MarketingPlatform.objects.filter(
                platform_type=0)
            social_media_platform = MarketingPlatform.objects.filter(
                platform_type=1)

            search_engine_platform_ads_campaign = Campaign.objects.filter(
                ~Q(ctype=leads_camp_ID), campaign_root=active_campaign_root, platform__in=search_engine_platform)
            social_media_platform_ads_campaign = Campaign.objects.filter(
                ~Q(ctype=leads_camp_ID), campaign_root=active_campaign_root, platform__in=social_media_platform)

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
        active_campaign_root = CampaignRoot.objects.filter(
            business=user_business, status=1).first()
        if active_campaign_root is not None:
            ads_campaign = Campaign.objects.filter(
                ~Q(ctype=leads_camp_ID), campaign_root=active_campaign_root)
            campaign_stats = []
            for campaign in ads_campaign:
                camp_Data = {
                    'platform_avatar': campaign.platform.avatar.url,
                    'reach': campaign.reach, 'click': campaign.click
                }
                campaign_stats.append(camp_Data)
            context['campaigns_stats'] = campaign_stats
    return render(request, 'users/campaign_reach_clicks.html', context=context)

@login_required
def leads(request):
    context = {}
    user_bussines = Business.objects.get(user=request.user)
    campaign_root = CampaignRoot.objects.filter(business=user_bussines, status=1).first()
    camtype = CampaignType.objects.get(pk=leads_camp_ID)
    campaign = Campaign.objects.filter(
        campaign_root=campaign_root, ctype=camtype)
    has_reachs = Reachs.objects.filter(campaign__in=campaign, no_of_reach__gte=1).exists()
    if user_bussines is not None and campaign_root is not None and len(campaign) > 0:
        campaign_leads = Leads.objects.filter(campaign__in=campaign)
        if len(campaign_leads) > 0:
            context['leads'] = campaign_leads
        if has_reachs:
            context['has_reachs'] = True
        context['campaign'] = campaign
        context['camapaign_Id'] = campaign_root.ID

    context['leadstab'] = True
    return render(request, 'users/leads.html', context=context)


def get_social_and_engine_leads_reach_clicks(request):
    data = {}
    user_business = Business.objects.get(user=request.user)
    if user_business is not None:
        active_campaign_root = CampaignRoot.objects.filter(
            business=user_business, status=1).first()
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
        filename = f'Leads-{camp_root.business.name}-{camp_root.business.user.first_name}-{camp_root.business.user.last_name}-{camp_root.business.user.id}-{camp_root.ID}.xlsx'
        camp_name = f'{camp_root.business.name} Marketing Campaign ID - {camp_root.ID}'
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



@login_required
def Account(request):
    return render(request, 'users/account.html')




def EditUser(request):
    if request.method == 'POST':
        prev_email = request.user.email
        prev_number = request.user.phone_number
        data = request.POST
        userform = UserForm(data=data, instance=request.user)
        if userform.is_valid():
            f = userform.save()
            if prev_number != data['phone_number'] and request.user.is_phonenumber_verified == True:
                f.is_phonenumber_verified = False
            if prev_email != data['email'] and request.user.is_email_verified == True:
                f.is_email_verified = False
            f.save()
            return JsonResponse({'success':1})
        resp_data = {}
        if prev_email != data['email']:
            is_email_exists = User.objects.filter(email=data['email']).exists()
            if is_email_exists:
                resp_data['email_exists'] = True
        if prev_number != data['phone_number']:
            is_phone_number_exists = User.objects.filter(phone_number=data['phone_number']).exists()
            if is_phone_number_exists:
                resp_data['phone_number_exists'] = True


        return JsonResponse(resp_data)
    return None




def EditUserAvatar(request):
    if request.method == 'POST':
        user_avatarform = UserAvatarForm(request.POST, request.FILES, instance=request.user)
        if user_avatarform.is_valid():
            user_avatarform.save()
            return JsonResponse({'status': 'Sucess'})

    return JsonResponse({'status': 'Error'})



def sendVerificationLink(request):
    uid = urlsafe_base64_encode(force_bytes(request.user.pk))
    activation_token = Token.give_token(
                pk=str(request.user.pk), email=request.user.email)

    res = request.user.email_user(email_type='email_verification',dynamic_data={
                'name':request.user.first_name,
                'link':f'{settings.DOMAIN}/user/verify-email-verification/{uid}/{activation_token}/'
                })
    if res == 1:
        return JsonResponse({'success':1})
    return JsonResponse({'failure':1})


def verifyEmail(request, uidb64, token):
    context = {}
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
        if user and Token.check_token(user,token):
            user.is_email_verified = True
            user.save()
            context['verified_email'] = 1
        else:
            context['invalid_link'] = 1
    except (TypeError, ValueError, OverflowError,):
        context['invalid_link'] = 1

    return render(request, 'users/verify_email.html', context=context)