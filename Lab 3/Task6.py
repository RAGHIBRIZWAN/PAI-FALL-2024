def ask(sentence):
    try:
        if sentence[len(sentence)-1] == '?':
            with open('Questions.txt', 'w') as fileObj:
                fileObj.write(sentence)
                print('It is a question, Accepted!')
        else:
            print('Not a question!')
    except IOError as e:
        print(str(e))
    except Exception as a:
        print(str(a))

sentence = str(input('Enter the sentence: '))

ask(sentence)
