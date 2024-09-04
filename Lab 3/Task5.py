import json

lists = []
check = False

try:
    num = int(input('Enter the number of people: '))
    dicts = {}

    for i in range(num):
        name = str(input('Enter your name: '))
        age = int(input('Enter your age: '))
        dicts[name] = age

    with open('Task5.json','w') as fileObj:
        json.dump(dicts,fileObj)
except FileNotFoundError:
    print("The file does not exist.")
except IOError:
     print("Issue occurred while reading the file.")
except Exception as e:
    print(str(e))

try:
    with open('Task5.json','r') as fileObj:
        lists = json.load(fileObj)
        maxAge = lists[name]
        for i in lists:
            if maxAge < lists[i]:
                maxAge = lists[i]
        print('Max age is: ',maxAge)

        for i in lists:
            for j in lists:
                if lists[i] == lists[j]:
                    same = lists[i]
                    check = True
                    break
            if check:
                break
        print('Same age is: ',same)
except FileNotFoundError:
    print("The file does not exist.")
except IOError:
    print("Issue occurred while reading the file.")
except Exception as e:
    print(str(e))
