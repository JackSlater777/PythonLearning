import re
lst = ["_a", "b", "__c", "_d"]
# Найти все protected атрибуты
# _a, _d

pattern = re.compile('^_[^_]')
result = []
for i in lst:
    result += re.findall(pattern, i)

print(result)
