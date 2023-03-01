from django.views.generic.base import View
from django.shortcuts import render,redirect,HttpResponseRedirect,HttpResponse
from django.contrib.auth import authenticate, login,logout
from django.utils.translation import gettext_lazy as _
from django.contrib import messages
from core.forms import LoginForm,TrainForm
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from core.models import TrainModel # imports the model


from django.urls import reverse
from django.http import JsonResponse
from core.predictor import Predictor
import numpy as np



class ViewLogin(View):
    http_method_names = [
        "get",
        "post",
    ]
    form = LoginForm

    def get(self, request, *args, **kwargs):
        return render(request, 'login.html', {"form":self.form(),})
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

            messages.error(request,self.form.errors)
            return render(request, 'login.html', {"form":self.form})



# @login_required
@login_required

def logout_view(request):
    """
    logout and remove all session data
    """

    logout(request)

    return HttpResponseRedirect(reverse('index')) 



# Build paths inside the project like this: BASE_DIR / 'subdir'.

@method_decorator(login_required, name='dispatch')
class ViewPrediction(View):
    form_class = TrainForm
    def get(self, request, *args, **kwargs):
        return render(request, 'prediction.html', {'prediction':'active','form':self.form_class()})
    def post(self, request, *args, **kwargs):
        self.form_class=self.form_class(data=request.POST)
        if self.form_class.is_valid():
            form_data=self.form_class.cleaned_data
            trian=Predictor()
            per=trian.lreg.predict(trian.s.transform(np.array([form_data[i] for i in form_data]).reshape(1,-1)))
            message=" "
            url = " "
            if per ==0:
                message="Between [700 & 1000] "
                url="https://www.amazon.com/cell-phone-devices/b/ref=dp_bc_aui_C_2?ie=UTF8&node=7072561011"            
            elif per ==1:
                message="Between [1100 & 1300]"
                url="https://www.amazon.com/cell-phone-devices/b/ref=dp_bc_aui_C_2?ie=UTF8&node=7072561011"            

            elif per ==2:
                message="Between [1400 & 1700]"
                url="https://www.amazon.com/cell-phone-devices/b/ref=dp_bc_aui_C_2?ie=UTF8&node=7072561011"            

            else:
                message="Between [1800 & 2000]"
                url="https://www.amazon.com/cell-phone-devices/b/ref=dp_bc_aui_C_2?ie=UTF8&node=7072561011"            


            context={
                'status': "success",
                'message': message,
                'url' :url

            }
        else:
            context={
                'status': "error",
                'errors':self.form_class.errors,
            }
    
        
        return JsonResponse(context,status=200)


class ViewIndex(View):
    form_class = TrainForm
    def get(self, request, *args, **kwargs):
        return render(request, 'index.html', {'home':'active'})

class ViewAboutUs(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'about_us.html', {'about_us':"active"})


class ViewMessage(View):
    http_method_names = [
        "post",
    ]
    def post(self, request, *args, **kwargs):
     
        return HttpResponse('index') 

