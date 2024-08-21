i = 0
sums = 0
highest = 0
marksInput = 0
dict = {}
while i < 3:
    marksInput = int(input('Enter the marks:'))
    key = str(input('Enter the key'))
    dict[key] = marksInput
    i += 1

for x in dict:
    sums += dict[x]

    if highest < dict[x]:
        highest = dict[x]

avg = sums / 3
print(avg)
print(highest)
