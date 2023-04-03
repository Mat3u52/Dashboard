# Generated by Django 4.1.5 on 2023-03-13 18:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('datasheet', '0003_guideline_image'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='guideline',
            options={'ordering': ('-publish_date',)},
        ),
        migrations.AddField(
            model_name='guideline',
            name='status',
            field=models.CharField(choices=[('draft', 'Draft'), ('published', 'Published')], default='draft', max_length=10),
        ),
    ]