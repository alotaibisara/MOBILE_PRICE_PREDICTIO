from django.views.generic.base import View
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login
from django.utils.translation import gettext_lazy as _
from django.contrib import messages
from core.forms import LoginForm,TrainForm
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from core.models import TrainModel # imports the model
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




from django.db.models import Avg,Max,Min
# from pandas
import pandas as pd

def data_farme():
    query_data = TrainModel.objects.all()

    
    df = pd.DataFrame(
  list(query_data.values('battery_power','bluetooth','clock_speed','dual_sim','front_camera','four_g','internal_memory','mobile_depth','mobile_weight','number_cores','primary_camera','px_height','px_width','ram','screen_height','screen_width','talk_time','three_g','touch_screen','wifi'))

)

from django.http import JsonResponse

@method_decorator(login_required, name='dispatch')
class ViewIndex(View):
    form_class = TrainForm
    def get(self, request, *args, **kwargs):
        return render(request, 'index.html', {'form':self.form_class()})
    def post(self, request, *args, **kwargs):
        self.form_class=self.form_class(data=request.POST)
        if self.form_class.is_valid():
            print(request.POST)
            context={
                'status': "success",
                'message':'ddfd'
            }
        else:
            context={
                'status': "error",
                'errors':self.form_class.errors,
            }
    
        
        return JsonResponse(context,status=200)



