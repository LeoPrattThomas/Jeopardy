# Generated by Django 4.1.7 on 2023-03-17 13:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jeopardy', '0022_question_color'),
    ]

    operations = [
        migrations.AlterField(
            model_name='team',
            name='incorrect',
            field=models.ManyToManyField(blank=True, related_name='incorrect', to='jeopardy.question'),
        ),
    ]
