l = []
ans = 0
inp = int(input('Enter the number of elements: '))

for i in range(inp):
    l.append(int(input('Enter the element: ')))

for i in range(inp):
    if(ans < l[i]):
        ans = l[i]

print(ans)
