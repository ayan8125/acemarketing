from django.shortcuts import render
from business.forms import USPForm, BusinessForm
from django.views import View
from django.views.generic import ListView, CreateView
from business.models import Business, USP, Goals, Sector
from django.http import JsonResponse, HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin
import json
from .utils import generate_unique_id
from .models import UK_COUNTRY_CHOICES

# Create your views here.


class Usp(View):
    def get(self, request):
        uspform = USPForm()
        return render(request, 'business/usp.html', {
            'uspform': uspform
        })

    def post(self, request):
        data = {}
        uspform = USPForm(data=request.POST)
        if uspform.is_valid():
            usp_form = uspform.save(commit=False)
            usp_form.business = request.user.business
            usp_form.ID = generate_unique_id(USP)
            usp_form.save()
            data['usp_added'] = 1
        else:
            data['invalid_usp'] = 1
        return JsonResponse(data)


class BusinessUspListView(ListView):
    model = USP

    def get_context_data(self, **kwargs):
        print(**kwargs)
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['usp_list'] = USP.objects.filter(
            business=self.request.user.business)
        return context


class BusinessAdd(LoginRequiredMixin, View):
    def get(self, request):
        businessform = BusinessForm()
        return render(request, 'business/business_add.html', {
            'BusinessForm': BusinessForm,
        })

    def post(self, request):
        user_business = Business.objects.filter(user=request.user)
        if len(user_business) > 0:
            businessform = BusinessForm(
                data=request.POST, instance=user_business[0])
        else:
            businessform = BusinessForm(data=request.POST)
        print(request.POST)
        if businessform.is_valid():
            business = businessform.save(commit=False)
            business.user = request.user
            business.save()

            return JsonResponse({'business_addedd': 1})
        else:
            return JsonResponse({'some_errors': 1})


class Goal(View):
    def get(self, request):
        return render(request, 'business/goals.html')

    def post(self, request):
        data = json.loads(request.body)
        for goal in data['goals']:
            Goal = Goals(ID=generate_unique_id(Goals), goal=goal,
                         business=request.user.business)
            Goal.save()
        return JsonResponse({'success': 1})






class SectorListView(ListView):

    model = Sector

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['sectors'] = Sector.objects.all()
        return context





def CountryList(request):
    return render(request, 'business/country_list.html', {
        'countries': UK_COUNTRY_CHOICES
        })



class GoalsListView(ListView):

    model = Goals

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['goals'] = Goals.objects.filter(business=self.request.user.business)
        return context
