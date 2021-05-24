"""acemarketing URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from marketing import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.Home, name="home"),
    path('services/', views.Services, name="services"),
    path('pricing/', views.Pricing, name="pricing"),
    path('payments/', include('payments.urls')),
    path('user/', include('users.urls')),
    path('business/', include('business.urls')),
    path('joinus/', views.Joinus, name="joinus"),
    path('signup/', views.Signup, name="signup"),
    path('signin/', views.Signin, name="signin"),
    path('signout/', views.SignOut, name="signout"),
    path('getIntouch/add/', views.getInTouch, name="getInTouch"),
    path('request-reset-password/', views.RequestResetPassword.as_view(), name="request-reset-password"),
    path('reset-password/<str:uidb64>/<str:token>/',
         views.ResetPassword.as_view(), name='reset-password'),
    path('test/', views.test, name="test"),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
