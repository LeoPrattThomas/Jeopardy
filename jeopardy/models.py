'''
Copyright (C) 2023 Leo Pratt-Thomas
This program is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.
This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU General Public License for more details.
You should have received a copy of the GNU General Public License along with this program.  If not, see <https://www.gnu.org/licenses/>.
'''
from django.db import models
from colorfield.fields import ColorField

# Create your models here.

class Topic(models.Model):
    name = models.CharField(max_length=50)
    def __str__(self):
        return self.name

class Point(models.Model):
    points = models.IntegerField()
    def __str__(self):
        return str(self.points)

class Question(models.Model):
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    points = models.ForeignKey(Point, on_delete=models.CASCADE)
    question = models.TextField(max_length=255)
    color = ColorField(default='#EC008C')
    answer = models.TextField(max_length=255)
    def str(self):
        return f"{ str(self.topic) } for { str(self.points) } points"# : {self.question}"
    def __str__(self):
        return f"{ str(self.topic) } for { str(self.points) } points"# : {self.question}" 

class Team(models.Model):
    teamName = models.CharField(max_length=50)
    correct = models.ManyToManyField(Question,blank=True, related_name="correct")
    incorrect = models.ManyToManyField(Question,blank=True, related_name="incorrect")
    def __str__(self):
        return self.teamName
    color = ColorField(default='#FF0000')
