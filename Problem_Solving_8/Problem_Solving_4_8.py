import re

text = "Omar has 25 apples and 30 oranges"

result = re.findall(r"[0-9]+", text)
print(result)
