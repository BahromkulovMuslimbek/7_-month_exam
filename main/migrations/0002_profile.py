# Generated by Django 5.1 on 2024-08-10 12:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=255, null=True)),
                ('phone', models.IntegerField(null=True)),
                ('adress', models.TextField(null=True)),
            ],
        ),
    ]
