# Generated by Django 3.2.20 on 2023-09-01 11:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_auto_20230901_1151'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rehome',
            name='age',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='What age is your Fox Terrier?'),
        ),
        migrations.AlterField(
            model_name='rehome',
            name='email',
            field=models.EmailField(blank=True, max_length=100, null=True, verbose_name='Your Email Address'),
        ),
        migrations.AlterField(
            model_name='rehome',
            name='sex',
            field=models.CharField(blank=True, choices=[('Male', 'Male'), ('Female', 'Female')], max_length=10, null=True, verbose_name='Is your Fox Terrier Male or Female?'),
        ),
    ]
