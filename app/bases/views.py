from django.views import generic
from django.shortcuts import render

from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.


class Home(LoginRequiredMixin, generic.TemplateView):
    template_name = 'bases/home.html'
    login_url='bases:login'



class HomeWithNoPrivileges(LoginRequiredMixin, generic.TemplateView):
    login_url = "bases:login"
    template_name="bases/no_privileges.html"