"""Anyupdate URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path, include, re_path
from django.conf.urls import url
from django.views.generic.base import RedirectView
from dashboard.views import *
from django.views.generic import TemplateView

admin.site.site_header = 'WPS Incident Anyupdate'
admin.site.site_title = 'WPS Incident Anyupdate'
#admin.site.site_url = ''
admin.site.index_title = 'WPS Incident Anyupdate'
admin.empty_value_display = '**Empty**'

#from dashing.utils import router
#from dashboard.widgets import NewClientsWidget
#from django.views.generic.base import RedirectView
#from dashboard.views import *

#router.register(NewClientsWidget, 'new_users_widget')

urlpatterns = [
    path('api/', include('dashboard.urls')),
    path('servicenow/', include('servicenow.urls')),
    path('grappelli/', include('grappelli.urls')),
    path('admin/', admin.site.urls),
    #url(r'^dashboard/', include(router.urls), name='dashboard'),
    url(r'^dashboard/', dashboard),
    url(r'^$', RedirectView.as_view(url='dashboard/'), name='index'),
    path(r'api/apps', get_application_list),
    re_path(r'(?P<appname>[a-zA-Z0-9\s]+)/getData$', get_application_details),
    path('flow/', TemplateView.as_view(template_name="flow.html")),
    path('data/', TemplateView.as_view(template_name="data.json")),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    re_path(r'relation/(?P<incidentID>[INC]{3}[0-9]{2})', get_relation),
    re_path(r'fakedata/', get_fake_data),
]
