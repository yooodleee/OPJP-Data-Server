# Generated by Django 5.1.4 on 2025-01-06 05:46

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BookRegistration',
            fields=[
                ('bookregistrationId', models.AutoField(primary_key=True, serialize=False)),
                ('bookCount', models.IntegerField(blank=True, null=True)),
                ('bookName', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='book_registration', to='books.books')),
            ],
            options={
                'db_table': 'book_registration',
            },
        ),
    ]