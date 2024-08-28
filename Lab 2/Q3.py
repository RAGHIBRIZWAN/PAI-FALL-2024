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
