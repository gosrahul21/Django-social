from django.shortcuts import render
from django.views.generic import ListView,DetailView,CreateView,DeleteView,UpdateView
from .forms import UserCreateForm
from django.urls import reverse_lazy
from .models import *
from django.contrib.auth.mixins import LoginRequiredMixin
from braces.views import SelectRelatedMixin
# Create your views here.

class SignUp(CreateView):
    template_name ='account/signup.html'
    form_class = UserCreateForm
    success_url = reverse_lazy('account:about_create')

class  AboutCreate(LoginRequiredMixin,SelectRelatedMixin,CreateView):
    model = About
    fields = ('first_name','middle_name','last_name','profile_pic')
    template_name = 'account/AboutForm.html'
    success_url=reverse_lazy('account:login')


    def form_valid(self, form):
        self.object=form.save(commit=False)


        self.object.user=self.request.user
        self.object.save()
        print('*********************************************')
        print(self.request.user)
        #form.instance.profile_pic=self.request.FILES['profile_pic']
        return super().form_valid(form)





class UserDetail(LoginRequiredMixin,DetailView):
    model=About
    template_name ='account/about_user.html'



class UpdateAccount(LoginRequiredMixin,UpdateView):
    model=About
    template_name='account/AboutForm.html'
    fields = ('first_name','middle_name','last_name','profile_pic')
