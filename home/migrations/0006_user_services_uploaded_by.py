# Generated by Django 4.0.3 on 2022-05-26 05:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_remove_user_services_uploaded_by'),
    ]

    operations = [
        migrations.AddField(
            model_name='user_services',
            name='uploaded_by',
            field=models.CharField(default='vishavjeet@gmail.com', max_length=40),
            preserve_default=False,
        ),
    ]
