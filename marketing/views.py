from django.shortcuts import render, redirect
from .forms import *
from django.http import JsonResponse
from django.contrib.auth import get_user_model
from django.contrib.auth import authenticate, login, logout
from business.models import Business
from marketing.models import GetInTouch
import json
from business.utils import generate_unique_id
from django.views import View
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from users.token import token
from django.conf import settings
from django.utils.encoding import force_bytes, force_text

User = get_user_model()
# Create your views here.


def Home(request):
    return render(request, 'marketing/home.html')


def Services(request):
    return render(request, 'marketing/service.html')


def Pricing(request):
    return render(request, 'marketing/pricing.html')


def Joinus(request):
    return render(request, 'marketing/joinus.html')


def Signup(request):
    if request.method == 'POST':
        data = {}
        Signupform = SignupForm(data=request.POST)
        if Signupform.is_valid():
            user = Signupform.save(commit=False)
            user.set_password(request.POST['password'])
            user.save()
            return JsonResponse({'success': 1, 'msg': 'account has created Succesfully'})
        # we are doing all validation work at frontend like regex and all using javascript
        phone_number = request.POST['phone_number']
        email = request.POST['email']

        is_email_exists = User.objects.filter(email=email).exists()
        is_phone_number_exists = User.objects.filter(
            phone_number=phone_number).exists()

        if is_email_exists:
            data['email_exists'] = 1
        if is_phone_number_exists:
            data['phone_number_exists'] = 1

        return JsonResponse(data)


def Signin(request):
    if request.method == 'POST':
        data = {}
        user = authenticate(
            email=request.POST['email'], password=request.POST['password'])

        if user is not None:
            login(request, user)
            has_business = Business.objects.filter(user=user).exists()
            print(has_business)
            if has_business == False:
                data['is_new_user'] = 1
            data['success'] = 1
            return JsonResponse(data)

        data['user_does_not_exists'] = 1
        return JsonResponse(data)


def SignOut(request):
    logout(request)
    return redirect('joinus')




def getInTouch(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        if data['email'] != '':
            getintouch = GetInTouch(ID=generate_unique_id(GetInTouch),email=data['email'])
            getintouch.save()
            return JsonResponse({'success':1})
    return None


class RequestResetPassword(View):
    def get(self, request):
        return render(request, 'marketing/request_password_reset.html')

    def post(self, request):
        data = request.POST
        if data['email'] != '':
            user = User.objects.filter(email = data['email']).first()
            if user is not None:
                # generate token and uid for activation link
                uid = urlsafe_base64_encode(force_bytes(user.pk))
                reset_token = token.give_token(
                    pk=str(user.pk), email=user.email)

                # send reset activation link through email
                res = user.email_user(email_type='password_reset',dynamic_data={
                    'name':user.first_name,
                    'link':f'{settings.DOMAIN}/reset-password/{uid}/{reset_token}/'
                    })

                if res == 1:
                    return JsonResponse({'success':1})
                return JsonResponse({'failure':1})
        
            return JsonResponse({'no_user_exists':1})


class ResetPassword(View):
    def get(self, request,**kwargs):
        context = {}
        try:
            uid = force_text(urlsafe_base64_decode(kwargs['uidb64']))
            user = User.objects.get(pk=uid)
            if user and token.check_token(user,kwargs['token']):
                context['user_id'] = uid
            else:
                context['invalid_link'] = 1
        except (TypeError, ValueError, OverflowError,):
            context['invalid_link'] = 1

        return render(request, 'marketing/reset_password.html',context=context)

    def post(self, request,**kwargs):
        data = request.POST
        if data['password'] != '':
            try: # it will give error when user does not exists
                uid = force_text(urlsafe_base64_decode(kwargs['uidb64']))
                user = User.objects.get(pk=uid)
                user.set_password(data['password'])
                user.save()
                return JsonResponse({'success':1})   
            except:
                pass
        return JsonResponse({'not_authorize':1})    
        

def test(request):
    return render(request, 'payments/successfull.html')