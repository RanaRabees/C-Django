# Generated by Django 3.1.2 on 2022-04-08 10:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CNIC',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=50)),
                ('father_name', models.CharField(default='', max_length=50)),
                ('gender', models.CharField(default='', max_length=50)),
                ('country', models.CharField(default='', max_length=50)),
                ('date_birth', models.CharField(default='', max_length=50)),
            ],
        ),
    ]
