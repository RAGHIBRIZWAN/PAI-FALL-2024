word = str(input('Enter the word: '))
ans = ''

for i in range(len(word)):
    ans += word[len(word)-1-i]

print(ans)
