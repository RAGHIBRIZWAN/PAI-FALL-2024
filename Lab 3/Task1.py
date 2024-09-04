try:
    with open(r'text.txt') as fileObj:
        content = fileObj.read()
except Exception as e:
    print(str(e))

word = content.split()

count1 = 0
count2 = 0

for i in range(len(content)):
    count1 += 1

for i in range(len(word)):
    count2 += 1

print(count1)
print(count2)
