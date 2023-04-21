# Generated by Django 4.1.5 on 2023-04-09 05:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('datasheet', '0004_alter_guideline_options_guideline_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='guideline',
            name='status',
            field=models.CharField(choices=[('draft', 'Draft'), ('certified', 'Certified')], default='draft', max_length=10),
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=80)),
                ('email', models.EmailField(max_length=254)),
                ('body', models.TextField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('active', models.BooleanField(default=True)),
                ('guideline', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='datasheet.guideline')),
            ],
            options={
                'ordering': ('created',),
            },
        ),
    ]