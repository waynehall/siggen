# Generated by Django 3.1.2 on 2020-10-29 17:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('signature', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='employeeinfo',
            name='employee_profile_pic',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
