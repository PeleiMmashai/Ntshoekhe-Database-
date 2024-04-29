from django.contrib import admin
from django.urls import path, include
from . import views
from django.views.generic import RedirectView

urlpatterns = [
    path('',views.home, name='home'),
    path('admin/', admin.site.urls),
    path('', RedirectView.as_view(url='/node1/'))
    path('node1/', include('node1.urls')),
]

