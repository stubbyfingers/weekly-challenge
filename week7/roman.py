def roman(numeral):
    conv = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
    }
    result = 0
    for i in range(len(numeral)):
        if i<len(numeral)-1 and conv[numeral[i]] < conv[numeral[i+1]]:
            result -= conv[numeral[i]]
        else:
            result += conv[numeral[i]]
    return (f"Which is: {result}")

numeral = input("Give me your roman numerals: ")
print(roman(numeral))

# def student_grades(score):
#     grades = {
#         "A": 70,
#         "B": 60,
#         "C": 50,
#         "D": 45,
#         "E": 40,
#         "F": 0
#     }
#     for grade in grades:
#         if score >= grades[grade]:
#             return grade

# score = int(input("Enter your score: "))
# print(student_grades(score))