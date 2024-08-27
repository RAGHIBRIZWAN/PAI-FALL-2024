def isPalindrome(word):
    i = 0
    j = len(word)-1

    while(i < j):
        if(word[i] == word[j]):
            i += 1
            j -= 1
        else:
            return 'Not a Palindrome'
    return 'Palindrome'

word = str(input('Enter the word: '))
print(isPalindrome(word))
