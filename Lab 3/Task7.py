def replaceLetter(wrong,correct,word):
    try:
        with open('replacement_needed.txt','r') as fileObj:
            content = fileObj.read()
        
        newWord = ''
        length = len(word)
        index = 0

        while index < length:
            if word[index] == wrong:
                newWord += correct
            else:
                newWord += word[index]
            index += 1

        update = content.replace(word,newWord)
        
    except FileNotFoundError:
        print("The file does not exist.")
    except IOError:
        print("Issue occurred while reading the file.")
    except Exception as e:
        print(str(e))

    try:
        with open('replacement_needed.txt','w') as fileObj:
            fileObj.write(update)
        print("File updated successfully.")
    except FileNotFoundError:
        print("The file does not exist.")
    except IOError:
        print("Issue occurred while reading the file.")
    except Exception as e:
        print(str(e))

replaceLetter('S','R','Saghib')
