# Generated by Django 3.2.3 on 2021-05-18 02:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Banking_System', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cutomers',
            name='phone_no',
            field=models.IntegerField(),
        ),
    ]
