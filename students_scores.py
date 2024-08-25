#students_scores = [ {'name': 'Alice', 'math': 85, 'science': 92, 'english': 88},
#                    {'name': 'Bob', 'math': 79, 'science': 85, 'english': 90},
#                    {'name': 'Charlie', 'math': 92, 'science': 87, 'english': 85} ]


students_scores = [ {'name': 'Alice', 'math': 85, 'science': 92, 'english': 88},
                    {'name': 'Bob', 'math': 79, 'english': 90},
                    {'name': 'Charlie', 'science': 87, 'english': 85},
                    {'name': 'David', 'math': 92, 'science': 89, 'english': 93} ]
#print(type(students_scores))
#print((students_scores[0]))
#print(type(students_scores[0]))

averages={}
top_student= ""
top_avrg= 0
for student in students_scores:
    #print(student["name"])
    scores = []
    for key, score in student.items():
        if key!= "name":
            scores.append(score)
    #print(scores)
    avrg = round(sum(scores) / len(scores),2)

    #avrg = round((student["math"] + student["science"] + student["english"])/3,2)
    #print(avrg)
    averages[student["name"]] = avrg
    
    if top_avrg<avrg:
        top_avrg = avrg
        top_student = student["name"]


averages["top_student"] = top_student
print(averages)

