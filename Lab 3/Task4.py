name = str(input('Enter your name: '))
cnic = int(input('Enter your cnic number: '))
age = int(input('Enter your age: '))
salary = int(input('Enter your salary: '))

list1 = [name,cnic,age,salary]
try:
    with open('text.txt','a') as fileObj:
        for i in range(len(list1)):
            fileObj.write(str(f"{list1[i]}\n"))
except Exception as e:
    print(str(e))

number = int(input('Enter your contact number: '))

try:
    with open('text.txt','a') as fileObj:
        fileObj.write(str(number))
except Exception as e:
    print(str(e))
