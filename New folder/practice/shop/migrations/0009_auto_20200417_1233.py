# Generated by Django 3.0.4 on 2020-04-17 07:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0008_auto_20200414_1610'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Employee',
        ),
        migrations.RemoveField(
            model_name='customer',
            name='id',
        ),
        migrations.AlterField(
            model_name='customer',
            name='c_mail',
            field=models.EmailField(default='', max_length=254, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='customer',
            name='c_phn',
            field=models.IntegerField(default='9013250804', max_length=10),
        ),
    ]
