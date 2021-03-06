from django.urls import path
from . import views


urlpatterns = [
    path('usp/', views.Usp.as_view(), name='usp'),
    path('usp_list/', views.BusinessUspListView.as_view(), name='usp_list'),
    path('add/', views.BusinessAdd.as_view(), name='add_business'),
    path('goals/', views.Goal.as_view(), name='goals'),
    path('goals-list/', views.GoalsListView.as_view(), name='goals-list'),

    path('sector-list/', views.SectorListView.as_view(), name='sector-list'),
    path('country-list/', views.CountryList, name='country-list'),
]
