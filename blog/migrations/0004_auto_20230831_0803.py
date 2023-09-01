# Generated by Django 3.2.20 on 2023-08-31 08:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0003_rehome'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='adoption',
            name='email',
        ),
        migrations.AddField(
            model_name='adoption',
            name='author',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='adoption_author', to='auth.user'),
            preserve_default=False,
        ),
    ]