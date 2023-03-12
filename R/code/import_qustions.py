from jeopardy.models import *
import csv

f = open("R/datasets/Jeopardy.csv")
freader = csv.reader(f)
print("hi")
print(freader.__next__())  # the header row

for row in freader:
    topic = Topic.objects.get(name = row[1])#load forine key
    points = Point.objects.get(points = int(row[2]))#load forine key

    question = Question(topic = topic, 
                        points = points, 
                        question = row[3], 
                        answer = row[4], 
                        id = int(row[0]))
    print(question)
    question.save()
    


    