# Generated by Django 4.1.4 on 2022-12-26 07:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('rank', models.IntegerField()),
                ('point', models.CharField(max_length=100)),
                ('desc', models.TextField()),
            ],
        ),
    ]
