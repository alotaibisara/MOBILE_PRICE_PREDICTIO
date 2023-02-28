from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.utils.translation import gettext_lazy as _
from core.models import TrainModel
from django.db.models import Avg,Max,Min
def get_data_choices(col,texting):
    train_data=TrainModel.objects.all()
    data= train_data.aggregate(avg=Avg(col),max=Max(col), min=Min(col))
    if type(data['avg']) == type(data['max']):
        data['avg']=round(data['avg'],1)
        data['min']=round(data['min'],1)
        data['max']=round(data['max'],1)
    else:
        data['avg']=int(round(data['avg'],0))

    return (
    ('', "  "),
    (data['min'], "{0} {1}".format(data['min'],texting)),
    # (data['avg'], "{0} {1}".format(data['avg'],texting)),
    (data['max'], "{0} {1}".format(data['max'],texting)),
    )

BOLEAN_CHOICES =(
    ('', "  "),
    (1, "Yes"),
    (0, "No"),)

class TrainForm(forms.Form):
    battery_power = forms.IntegerField(label=_('Choice battery capacity'),
                           widget=forms.Select(attrs={'class':'form-control','placeholder':" "},choices=(('', "  "),(1949, '1949 mh' ),
(803, ' 803  mh' ),
(519, ' 519  mh' ),)),
                           
                           required=True,
                           localize=True,
                           disabled=False,
                           help_text="")
    bluetooth =forms.IntegerField(label=_('have a bluetooth'),
                            widget=forms.Select(attrs={'class':'form-control','placeholder':" "},choices=BOLEAN_CHOICES),
                            required=True,
                           disabled=False,
                           help_text="")
    clock_speed = forms.DecimalField(label=_('Choice Speed processor'),
                                     widget=forms.Select(attrs={'class':'form-control','placeholder':" "},choices=(('', "  "),( 2.6, '2.6 GHz' ),
( 2.1, '2.1 GHz' ),
( 1.6, '1.6 GHz' ),)),

                           max_digits=3,
                           decimal_places=1,
                           required=True,
                           disabled=False,
                           help_text="")
    dual_sim= forms.IntegerField(label=_('Have Dual SIM'),
                            widget=forms.Select(attrs={'class':'form-control','placeholder':" "},choices=BOLEAN_CHOICES),
                           required=True,
                           disabled=False,
                           help_text="") 
    front_camera= forms.IntegerField(label=_('Choice Size front camera'),
                                     widget=forms.Select(attrs={'class':'form-control','placeholder':" "},choices=(('', "  "),(3, "3 mega pixels"),(7, "7 mega pixels"),(4, "4 mega pixels"))),

                           required=True,
                           localize=True,
                           disabled=False,
                           help_text="")
    four_g= forms.IntegerField(label=_('Have 4G technology?'),
                               widget=forms.Select(attrs={'class':'form-control','placeholder':" "},choices=BOLEAN_CHOICES),
                           required=True,
                           disabled=False,
                           help_text="") 
    internal_memory= forms.IntegerField(label=_('choice internal memory capacity'),
                                                                             widget=forms.Select(attrs={'class':'form-control','placeholder':" "},choices=(('', "  "),( 47, '47 GB' ),
( 17, '17 GB' ),
( 51, '51 GB' ),)),

                           
                           required=True,
                           localize=True,
                           disabled=False,
                           help_text="")
    mobile_depth =forms.DecimalField(label=_('choice depth of Mobile'),
                                     widget=forms.Select(attrs={'class':'form-control','placeholder':" "},choices=(('', "  "),( 0.3, '0.3 CM' ),
( 1.0, '1.0 CM' ),
( 0.3, '0.3 CM' ),)),

                           max_digits=3,
                           decimal_places=1,
                           required=True,
                           disabled=False,
                           help_text="")
    mobile_weight= forms.IntegerField(label=_('choice Weight of mobile'),
                           widget=forms.Select(attrs={'class':'form-control','placeholder':" "},choices=(('', "  "),( 199, '199 CM' ),
( 198, '198 CM' ),
( 132, '132 CM' ),)),
                           required=True,
                           localize=True,
                           disabled=False,
                           help_text="")
    number_cores= forms.IntegerField(label=_('choice cores of a processor'),
                                                                                                                  widget=forms.Select(attrs={'class':'form-control','placeholder':" "},choices=(('', "  "),(1, "1 Core"),(3, "3 Core"),(8, "8 Core"))),
                           required=True,
                           localize=True,
                           disabled=False,
                           help_text="")
    primary_camera= forms.IntegerField(label=_('choice primary camera'),
                                     widget=forms.Select(attrs={'class':'form-control','placeholder':" "},choices=(('', "  "),(3, "3 mega pixels"),(17, "17 mega pixels"),(2, "2 mega pixels"))),
                           required=True,
                           localize=True,
                           disabled=False,
                           help_text="")
    
    px_height= forms.IntegerField(label=_('choice Resolution Height'),
                                                                                                                                             
                        widget=forms.Select(attrs={'class':'form-control','placeholder':" "},choices=(('', "  "),(3, "3 Pixels"),(17, "17 pixels"),(2, "2 mega pixels"))),
                           required=True,
                           localize=True,
                           disabled=False,
                           help_text="")
    px_width= forms.IntegerField(label=_('choice Resolution Width'),
                        widget=forms.Select(attrs={'class':'form-control','placeholder':" "},choices=(('', "  "),(3, "3 Pixels"),(17, "17 pixels"),(2, "2 mega pixels"))),
                           required=True,
                           localize=True,
                           disabled=False,
                           help_text="")
    ram= forms.IntegerField(label=_('choice RAM capacity'),
                           widget=forms.Select(attrs={'class':'form-control','placeholder':" "},choices=get_data_choices('ram','MB')),
                           required=True,
                           localize=True,
                           disabled=False,
                           help_text="")
    screen_height= forms.IntegerField(label=_('Choice Height of mobile'),
                           widget=forms.Select(attrs={'class':'form-control','placeholder':" "},choices=get_data_choices('screen_height','CM')),
                           required=True,
                           localize=True,
                           disabled=False,
                           help_text="")
    screen_width= forms.IntegerField(label=_('Choice Width of mobile'),
                           widget=forms.Select(attrs={'class':'form-control','placeholder':" "},choices=get_data_choices('screen_width','CM')),
                           required=True,
                           localize=True,
                           disabled=False,
                           help_text="")
    talk_time= forms.IntegerField(label=_(' Choice longest time that a single battery'),
                           widget=forms.Select(attrs={'class':'form-control','placeholder':" "},choices=get_data_choices('talk_time','%')),
                           required=True,
                           localize=True,
                           disabled=False,
                           help_text="")
    three_g=forms.IntegerField(label=_('Have 3G technology'),
                            widget=forms.Select(attrs={'class':'form-control','placeholder':" "},choices=BOLEAN_CHOICES),
                           required=True,
                           disabled=False,
                           help_text="")
    touch_screen=forms.IntegerField(label=_('Does your device support touch screen'),
                            widget=forms.Select(attrs={'class':'form-control','placeholder':" "},choices=BOLEAN_CHOICES),
                           required=True,
                           disabled=False,
                           help_text="")
    wifi=forms.IntegerField(label=_('Does have Wifi'),
                            widget=forms.Select(attrs={'class':'form-control','placeholder':" "},choices=BOLEAN_CHOICES),
                           required=True,
                           disabled=False,
                           help_text="")

class LoginForm(AuthenticationForm):
    username= forms.CharField(label=False,
                           widget=forms.TextInput(attrs={'class':'form-control rounded-left','placeholder':"Username"}),
                           
                           required=True,
                           localize=True,
                           disabled=False,
                           help_text="")
    password = forms.CharField(label=False,
                           widget=forms.PasswordInput(attrs={'class':'form-control rounded-left','placeholder':"Password"}),
                           max_length=20,
                           required=True,
                           localize=True,
                           disabled=False,
                           help_text="")

