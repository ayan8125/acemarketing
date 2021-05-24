from django.urls import path
from . import views


urlpatterns = [

    path('give_date/', views.give_date, name='give_date'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('campaign-reach/', views.campaign_reach, name='campaign_reach'),
    path('get-social-and-engine-reachs/', views.get_social_and_engine_reachs,
         name='get_social_and_engine_reachs'),
    path('get-social-and-engine-clicks/', views.get_social_and_engine_clicks,
         name='get_social_and_engine_clicks'),
    path('get-campaign-reach-clicks-info/', views.get_campaign_reach_clicks_info,
         name='get_campaign_reach_clicks_info'),

    path('leads/', views.leads, name='leads'),
    path('get-social-and-engine-leads-reach-clicks/', views.get_social_and_engine_leads_reach_clicks,
         name='get_social_and_engine_leads_reach_clicks'),

    path('download/camp_id=<int:campaignid>/',
         views.dowload_Xls, name='dowload_Xls'),


    path('account/', views.Account, name='account'),
    path('edit-user/', views.EditUser, name='edituser'),
    path('edit-user-avatar/', views.EditUserAvatar, name='edituseravatar'),

    path('email-verification/', views.sendVerificationLink, name="email-verification"),
    path('verify-email-verification/<str:uidb64>/<str:token>/',
         views.verifyEmail, name='verify-email'),
]
