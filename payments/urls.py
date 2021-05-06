from django.urls import path
from . import views


urlpatterns = [
    path('paymentsuccessfull/<str:transactionId>/',
         views.paymentSuccessful, name='paymentsuccessfull'),
    path('paymentcancel/<str:transactionId>/',
         views.paymentCancel, name='paymentcancel'),
    path('addmoney/', views.AddMoney, name='addmoney'),
    path('transaction/',
         views.Transaction.as_view(), name='transaction'),
]
