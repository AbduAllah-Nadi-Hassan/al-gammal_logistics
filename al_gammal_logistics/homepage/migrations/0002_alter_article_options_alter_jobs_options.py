# Generated by Django 5.1 on 2024-08-12 04:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='article',
            options={'verbose_name': 'Article', 'verbose_name_plural': 'Articles'},
        ),
        migrations.AlterModelOptions(
            name='jobs',
            options={'verbose_name': 'Job', 'verbose_name_plural': 'Jobs'},
        ),
    ]
