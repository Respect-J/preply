# Generated by Django 4.2.4 on 2023-08-31 08:57

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('topics', '0001_initial'),
        ('subjects', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tests',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('language', models.CharField(choices=[('UZ', 'Uzbek'), ('EN', 'English'), ('RU', 'Russian'), ('KAA', 'Kazakh')], max_length=3)),
                ('is_mandatory', models.BooleanField(default=False)),
                ('correct_answer', models.CharField(choices=[('a', 'a'), ('b', 'b'), ('c', 'c'), ('d', 'd')], max_length=3)),
                ('options', models.JSONField()),
                ('subject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='subjects.subjects')),
                ('topic', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='topics.topics')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]