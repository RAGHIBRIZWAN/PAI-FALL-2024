def check(word):
    check = word[len(word) - 1]
    for i in range(len(word)):
        if check == 'a' or check == 'e' or check == 'i' or check == 'o' or check == 'u':
            return 'Last letter is vowel!'
    return 'Last letter is consonant!'

word = str(input('Enter the word: '))

print(check(word))
