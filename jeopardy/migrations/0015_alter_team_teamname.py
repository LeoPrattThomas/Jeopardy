# Generated by Django 4.1.7 on 2023-03-12 02:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jeopardy', '0014_rename_team_name_team_teamname'),
    ]

    operations = [
        migrations.AlterField(
            model_name='team',
            name='teamName',
            field=models.CharField(max_length=50),
        ),
    ]