# Generated by Django 2.2.1 on 2019-09-02 05:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('servicenow', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='application',
            name='Colspan',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='application',
            name='Posx',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='application',
            name='Posy',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]