# Generated by Django 4.1.5 on 2023-01-31 11:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=60)),
                ('phone_number', models.CharField(help_text='needs to be in this format 08100482341', max_length=11)),
                ('message', models.TextField(blank=True, null=True)),
            ],
        ),
    ]