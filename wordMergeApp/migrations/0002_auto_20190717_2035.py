# Generated by Django 2.2.3 on 2019-07-17 20:35

from django.db import migrations
import oauth2client.contrib.django_util.models


class Migration(migrations.Migration):

    dependencies = [
        ('wordMergeApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='group',
            name='token',
            field=oauth2client.contrib.django_util.models.CredentialsField(blank=True, editable=False, null=True),
        ),
    ]
