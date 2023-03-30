import re

s = 'netops.microsoft.com - - [01/Jul/1995:07:43:07 -0400] "GET /history/gemini/gemini.html HTTP/1.0" 200 2522'
# netops.microsoft.com - 01/Jul/1995:07:43:07 -0400

res = re.findall(r'(.*) - - \[(.*)\] ".*$', s)
print(res)
