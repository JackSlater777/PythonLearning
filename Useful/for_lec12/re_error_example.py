import re


res = []
p = re.compile(r'(ERROR-\d+)')
with open('logfile.txt', 'r') as f:
    for line in f:
        lst = re.findall(p, line)
        res.extend(lst)

print(res)
