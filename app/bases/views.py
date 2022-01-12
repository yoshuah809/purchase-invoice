from django.contrib.auth import REDIRECT_FIELD_NAME
from django.http.response import HttpResponseRedirect
from django.urls.base import reverse_lazy
from django.views import generic
from django.shortcuts import render

from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
# Create your views here.


class Home(LoginRequiredMixin, generic.TemplateView):
    template_name = 'bases/home.html'
    login_url='bases:login'



class HomeWithNoPrivileges(LoginRequiredMixin, generic.TemplateView):
    login_url = "bases:login"
    template_name="bases/no_privileges.html"


class NoProvileges(PermissionRequiredMixin, LoginRequiredMixin):
    login_url = "bases:login"
    raise_exception=False
    REDIRECT_FIELD_NAME='redirect_to'

    def handle_no_permission(self):
        self.login_url ='bases:no_privileges'
        return HttpResponseRedirect(reverse_lazy(self.login_url))
        
        