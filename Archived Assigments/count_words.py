import re

# name = input("Please give name of file: ")
name = "video_script.txt"
handle = open(name, "r")

counts = dict()
for line in handle:
    words = line.split()
    for word in words:
        temp = re.sub( r'[^a-zA-Z0-9\s]' , '', word).lower()
        counts[temp] = counts.get(temp, 0) + 1


# print(count)

json = []
for word, count in counts.items():
    # print(word)
    # print(count)
    json.extend([{ "word" : word , "value" : count}])

print(json)

import pandas as pd
df = pd.DataFrame(json)
print(df.sort_values(by="value", ascending=False))

