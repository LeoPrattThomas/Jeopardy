# Generated by Django 4.1.7 on 2023-03-11 20:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jeopardy', '0006_employee'),
    ]

    operations = [
        migrations.RenameField(
            model_name='question',
            old_name='root',
            new_name='topic',
        ),
        migrations.AddField(
            model_name='question',
            name='answer',
            field=models.TextField(default='None', max_length=255),
            preserve_default=False,
        ),
    ]
