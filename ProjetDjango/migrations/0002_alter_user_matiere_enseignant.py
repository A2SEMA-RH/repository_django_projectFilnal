# Generated by Django 4.1.4 on 2023-08-26 15:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('djangoApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='matiere_enseignant',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='djangoApp.matiere'),
        ),
    ]