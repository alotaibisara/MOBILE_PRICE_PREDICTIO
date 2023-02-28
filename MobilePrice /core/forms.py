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
    (data['avg'], "{0} {1}".format(data['avg'],texting)),
    (data['max'], "{0} {1}".format(data['max'],texting)),
    )

BOLEAN_CHOICES =(
    ('', "  "),
    (1, "Yes"),
    (0, "No"),
 
)

# def get_data(col,texting):
    # TrainModel.objects.all()
    # .aggregate(Avg())

class TrainForm(forms.Form):
    battery_power = forms.IntegerField(label=_('What is your battery capacity'),
                           widget=forms.Select(attrs={'class':'form-control','placeholder':" "},choices=get_data_choices('battery_power','mh')),
                           
                           required=True,
                           localize=True,
                           disabled=False,
                           help_text="")
    bluetooth =forms.BooleanField(label=_('Is there bluetooth in your mobile phone'),
                            widget=forms.Select(attrs={'class':'form-control','placeholder':" "},choices=BOLEAN_CHOICES),
                            required=True,
                           disabled=False,
                           help_text="")
    clock_speed = forms.DecimalField(label=_('What is the frequency of your mobile phone processor'),
                           widget=forms.Select(attrs={'class':'form-control','placeholder':" "},choices=get_data_choices('clock_speed','GHz')),
                           max_digits=3,
                           decimal_places=1,
                           required=True,
                           disabled=False,
                           help_text="")
    dual_sim= forms.BooleanField(label=_('Does your device have a dual_sim feature'),
                            widget=forms.Select(attrs={'class':'form-control','placeholder':" "},choices=BOLEAN_CHOICES),
                           required=True,
                           disabled=False,
                           help_text="") 
    front_camera= forms.IntegerField(label=_('How many megapixels is your front camera'),
                           widget=forms.Select(attrs={'class':'form-control','placeholder':" "},choices=get_data_choices('front_camera','mega pixels')),
                           required=True,
                           localize=True,
                           disabled=False,
                           help_text="")
    four_g= forms.BooleanField(label=_('Does your device support 4G technology?'),
                               widget=forms.Select(attrs={'class':'form-control','placeholder':" "},choices=BOLEAN_CHOICES),
                           required=True,
                           disabled=False,
                           help_text="") 
    internal_memory= forms.IntegerField(label=_('What is the internal memory capacity of your mobile phone'),
                           widget=forms.Select(attrs={'class':'form-control','placeholder':" "},choices=get_data_choices('internal_memory','GB')),
                           
                           required=True,
                           localize=True,
                           disabled=False,
                           help_text="")
    mobile_depth =forms.DecimalField(label=_('Enter the depth of your mobile in cm'),
                           widget=forms.Select(attrs={'class':'form-control','placeholder':" "},choices=get_data_choices('mobile_depth','CM')),
                           max_digits=3,
                           decimal_places=1,
                           required=True,
                           disabled=False,
                           help_text="")
    mobile_weight= forms.IntegerField(label=_('Enter the Weight of your mobile in gram'),
                           widget=forms.Select(attrs={'class':'form-control','placeholder':" "},choices=get_data_choices('mobile_weight','CM')),
                           
                           required=True,
                           localize=True,
                           disabled=False,
                           help_text="")
    number_cores= forms.IntegerField(label=_('Enter the Number of cores of a processor'),
                           widget=forms.Select(attrs={'class':'form-control','placeholder':" "},choices=get_data_choices('number_cores','Core')),
                           required=True,
                           localize=True,
                           disabled=False,
                           help_text="")
    primary_camera= forms.IntegerField(label=_('How many megapixels is your primary camera'),
                           widget=forms.Select(attrs={'class':'form-control','placeholder':" "},choices=get_data_choices('primary_camera','MPls')),
                           required=True,
                           localize=True,
                           disabled=False,
                           help_text="")
    px_height= forms.IntegerField(label=_('Enter Pixel Resolution Height'),
                           widget=forms.Select(attrs={'class':'form-control','placeholder':" "},choices=get_data_choices('px_height','Pixel')),
                           required=True,
                           localize=True,
                           disabled=False,
                           help_text="")
    px_width= forms.IntegerField(label=_('Enter Pixel Resolution Width'),
                           widget=forms.Select(attrs={'class':'form-control','placeholder':" "},choices=get_data_choices('px_width','Pixel')),
                           required=True,
                           localize=True,
                           disabled=False,
                           help_text="")
    ram= forms.IntegerField(label=_('What is the RAM capacity of your mobile phone'),
                           widget=forms.Select(attrs={'class':'form-control','placeholder':" "},choices=get_data_choices('ram','MB')),
                           required=True,
                           localize=True,
                           disabled=False,
                           help_text="")
    screen_height= forms.IntegerField(label=_('15-Enter the Screen Height of mobile in cm'),
                           widget=forms.Select(attrs={'class':'form-control','placeholder':" "},choices=get_data_choices('screen_height','CM')),
                           required=True,
                           localize=True,
                           disabled=False,
                           help_text="")
    screen_width= forms.IntegerField(label=_('Enter the Screen Width of mobile in cm'),
                           widget=forms.Select(attrs={'class':'form-control','placeholder':" "},choices=get_data_choices('screen_width','CM')),
                           required=True,
                           localize=True,
                           disabled=False,
                           help_text="")
    talk_time= forms.IntegerField(label=_('what is the longest time that a single battery charge will last when you are'),
                           widget=forms.Select(attrs={'class':'form-control','placeholder':" "},choices=get_data_choices('talk_time','%')),
                           required=True,
                           localize=True,
                           disabled=False,
                           help_text="")
    three_g=forms.BooleanField(label=_('Does your device support 3G technology'),
                            widget=forms.Select(attrs={'class':'form-control','placeholder':" "},choices=BOLEAN_CHOICES),
                           required=True,
                           disabled=False,
                           help_text="")
    touch_screen=forms.BooleanField(label=_('Does your device support touch screen'),
                            widget=forms.Select(attrs={'class':'form-control','placeholder':" "},choices=BOLEAN_CHOICES),
                           required=True,
                           disabled=False,
                           help_text="")
    wifi=forms.BooleanField(label=_('Wifi'),
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

