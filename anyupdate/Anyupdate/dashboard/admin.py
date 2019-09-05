# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from dashboard.models import *

from import_export import resources
from import_export.admin import ImportExportModelAdmin

class SupportTeamResource(resources.ModelResource):
    class Meta:
        model = support_team
        skip_unchanged = True
        fields = ("id","name","region",)
        exclude = ("create_at", "update_at", "status",)

class ConfigureItemResource(resources.ModelResource):
    class Meta:
        model = configure_item
        skip_unchanged = True
        fields = ("id","name",)
        exclude = ( "support_team", "create_at", "update_at", "status")

class ApplicationResource(resources.ModelResource):
    class Meta:
        model = application
        skip_unchanged = True
        fields = ("id","name",)
        exclude = ("create_at", "update_at", "status",)

@admin.register(support_team)
#class SupportTeamAdmin(admin.ModelAdmin):
class SupportTeamAdmin(ImportExportModelAdmin):
    list_display = ["name","region","email","create_at","update_at"]
    search_fields = ['name',"region","email"]
    readonly_fields = ["status"]
    resource_class = SupportTeamResource

@admin.register(configure_item)
#class ConfigureItemAdmin(admin.ModelAdmin):
class ConfigureItemAdmin(ImportExportModelAdmin):
    list_display = ["name","create_at","update_at"]
    filter_horizontal = ('support_team',)
    search_fields = ['name']
    readonly_fields = ["status"]
    resource_class = ConfigureItemResource

@admin.register(application)
#class ApplicationAdmin(admin.ModelAdmin):
class ApplicationAdmin(ImportExportModelAdmin):
    list_display = ["name","posx","posy","create_at","update_at"]
    filter_horizontal = ('configure_item',)
    search_fields = ['name']
    readonly_fields = ["status"]
