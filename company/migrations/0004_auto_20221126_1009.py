# Generated by Django 3.1.2 on 2022-11-26 10:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0003_auto_20221126_0956'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='deleted_at',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
