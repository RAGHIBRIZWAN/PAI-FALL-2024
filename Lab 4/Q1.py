a = ['He','th','i','sal']
b = ['llo','is','s','man']
c = []
d = ''
for i in range(len(a)):
    c.append(a[i] + b[i])
    d += a[i] + b[i]
    d += ' '
print(c)
print(d)
