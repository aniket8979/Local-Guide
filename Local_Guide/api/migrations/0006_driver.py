# Generated by Django 4.1.5 on 2023-04-25 06:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_alter_user_city_alter_user_name_alter_user_phone_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Driver',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('unique_id', models.CharField(max_length=100, null=True)),
                ('dname', models.CharField(max_length=100, null=True)),
                ('dphone', models.CharField(max_length=15, null=True)),
            ],
        ),
    ]
