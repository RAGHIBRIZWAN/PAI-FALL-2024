dict = {}
avg = 0
sums = 0
perc = 0

i = 0
while i < 3:
    key = str(input('Enter the key: '))
    value = int(input('Enter the marks: '))
    dict[key] = value
    sums += dict[key]
    i += 1

avg = sums / 3
perc = (sums / 300)*100
print(avg)
print(perc)
