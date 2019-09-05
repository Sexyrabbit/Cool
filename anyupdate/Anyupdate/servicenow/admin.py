from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import ConfigItem, Incident, Application


admin.site.register(ConfigItem)
admin.site.register(Incident)
admin.site.register(Application)