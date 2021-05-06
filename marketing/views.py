from django.shortcuts import render
from .forms import *
from django.http import JsonResponse
from django.contrib.auth import get_user_model
from django.contrib.auth import authenticate, login


User = get_user_model()
# Create your views here.


def Joinus(request):
    return render(request, 'marketing/joinus.html')


def Signup(request):
    if request.method == 'POST':
        data = {}
        Signupform = SignupForm(data=request.POST)
        if Signupform.is_valid():
            Signupform.save()
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
            return JsonResponse({'success': 1})

        data['user_does_not_exists'] = 1
        return JsonResponse(data)
