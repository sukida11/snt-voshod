# Generated by Django 4.1 on 2022-09-05 19:33

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0002_alter_forumquestion_pub_date_alter_reply_pub_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='forumquestion',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2022, 9, 5, 19, 33, 22, 40762, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='reply',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2022, 9, 5, 19, 33, 22, 41978, tzinfo=datetime.timezone.utc)),
        ),
    ]
