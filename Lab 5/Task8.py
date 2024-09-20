import re

text = "20/9/2024 2024-09-20 Sep 20 2024"

check = r"\b(\d{1,2}/\d{1}/\d{4}|\d{4}-\d{1,2}-\d{1,2}|[A-Za-z]{3,} \d{1,2} \d{4})\b"

x = re.findall(check,text)

for date in x:
    print(date)
