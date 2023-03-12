from jeopardy.models import *
import csv

f = open("R/datasets/Topic.csv")
freader = csv.reader(f)

print(freader.__next__())  # the header row
for row in freader:
    #print(row)
    topic = Topic(name=row[1], id = row[0])
    topic.save()
    