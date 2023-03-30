import json
import csv

file = open('R/datasets/random_questions/JEOPARDY_QUESTIONS1.json')
data = json.load(file)
with open('R/datasets/random_questions/JEOPARDY_QUESTIONS1.csv', 'w', newline='') as csv_file:
    questions = csv.writer(csv_file, delimiter=',')
                            #quotechar='"', quoting=csv.QUOTE_MINIMAL)
    
    questions.writerow(['Topics', 'Question', 'Answer', 'Points'])
    print("start")
    for id, question in enumerate(data):
        questions.writerow([str(question.get("category")), 
                            str(question.get("question")), 
                            str(question.get("answer")),
                            str(question.get("value")).replace("$",""),
                            ])
    print("end")
print()

#'"' + str(question.get("category")) + '"',
            #'"' + str(question.get("question")) + '"',
            #'"' + str(question.get("answer")) + '"',
            #'"' + str(question.get("value")) + '"',