sum = 0
l = []
ans = []

num = int(input('Enter the length of list: '))
key = int(input('Enter the number: '))

for i in range(num):
    l.append(int(input('Enter the number to be input: ')))

for j in range(num):
    if l[j] >= key:
        ans.append(l[j])

print(ans)
