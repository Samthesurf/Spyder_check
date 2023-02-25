student_scores = {
    'Harry': 81,
    'Ron':78,
    'Hermione':99,
    'Draco':74,
    'Neville':62,
}
# Don't change the above code

#Create a empty directory called student_grades
student_grades = {}
Outstanding = [x for x in range (91,101)]
Exceeds_Expectation = [x for x in range(81,91)]
Acceptable = [x for x in range(71,81)]
Fail = [x for x in range(0,71)]
def grades():
    for key,values in student_scores.items():
        if values in Outstanding:
            student_grades[key] = "Outstanding"
        elif values in Exceeds_Expectation:
            student_grades[key] = 'Exceeds Expectations'
        elif values in Acceptable:
            student_grades[key] = 'Acceptable'
        elif values in Fail:
            student_grades[key] = 'Fail'
grades()
#Write your code below to add the grades to the student_grades
print(student_grades)
#Nesting Dictionary and list in a Dictionary
travel_log = {
    'France':{
        'cities visited': ['Paris','Lille','Dijon'],
        'total visits':12,
    },
    'Germany':{
        'cities visited':['Berlin','Frankfurt'],
        'total visits':12
    }
}
#Nesting Dictionary in list
# travell_log = [{ 
        # 'country visited':'France'
        # 'cities visited': ['Paris','Lille','Dijon'],
        # 'total visits':12
    # },
    # {
        # 'country visited':'Germany'
        # 'cities visited':['Berlin','Frankfurt'],
        # 'total visits':12
    # }
# ]      