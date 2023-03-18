'''
MIT License
Copyright (C) 2023 Leo O. Pratt-Thomas
Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:
The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.
THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
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
