from django.shortcuts import render,redirect
from django.views import View
from django.http import HttpResponse
from django.views.generic import TemplateView,CreateView,FormView
from .forms import VehicleForm
from .models import Vehicle
from django.forms import BaseModelForm
from .forms import RegisterForm,LogForm
from django.urls import reverse_lazy
from django.contrib.auth import authenticate,login
# Create your views here.

class LandingView(TemplateView):
    template_name="index.html"


class RegView(CreateView):
    form_class=RegisterForm
    template_name="reg.html"
    success_url=reverse_lazy("log")
    def form_valid(self, form: BaseModelForm):
        return super().form_valid(form)
    def form_invalid(self, form: BaseModelForm):
        return super().form_invalid(form)
    
class LoginView(FormView):
    template_name="log.html"
    form_class=LogForm
    def post(self,request):
        form_data=LogForm(data=request.POST)
        if form_data.is_valid():
            uname=form_data.cleaned_data.get('username')
            pswd=form_data.cleaned_data.get('password')
            user=authenticate(request,username=uname,password=pswd)
            if user:
                print(user)
                login(request,user)
                return redirect('land')
            else:
                return redirect('log')
        return render(request,"log.html",{"form":form_data})
    
    
class AddVehicleView(View):
    def get(self,request):
        form=VehicleForm()
        return render(request,"addvehicle.html",{"form":form})
    def post(self,request):
        form_data=VehicleForm(data=request.POST)
        if form_data.is_valid():
            title=form_data.cleaned_data.get('title')
            price=form_data.cleaned_data.get('price')
            img=form_data.cleaned_data.get('image')
            cat=form_data.cleaned_data.get('category')
            Vehicle.objects.create(title=title,price=price,image=img,category=cat)
            return redirect('land')
        return render(request,"addvehicle.html",{"form":form_data})

            




