num = int(input('Enter the length of lists: '))
list1 = []
list2 = []
dicts = {}

print('Input for list 1: ')
for i in range(num):
    list1.append(int(input('Enter the number: ')))

print('Input for list 2: ')
for i in range(num):
    list2.append(int(input('Enter the number: ')))

for i in range(len(list1)):
    dicts[list1[i]] = list2[i]

try:
    with open('text.txt', 'w') as fileObj:
       fileObj.write(str(dicts))
except Exception as e:
    print(str(e))
