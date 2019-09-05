# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class support_team(models.Model):
    id = models.AutoField(primary_key=True, serialize=False)
    name = models.CharField(max_length=50)
    region = models.CharField(max_length=50)
    email = models.CharField(max_length=200)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    status = models.IntegerField(default=1)
    class Meta:
        verbose_name = 'Support Team'
        verbose_name_plural = 'Support Team Management'
    def __str__(self):
        return self.name

class configure_item(models.Model):
    id = models.AutoField(primary_key=True, serialize=False)
    name = models.CharField(max_length=50)
    support_team = models.ManyToManyField(support_team)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    status = models.IntegerField(default=1)
    class Meta:
        verbose_name = 'Configure Item'
        verbose_name_plural = 'Configure Item Management'
    def __str__(self):
        return self.name

class application(models.Model):
    id = models.AutoField(primary_key=True, serialize=False)
    name = models.CharField(max_length=50)
    posx = models.IntegerField()
    posy = models.IntegerField()
    colspan = models.IntegerField(default=1)
    configure_item = models.ManyToManyField(configure_item)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    status = models.IntegerField(default=1)
    class Meta:
        verbose_name = 'Application'
        verbose_name_plural = 'Application Management'
    def __str__(self):
        return self.name

