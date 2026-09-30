import re

txt = "my phone is 01093584500"
result = re.search(r"\d+", txt)

print(result.group())
