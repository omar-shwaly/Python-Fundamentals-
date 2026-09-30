import re

text = "Omar is 20 years old Ahmed is 21 "
result = re.findall(r"\d+", text)
print(result)
