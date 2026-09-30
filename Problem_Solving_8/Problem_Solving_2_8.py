import re

text = "omar is 20 years old and Ahmed is 21"

result = re.search(r"\d+", text)
print(result.group())
