# Generated by Django 4.0.1 on 2022-03-27 21:19

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('frontend', '0014_alter_customer_cust_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='email',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cust_email', to=settings.AUTH_USER_MODEL),
        ),
    ]
