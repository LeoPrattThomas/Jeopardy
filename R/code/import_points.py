from jeopardy.models import *
import csv

f = open("R/datasets/Points.csv")
freader = csv.reader(f)

print(freader.__next__())  # the header row
for row in freader:
    #print(row)
    points = Point(points=row[1], id = row[0])
    print(points)
    points.save()