# Generated by Django 4.1.3 on 2023-02-14 23:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jeopardy', '0003_rename_teams_team'),
    ]

    operations = [
        migrations.AlterField(
            model_name='topic',
            name='name',
            field=models.CharField(max_length=50),
        ),
    ]
