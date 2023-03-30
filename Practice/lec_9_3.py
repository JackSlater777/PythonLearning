# * Используя модуль urllib, соберите все ссылки на заданной веб-странице
# (http://google.com) и проверьте их работоспособность.

import re
from urllib import request


req = request.Request('http://google.com')
response = request.urlopen(req)
web_page = response.read()

pattern1 = re.compile('["]http://\S*["]')
pattern2 = re.compile('["]https://\S*["]')

res1 = re.findall(pattern1, str(web_page))
# print(res1)

res2 = re.findall(pattern2, str(web_page))
# print(res2)

for link in res1:
    link = link[1:-1]  # Обрезаем кавычки с краев
    print(link)
    req_link = request.Request(link)
    request.urlopen(req_link)

for link in res2:
    link = link[1:-1]  # Обрезаем кавычки с краев
    print(link)
    req_link = request.Request(link)
    request.urlopen(req_link)
