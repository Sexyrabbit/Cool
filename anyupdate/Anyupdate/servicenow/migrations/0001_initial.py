# Generated by Django 2.2.1 on 2019-08-30 09:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Application',
            fields=[
                ('app_name', models.CharField(max_length=50, primary_key=True, serialize=False, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='ConfigItem',
            fields=[
                ('ci', models.CharField(max_length=50, primary_key=True, serialize=False, unique=True)),
                ('app', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='configitem', to='servicenow.Application')),
            ],
        ),
        migrations.CreateModel(
            name='Incident',
            fields=[
                ('inc_id', models.CharField(max_length=50, primary_key=True, serialize=False, unique=True)),
                ('short_desc', models.TextField(blank=True, max_length=500)),
                ('parent', models.CharField(blank=True, max_length=100, null=True)),
                ('children', models.CharField(blank=True, max_length=500, null=True)),
                ('configitem', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='incs', to='servicenow.ConfigItem')),
            ],
        ),
    ]
