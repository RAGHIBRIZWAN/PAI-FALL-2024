sum = 0
l = []

num = int(input('Enter the length of list: '))

for i in range(num):
    l.append(int(input('Enter the number: ')))

for j in range(num):
    sum += l[j]

print(sum)
