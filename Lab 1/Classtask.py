marks = int(input('Enter the marks: '))

if marks >= 80:
    if marks >= 85:
        print('Congrats you are eligible for CS department in Section A')
    elif marks < 85:
        print('Congrats you are eligible for CS department in Section B')

elif marks >= 70:
    if marks >= 75:
        print('Congrats you are eligible for AI department in Section A')
    elif marks < 75:
        print('Congrats you are eligible for AI department in Section B')

elif marks >= 60:
    if marks >= 65:
        print('Congrats you are eligible for DS department in Section A')
    elif marks < 65:
        print('Congrats you are eligible for DS department in Section B')
