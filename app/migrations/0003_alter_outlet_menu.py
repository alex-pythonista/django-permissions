# Generated by Django 4.0.4 on 2022-05-04 18:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_outlet_menu'),
    ]

    operations = [
        migrations.AlterField(
            model_name='outlet',
            name='menu',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='app.menu'),
        ),
    ]
