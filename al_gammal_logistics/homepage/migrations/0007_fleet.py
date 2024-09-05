# Generated by Django 5.1 on 2024-09-05 11:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0006_alter_article_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Fleet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name="Fleet's name")),
                ('description', models.TextField(verbose_name="Fleet's Description")),
            ],
            options={
                'verbose_name': 'Fleet',
                'verbose_name_plural': 'Fleets',
            },
        ),
    ]