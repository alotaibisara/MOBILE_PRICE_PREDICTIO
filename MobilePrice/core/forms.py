from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.utils.translation import gettext_lazy as _

BOLEAN_CHOICES =(
    ('', "------"),
    (1, "Yes"),
    (0, "No"),
    )

battery_power_CHOICES =(
    ('', "------"),
(1954,"1954 mh"),
(1445,"1445 mh"),
(509 ,"509  mh"),
(578 ,"578  mh"),
(1131,"1131 mh"),
(682 ,"682  mh"),
(1949,"1949 mh"),
(503 ,"503  mh"),
(1965,"1965 mh"),
(1784,"1784 mh"),
(1262,"1262 mh"),
(1379,"1379 mh"),
(1829,"1829 mh"),
(1882,"1882 mh"),
(1467,"1467 mh"),
(1911,"1911 mh"),
    )
bluetooth_CHOICES =(

    )
clock_speed_CHOICES =(
    ('', "------"),
(0.5,'0.5 GHz'),
(0.6,'0.6 GHz'),
(1.2,'1.2 GHz'),
(2.6,'2.6 GHz'),
(1.6,'1.6 GHz'),
(1.8,'1.8 GHz'),
(1.1,'1.1 GHz'),
(2.1,'2.1 GHz'),
(2.0,'2.0 GHz'),
(0.9,'0.9 GHz'),
    )

front_camera_CHOICES =(
    ('', "------"),

(0 ,'0  Mega pixels'),
(1 ,'1  Mega pixels'),

(2 ,'2  Mega pixels'),
(4 ,'4  Mega pixels'),
(5 ,'5  Mega pixels'),
(12 ,'12 Mega pixels'),
(8 ,'8  Mega pixels'),
(11 ,'11 Mega pixels'),
    )

internal_memory_CHOICES =(
    ('', "------"),
(24,'24 GB'),
(53,'53 GB'),
(9 ,'9  GB'),
(57,'57 GB'),
(49,'49 GB'),
(19,'19 GB'),
(47,'47 GB'),
(8 ,'8  GB'),
(39,'39 GB'),
(41,'41 GB'),
(34,'34 GB'),
(18,'18 GB'),
(59,'59 GB'),
(44,'44 GB'),
(18,'18 GB'),
(36,'36 GB'),
    )
mobile_depth_CHOICES =(
    ('', "------"),
(0.1,'0.1 CM'),
(0.2,'0.2 CM'),
(0.6,'0.6 CM'),
(1.0,'1.0 CM'),
(0.3,'0.3 CM'),
(0.4,'0.4 CM'),
(0.2,'0.2 CM'),
(0.4,'0.4 CM'),
(0.8,'0.8 CM'),
(0.7,'0.7 CM'),
    )
mobile_weight_CHOICES =(
('', "------"),
(187,'187 CM'),
(174,'174 CM'),
(93 ,'93  CM'),
(162,'162 CM'),
(101,'101 CM'),
(121,'121 CM'),
(199,'199 CM'),
(111,'111 CM'),
(187,'187 CM'),
(164,'164 CM'),
(149,'149 CM'),
(129,'129 CM'),
(91 ,'91  CM'),
(113,'113 CM'),
(122,'122 CM'),
(108,'108 CM'),
)
number_cores_CHOICES =(
    ('', "------"),
(7,'7 cores'),
(5,'5 cores'),
(3,'3 cores'),
(4,'4 cores'),
(6,'6 cores'),
(2,'2 cores'),
(8,'8 cores'),
    )
primary_camera_CHOICES =(
    ('', "------"),
(0 ,"Not have"),
(14,"14 Mega pixels"),
(15,"15 Mega pixels"),
(8 ,"8  Mega pixels"),
(18,"18 Mega pixels"),
(11,"11 Mega pixels"),
(7 ,"7  Mega pixels"),
(13,"13 Mega pixels"),
(3 ,"3  Mega pixels"),
(20,"20 Mega pixels"),
(16,"16 Mega pixels"),
(19,"19 Mega pixels"),
    )
px_height_CHOICES =(
    ('', "------"),
(512 ,'512  Pixels'),
(386 ,'386  Pixels'),
(1137,'1137 Pixels'),
(1025,'1025 Pixels'),
(658 ,'658  Pixels'),
(902 ,'902  Pixels'),
(407 ,'407  Pixels'),
(201 ,'201  Pixels'),
(915 ,'915  Pixels'),
(610 ,'610  Pixels'),
(223 ,'223  Pixels'),
(838 ,'838  Pixels'),
(1457,'1457 Pixels'),
(4   ,'4    Pixels'),
(888 ,'888  Pixels'),
(868 ,'868  Pixels'),
    )
px_width_CHOICES =(
    ('', "------"),
(1149,'1149 Pixels'),
(836 ,'836  Pixels'),
(1224,'1224 Pixels'),
(1433,'1433 Pixels'),
(878 ,'878  Pixels'),
(1064,'1064 Pixels'),
(822 ,'822  Pixels'),
(1245,'1245 Pixels'),
(1965,'1965 Pixels'),
(1437,'1437 Pixels'),
(737 ,'737  Pixels'),
(885 ,'885  Pixels'),
(1919,'1919 Pixels'),
(743 ,'743  Pixels'),
(1099,'1099 Pixels'),
(1632,'1632 Pixels'),
    )
