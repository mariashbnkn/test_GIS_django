# Generated by Django 4.2.2 on 2023-08-25 11:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('terzone', '0006_create_plan_reg'),
    ]

    operations = [
        migrations.AddField(
            model_name='planregulation',
            name='index',
            field=models.CharField(default='-', max_length=100),
        ),
    ]