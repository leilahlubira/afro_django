# Generated by Django 4.2 on 2023-05-22 13:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('afro_dtl', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ChatBox',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('messenger', models.CharField(blank=True, max_length=100)),
                ('message', models.CharField(blank=True, max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='User_form_model',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=1000)),
                ('email', models.EmailField(max_length=1000)),
                ('occupation', models.CharField(max_length=1000)),
                ('message', models.TextField(max_length=1000)),
            ],
        ),
    ]