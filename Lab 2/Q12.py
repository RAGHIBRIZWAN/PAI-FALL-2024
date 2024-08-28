def makeDict(list1,list2):
    dict = {}
    for i in range(len(list1)):
        dict[list1[i]] = list2[i]
    
    return dict

num = int(input('Enter the number elements in a list: '))
list1 = []
list2 = []
for i in range(num):
    list1.append(int(input('Enter the element for list 1: ')))

for i in range(num):
    list2.append(int(input('Enter the element for list 2: ')))

print(makeDict(list1,list2))
