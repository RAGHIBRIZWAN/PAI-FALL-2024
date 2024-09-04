try:
    with open(r'text.txt') as fileObj:
        content = fileObj.read()
except Exception as e:
    print(str(e))

word1 = str(input('Enter the word you want to add: '))
word2 = str(input('Enter the word you want to remove: '))

replace = content.replace(word2,word1)

with open('text.txt', 'w') as fileObjs:
    fileObjs.write(replace)

try:
    with open(r'text.txt') as fileObj:
        content = fileObj.read()
except Exception as e:
    print(str(e))

print(content)
