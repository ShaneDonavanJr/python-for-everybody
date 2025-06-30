import re

text = "I am number 1one!"

clean_num = re.sub(r'\d+', '', text)
print(clean_num)

clean_char = re.sub(r'[^a-zA-Z0-9\s]', '', text)
print(clean_char)