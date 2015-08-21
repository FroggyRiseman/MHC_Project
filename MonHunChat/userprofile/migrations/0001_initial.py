# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('description', models.TextField(max_length=200, null=True, blank=True)),
                ('hunter_name', models.CharField(default=b'', max_length=30, blank=True)),
                ('nintendo_name', models.CharField(default=b'', max_length=30, blank=True)),
                ('skype_name', models.CharField(default=b'', max_length=30, blank=True)),
                ('teamspeak_name', models.CharField(default=b'', max_length=30, blank=True)),
                ('friend_code', models.CharField(default=b'', help_text=b'Please use the following format: <em>####-####-####</em>.', max_length=14, blank=True)),
                ('rank', models.CharField(default=b'LR', max_length=3, choices=[(b'LR', b'Low Rank'), (b'HR', b'High Rank'), (b'GR', b'G-Rank'), (b'GRP', b'G-Rank 100-998'), (b'GM', b'G-Rank 999')])),
                ('weapon', models.CharField(default=None, max_length=3, null=True, blank=True, choices=[(b'GS', b'Greatsword'), (b'LS', b'Longsword'), (b'SNS', b'Sword & Shield'), (b'DB', b'Dual Blades'), (b'HAM', b'Hammer'), (b'HH', b'Hunting Horn'), (b'LAN', b'Lance'), (b'GL', b'Gunlance'), (b'SA', b'Switch Axe'), (b'CA', b'Charge Axe'), (b'IG', b'Insect Glaive'), (b'TON', b'Tonfa'), (b'BOW', b'Bow'), (b'HBG', b'Heavy Bowgun'), (b'LBG', b'Light Bowgun')])),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
