def student_grades(student):
    a = 0
    for i in student:        
        scores = student[a]["scores"]
        name = student[a]["name"]
        a += 1
        divisor = len(scores)

        total = 0
        for i in scores:
            total += i
        
        average = total/divisor
        
        grade = grading_system(average)
        print(f"{name} -> Average: {average} -> Grade: {grade}")
            
def grading_system(grade):
    if grade > 100:
        return "False"
    if grade >= 70 or grade <= 100:
        return "A"
    elif grade >= 60 or grade <= 69:
        return "B"
    elif grade >= 50 or grade <= 59:
        return "C"
    elif grade >= 45 or grade <= 49:
        return "D"
    elif grade >= 40 or grade <= 44:
        return "E"
    else:
        return "F"



student = [
    {"name": "Sam", "scores": [80, 90]},
    {"name": "David", "scores": [55, 60]}
]


student_grades(student)