# Generated by Django 3.0.3 on 2020-02-12 03:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('digitalbeti', '0003_auto_20200211_1833'),
    ]

    operations = [
        migrations.AddField(
            model_name='digitalbetiuser',
            name='city',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='digitalbetiuser',
            name='district',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='digitalbetiuser',
            name='state',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='digitalbetiuser',
            name='village',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='address',
            name='city',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='address',
            name='district',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='address',
            name='village',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]