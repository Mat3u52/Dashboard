# Generated by Django 4.1.5 on 2023-02-10 06:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('datasheet', '0002_guideline_version'),
    ]

    operations = [
        migrations.AddField(
            model_name='guideline',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]
