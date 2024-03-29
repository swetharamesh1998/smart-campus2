# Generated by Django 2.2.3 on 2019-07-29 07:23

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='entry',
            fields=[
                ('uid', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('passcode', models.CharField(max_length=8, validators=[django.core.validators.MinLengthValidator(8)])),
                ('status', models.CharField(default='P', max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='events',
            fields=[
                ('mid', models.TextField(max_length=17, primary_key=True, serialize=False)),
                ('EventName', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='students',
            fields=[
                ('usn1', models.CharField(max_length=10, primary_key=True, serialize=False, validators=[django.core.validators.MinLengthValidator(10, message=None)])),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='SubID',
            fields=[
                ('subid', models.CharField(max_length=8, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subname', models.CharField(max_length=30)),
                ('subid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='student.SubID')),
            ],
        ),
        migrations.CreateModel(
            name='details',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.TextField()),
                ('ph_no', models.CharField(max_length=10, validators=[django.core.validators.MinLengthValidator(10, message=None)])),
                ('email', models.EmailField(default='Enter Email', max_length=254)),
                ('dept', models.CharField(max_length=3, validators=[django.core.validators.MinLengthValidator(2, message=None)])),
                ('blood_group', models.CharField(max_length=3)),
                ('parent_name', models.CharField(max_length=50)),
                ('parent_phno', models.CharField(max_length=10, validators=[django.core.validators.MinLengthValidator(10, message=None)])),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='student.students')),
            ],
        ),
        migrations.CreateModel(
            name='CheckIn',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('checkInTime', models.DateTimeField(auto_now=True)),
                ('mid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='student.events')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='student.students')),
                ('uid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='student.entry')),
            ],
        ),
        migrations.CreateModel(
            name='Authenticate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pwd', models.TextField()),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='student.students')),
                ('uid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='student.entry')),
            ],
        ),
    ]
