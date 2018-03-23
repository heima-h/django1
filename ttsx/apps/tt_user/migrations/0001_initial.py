# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone
from django.conf import settings
import django.core.validators
import django.contrib.auth.models


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0006_require_contenttypes_0002'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, verbose_name='last login', null=True)),
                ('is_superuser', models.BooleanField(help_text='Designates that this user has all permissions without explicitly assigning them.', default=False, verbose_name='superuser status')),
                ('username', models.CharField(validators=[django.core.validators.RegexValidator('^[\\w.@+-]+$', 'Enter a valid username. This value may contain only letters, numbers and @/./+/-/_ characters.', 'invalid')], error_messages={'unique': 'A user with that username already exists.'}, verbose_name='username', max_length=30, unique=True, help_text='Required. 30 characters or fewer. Letters, digits and @/./+/-/_ only.')),
                ('first_name', models.CharField(blank=True, verbose_name='first name', max_length=30)),
                ('last_name', models.CharField(blank=True, verbose_name='last name', max_length=30)),
                ('email', models.EmailField(blank=True, verbose_name='email address', max_length=254)),
                ('is_staff', models.BooleanField(help_text='Designates whether the user can log into this admin site.', default=False, verbose_name='staff status')),
                ('is_active', models.BooleanField(help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', default=True, verbose_name='active')),
                ('date_joined', models.DateTimeField(verbose_name='date joined', default=django.utils.timezone.now)),
                ('update_date', models.DateField(auto_now=True, verbose_name='修改时间')),
                ('add_date', models.DateField(auto_now_add=True, verbose_name='添加时间')),
                ('isDelete', models.BooleanField(default=False, verbose_name='逻辑删除')),
                ('groups', models.ManyToManyField(to='auth.Group', blank=True, verbose_name='groups', related_name='user_set', help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_query_name='user')),
                ('user_permissions', models.ManyToManyField(to='auth.Permission', blank=True, verbose_name='user permissions', related_name='user_set', help_text='Specific permissions for this user.', related_query_name='user')),
            ],
            options={
                'db_table': 'tt_user',
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('update_date', models.DateField(auto_now=True, verbose_name='修改时间')),
                ('add_date', models.DateField(auto_now_add=True, verbose_name='添加时间')),
                ('isDelete', models.BooleanField(default=False, verbose_name='逻辑删除')),
                ('recevier', models.CharField(max_length=10)),
                ('addr', models.CharField(max_length=20)),
                ('code', models.CharField(max_length=6)),
                ('recevier_mobile', models.CharField(max_length=11)),
                ('isDefault', models.BooleanField(default=0)),
            ],
            options={
                'db_table': 'df_address',
            },
        ),
        migrations.CreateModel(
            name='AreaInfo',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('title', models.CharField(max_length=20)),
                ('aParent', models.ForeignKey(blank=True, null=True, to='tt_user.AreaInfo')),
            ],
            options={
                'db_table': 'tt_area',
            },
        ),
        migrations.AddField(
            model_name='address',
            name='city',
            field=models.ForeignKey(to='tt_user.AreaInfo', related_name='city'),
        ),
        migrations.AddField(
            model_name='address',
            name='district',
            field=models.ForeignKey(to='tt_user.AreaInfo', related_name='district'),
        ),
        migrations.AddField(
            model_name='address',
            name='province',
            field=models.ForeignKey(to='tt_user.AreaInfo', related_name='province'),
        ),
        migrations.AddField(
            model_name='address',
            name='user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
        ),
    ]