ram_CHOICES =(
    ('', "------"),
(700 ,'700  MB'),
(1099,'1099 MB'),
(513 ,'513  MB'),
(1270,'1270 MB'),
(1835,'1835 MB'),
(2337,'2337 MB'),
(1433,'1433 MB'),
(2583,'2583 MB'),
(2032,'2032 MB'),
(2313,'2313 MB'),
(3248,'3248 MB'),
(2358,'2358 MB'),
(3142,'3142 MB'),
(3579,'3579 MB'),
(3962,'3962 MB'),
(3057,'3057 MB'),
    )
screen_height_CHOICES =(
    ('', "------"),
    (16,'16 CM'),
    (17,'17 CM'),
    (15,'15 CM'),
    (11,'11 CM'),
    (14,'14 CM'),
    (13,'13 CM'),
    (10,'10 CM'),
    (19,'19 CM'),
    (9 ,'9  CM'),
    )
screen_width_CHOICES =(
    ('', "------"),
    (3 ,'3  CM'),
    (1 ,'1  CM'),
    (10,'10 CM'),
    (13,'13 CM'),
    (5 ,'5  CM'),
    (0 ,'0  CM'),
    (10,'10 CM'),
    (6 ,'6  CM'),
    (8 ,'8  CM'),
    (11,'11 CM'),
    )
talk_time_CHOICES =(
    ('', "------"),
    (5 ,'5  %'),
    (20,'20 %'),
    (12,'12 %'),
    (16,'16 %'),
    (18,'18 %'),
    (20,'20 %'),
    (11,'11 %'),
    (4 ,'4  %'),
    (15,'15 %'),
    )

    # price_range

class TrainForm(forms.Form):
    battery_power = forms.IntegerField(label=_('Choice battery capacity'),
                           widget=forms.Select(attrs={'class':'form-control','placeholder':" "},choices=battery_power_CHOICES),
                           
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
                           widget=forms.Select(attrs={'class':'form-control','placeholder':" "},choices=clock_speed_CHOICES),


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
                           widget=forms.Select(attrs={'class':'form-control','placeholder':" "},choices=front_camera_CHOICES),

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
                           widget=forms.Select(attrs={'class':'form-control','placeholder':" "},choices=internal_memory_CHOICES),


                           
                           required=True,
                           localize=True,
                           disabled=False,
                           help_text="")
    mobile_depth =forms.DecimalField(label=_('choice depth of Mobile'),
                           widget=forms.Select(attrs={'class':'form-control','placeholder':" "},choices=mobile_depth_CHOICES),

                           max_digits=3,
                           decimal_places=1,
                           required=True,
                           disabled=False,
                           help_text="")
    mobile_weight= forms.IntegerField(label=_('choice Weight of mobile'),
                           widget=forms.Select(attrs={'class':'form-control','placeholder':" "},choices=mobile_weight_CHOICES),

                           required=True,
                           localize=True,
                           disabled=False,
                           help_text="")
    number_cores= forms.IntegerField(label=_('choice cores of a processor'),
                           widget=forms.Select(attrs={'class':'form-control','placeholder':" "},choices=number_cores_CHOICES),

                           required=True,
                           localize=True,
                           disabled=False,
                           help_text="")
    primary_camera= forms.IntegerField(label=_('choice primary camera'),
                           widget=forms.Select(attrs={'class':'form-control','placeholder':" "},choices=primary_camera_CHOICES),
                           required=True,
                           localize=True,
                           disabled=False,
                           help_text="")
    
    px_height= forms.IntegerField(label=_('choice Resolution Height'),
                                                                                                                                             
                           widget=forms.Select(attrs={'class':'form-control','placeholder':" "},choices=px_height_CHOICES),
                           required=True,
                           localize=True,
                           disabled=False,
                           help_text="")
    px_width= forms.IntegerField(label=_('choice Resolution Width'),
                           widget=forms.Select(attrs={'class':'form-control','placeholder':" "},choices=px_width_CHOICES),
                           required=True,
                           localize=True,
                           disabled=False,
                           help_text="")
    ram= forms.IntegerField(label=_('choice RAM capacity'),
                           widget=forms.Select(attrs={'class':'form-control','placeholder':" "},choices=ram_CHOICES),
                           required=True,
                           localize=True,
                           disabled=False,
                           help_text="")
    screen_height= forms.IntegerField(label=_('Choice Height of mobile'),
                           widget=forms.Select(attrs={'class':'form-control','placeholder':" "},choices=battery_power_CHOICES),
                           required=True,
                           localize=True,
                           disabled=False,
                           help_text="")
    screen_width= forms.IntegerField(label=_('Choice Width of mobile'),
                           widget=forms.Select(attrs={'class':'form-control','placeholder':" "},choices=screen_height_CHOICES),
                           required=True,
                           localize=True,
                           disabled=False,
                           help_text="")
    talk_time= forms.IntegerField(label=_(' Choice longest time that a single battery'),
                           widget=forms.Select(attrs={'class':'form-control','placeholder':" "},choices=talk_time_CHOICES),
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

