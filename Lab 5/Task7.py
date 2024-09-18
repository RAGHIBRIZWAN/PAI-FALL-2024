import re

text = '''Hello my name is raghib@gmail.com and my age is 19@gmail.com while helloWorld@gmail.com'''

splitList = re.split(' ',text)
email = []

for i in splitList:
    if(re.search('.com',i)):
        email.append(i)
        
print(email)
