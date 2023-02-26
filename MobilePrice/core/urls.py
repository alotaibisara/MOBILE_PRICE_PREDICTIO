
from django.urls import path
import core.views as view
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [

        path("login/", view.ViewLogin.as_view(),name='login'),
        path("", view.ViewIndex.as_view(),name='index'),

]
if settings.DEBUG: 
        urlpatterns += static(settings.MEDIA_URL, 
                              document_root=settings.MEDIA_ROOT)