sentence = str(input('Enter the sentence: '))

for i in range(len(sentence)):
    if sentence[i] == '?':
        try:
            with open('Questions.txt', 'w') as fileObj:
                fileObj.write(sentence)
        except Exception as e:
            print(str(e))
