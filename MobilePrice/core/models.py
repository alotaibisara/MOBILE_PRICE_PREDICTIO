from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User
# Create your models here.
class MobileModel(models.Model):
    battery_power =models.IntegerField(_("battery power"),null=False,blank=False)
    bluetooth = models.BinaryField(_("bluetooth"),null=False,blank=False)
    clock_speed = models.DecimalField(_("clock_speed"),decimal_places=1,max_digits=3)
    dual_sim= models.BinaryField(_("dual_sim"),null=False,blank=False) 
    front_camera=models.IntegerField(_("front_camera"),null=False,blank=False)
    four_g= models.BinaryField(_("4G"),null=False,blank=False) 
    internal_memory=models.IntegerField(_("internal_memory"),null=False,blank=False)
    mobile_depth = models.DecimalField(_("mobile_depth"),decimal_places=1,max_digits=3)
    mobile_weight=models.IntegerField(_("mobile_weight"),null=False,blank=False)
    number_cores=models.IntegerField(_("number_cores"),null=False,blank=False)
    primary_camera=models.IntegerField(_("primary_camera"),null=False,blank=False)
    px_height=models.IntegerField(_("px_height"),null=False,blank=False)
    px_width=models.IntegerField(_("px_width"),null=False,blank=False)
    ram=models.IntegerField(_("RAM"),null=False,blank=False)
    screen_height=models.IntegerField(_("screen_height"),null=False,blank=False)
    screen_width=models.IntegerField(_("screen_width"),null=False,blank=False)
    talk_time=models.IntegerField(_("talk_time"),null=False,blank=False)
    three_g=models.BinaryField(_("3G"),null=False,blank=False)
    touch_screen=models.BinaryField(_("touch screen"),null=False,blank=False)
    wifi=models.BinaryField(_("wifi"),null=False,blank=False)
    class Meta:
        abstract=True

class TrainModel(MobileModel):
    price_range=models.IntegerField(_("price range"),null=False,blank=False)


