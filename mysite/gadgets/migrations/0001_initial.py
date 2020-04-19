# Generated by Django 3.0.2 on 2020-02-28 15:13

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Type',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, validators=[django.core.validators.MinLengthValidator(2, 'Type must be greater than 1 character')])),
            ],
        ),
        migrations.CreateModel(
            name='Gadget',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nickname', models.CharField(max_length=200, validators=[django.core.validators.MinLengthValidator(2, 'Nickname must be greater than 1 character')])),
                ('price', models.PositiveIntegerField()),
                ('year', models.PositiveIntegerField()),
                ('notes', models.CharField(max_length=300)),
                ('type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gadgets.Type')),
            ],
        ),
    ]
