"""
URL configuration for disease project.

The `urlpatterns` list routes URLs to view. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function view
    1. Add an import:  from my_app import view
    2. Add a URL to urlpatterns:  path('', view.home, name='home')
Class-based view
    1. Add an import:  from other_app.view import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import view
from django.contrib.staticfiles.storage import staticfiles_storage
from django.views.generic.base import RedirectView



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', view.new, name="home"),
    path('form/', view.form, name="form"),
    path('result/', view.result, name="result"),
    path('bmi/',view.bmi,name='bmi'),
    path('period_cal/',view.period_calculator,name='period_cal'),
    path('calory_cal/',view.cal_calculate,name='cal_calory'),
    path('widal/',view.widal,name='widal'),
    path('sugar/',view.sugar,name='sugar'),
    path('pregnancy_cal/',view.pregnancy_cal,name='pregnancy_cal'),
    path('anxiety/',view.anxiety_screening,name='anxiety'),
    path('medical/',view.medical,name='medical'),
    path('favicon.ico', RedirectView.as_view(url=staticfiles_storage.url('favicon.ico'))),
]
