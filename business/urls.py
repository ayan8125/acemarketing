from django.urls import path
from . import views


urlpatterns = [
    path('usp/', views.Usp.as_view(), name='usp'),
    path('usp_list/', views.BusinessUspListView.as_view(), name='usp_list'),
    path('add/', views.BusinessAdd.as_view(), name='add_business'),
    path('goals/', views.Goal.as_view(), name='goals'),
]
