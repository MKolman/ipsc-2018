import requests
url1 = 'https://ipsc.ksp.sk/2018/practice/problems/r1'
url2 = 'https://ipsc.ksp.sk/2018/practice/problems/r2'
cookie = {}

for i in range(3):
    r = requests.post(url2, cookies=cookie)
    print(r.content)
