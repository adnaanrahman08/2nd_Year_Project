# Generated by Django 3.1.7 on 2021-03-19 19:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hire', '0006_application'),
    ]

    operations = [
        migrations.AddField(
            model_name='application',
            name='email',
            field=models.CharField(default='some@email.com', max_length=50),
        ),
        migrations.AddField(
            model_name='application',
            name='phone',
            field=models.CharField(default='000', max_length=50),
        ),
    ]
