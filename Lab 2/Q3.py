#METHOD 1:

def url_check(url):
    check = ''
    ans = ''
    for i in range(11):
        check += url[i]

    if check == 'http://www.':
        for i in range(11,len(url)):
            ans += url[i]

    return ans

print(url_check('http://www.raghib.com'))

#METHOD 2:

def url_check(url):
    if url.startswith('http://www.'):
        user_url = url[len('http://www.'):]
        return user_url
    else:
        return 'Invalid'

print(url_check('http://www.raghib.com'))
