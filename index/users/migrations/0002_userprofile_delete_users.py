# Generated by Django 4.2.4 on 2023-08-14 12:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('username', models.CharField(max_length=255)),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('photo', models.CharField(max_length=255)),
                ('phone_number', models.CharField(max_length=255)),
                ('region', models.CharField(choices=[('UNKNOWN', 'Unknown')], default='UNKNOWN', max_length=255)),
                ('id', models.UUIDField(primary_key=True, serialize=False)),
                ('password', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField()),
                ('updated_at', models.DateTimeField()),
                ('payment_status', models.BooleanField(default=True)),
                ('leaderboard_rate', models.IntegerField(default=0)),
                ('basket', models.JSONField(default=list)),
            ],
        ),
        migrations.DeleteModel(
            name='Users',
        ),
    ]
