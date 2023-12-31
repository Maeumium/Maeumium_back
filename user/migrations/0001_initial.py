# Generated by Django 4.2.2 on 2023-08-12 12:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('id', models.CharField(max_length=24, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=24)),
                ('email', models.EmailField(default='example@example.com', max_length=254, unique=True)),
                ('nickname', models.CharField(default='default_nickname', max_length=24)),
                ('agreeTerms', models.BooleanField(default=None)),
            ],
            options={
                'db_table': 'User',
            },
        ),
    ]
