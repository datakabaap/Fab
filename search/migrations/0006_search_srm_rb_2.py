# Generated by Django 2.2.9 on 2020-03-04 12:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('search', '0005_auto_20200221_1834'),
    ]

    operations = [
        migrations.AddField(
            model_name='search',
            name='SRM_Rb_2',
            field=models.CharField(max_length=500, null=True),
        ),
    ]
