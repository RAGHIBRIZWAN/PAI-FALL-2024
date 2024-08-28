def add(students_dict,grade,name):
    students_dict[name].append(grade) 
    return students_dict

def avg(students_dict,name):
    if name in students_dict:
        check = students_dict[name]
        avg = sum(check) / len(check)
        print(f"{name}'s average grade is {avg}.")
    else:
        print(f"Student {name} not found.")

def add_student(students_dict, name):
    if name not in students_dict:
        students_dict[name] = []
        print(f"Added new student {name} with an empty list of grades.")
    else:
        print(f"Student {name} already exists.")

def remove(students_dict,name):
    if name in students_dict:
        del students_dict[name]
        return students_dict
    else:
        print(f"Student {name} not found.")

students_dict = {}
num = int(input('Enter the number of students: '))

for i in range(num):
    name = input('Enter the name: ')
    grades = []
    gradeNum = int(input(f"Enter the number of grades for {name}: "))
    
    for j in range(gradeNum):
        grades.append(int(input(f"Enter grade {j + 1}: ")))
    
    students_dict[name] = grades

print(students_dict)
print(add(students_dict,50,'Raghib'))
print(avg(students_dict,'Raghib'))
print(add_student(students_dict,'Rabani'))
print(remove(students_dict,'Raghib'))
