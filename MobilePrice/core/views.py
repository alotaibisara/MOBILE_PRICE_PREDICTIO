from django.views.generic.base import View
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login
from django.utils.translation import gettext_lazy as _
from django.contrib import messages
from core.forms import LoginForm
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
class ViewLogin(View):
    http_method_names = [
        "get",
        "post",
    ]
    form = LoginForm

    def get(self, request, *args, **kwargs):
        return render(request, 'login.html', {"form":self.form()})
    def post(self, request, *args, **kwargs):
 
        self.form = self.form(data=request.POST)
        if self.form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)
                messages.success(request,_('Login is successful'))
                return redirect('index')
            else:
                messages.add_message(request, messages.ERROR,_('You are not eligible to access the system yet, wait for admin’s approval'))

        else:
            print(self.form.errors)

            messages.error(request,self.form.errors)
            return render(request, 'login.html', {"form":self.form})
@method_decorator(login_required, name='dispatch')
class ViewIndex(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'index.html', {})


