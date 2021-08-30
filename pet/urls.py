"""pet URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

#from calc.views import home

from . import index

urlpatterns = [
    path('one/',index.one,name='one'),
    path('two/',index.two,name='two'),

    path('admin/', admin.site.urls),
    #path('sayHello/', home),
    path('',index.mainp,name='mainp'),
    path('stepsToAdopt/',index.steps,name='steps'),
    path('lucy/',index.lucy,name='lucy'),
    path('mia/',index.mia,name='mia'),
    path('lola/',index.lola,name='lola'),
    path('harley/',index.harley,name='harley'),
    path('snow/',index.snow,name='snow'),
    path('newlitter/',index.newlitter,name='newlitter'),
    path('buddy/',index.buddy,name='buddy'),
    path('sunny/',index.sunny,name='sunny'),
    path('bear/',index.bear,name='bear'),
    path('prepare/',index.PYH,name='PYH'),
    path('donate/',index.donate,name='donate'),
    path('newvolunteer/',index.newvolunteer,name='newvolunteer'),
    path('fosterawareness/',index.fosterawareness,name='fosterawareness'),
    path('daycare/',index.daycare,name='daycare'),
    path('release/',index.release,name='release'),
    path('whydogs&life/',index.why,name='why'),
    path('contactus/',index.insertContact,name='contactus'),
    path('adoptform/',index.insertAdopt,name='formA'),
    path('fosterform/',index.insertFoster,name='formF'),
    path('daycareform/',index.insertDaycare,name='formD'),
    path('daycareslot/',index.displayDaycare,name='daycareslot'),
    #path('adminDogs/',index.adminDogs,name='adminDogs'),
]

urlpatterns = urlpatterns + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

