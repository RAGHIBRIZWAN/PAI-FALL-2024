def replaceLetter(wrong,correct):
    try:
        with open('replacement_needed.txt','r') as fileObj:
            content = fileObj.read()
        correctedContent = ''
        for char in content:
            if char == wrong:
                correctedContent += correct
            else:
                correctedContent += char

        print('Corrected content: ',correctedContent)

    except FileNotFoundError:
        print("The file does not exist.")
    except IOError:
        print("Issue occurred while reading the file.")
    except Exception as e:
        print(str(e))

    try:
        with open('replacement_needed.txt','w') as fileObj:
            fileObj.write(correctedContent)
    except FileNotFoundError:
        print("The file does not exist.")
    except IOError:
        print("Issue occurred while reading the file.")
    except Exception as e:
        print(str(e))

    

replaceLetter('S','R')
