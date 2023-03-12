from django.db import models

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
    answer = models.TextField(max_length=255)
    def __str__(self):
        return f"{ str(self.topic) } for { str(self.points) } points : {self.question}" 

class Team(models.Model):
    teamName = models.CharField(max_length=50)
    qustionsAnsered = models.ManyToManyField(Question,blank=True)
    def __str__(self):
        return self.teamName
    is_turn = models.BooleanField(default=False)
