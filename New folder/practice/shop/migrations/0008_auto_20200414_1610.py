# Generated by Django 3.0.4 on 2020-04-14 10:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0007_auto_20200414_1550'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='c_phn',
            field=models.IntegerField(default='', max_length=10),
        ),
    ]
