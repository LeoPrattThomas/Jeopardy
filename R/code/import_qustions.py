'''
MIT License
Copyright (C) 2023 Leo O. Pratt-Thomas
Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:
The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.
THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
'''
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
                        color = row[5], 
                        id = int(row[0]))
    print(question)
    question.save()
    


    