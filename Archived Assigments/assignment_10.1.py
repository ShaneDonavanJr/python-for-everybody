

# name = input("Enter file:")
name = "mbox-short.txt"
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)

count = dict()

for line in handle:
    # print(line)
    if line.startswith("From "):
        # print(line)
        time = line.split(" ")[6]
        # print(time)
        hour = time.split(":")[0]
        # print(hour)
        count[hour] = count.get(hour, 0) + 1

# print(count)

sort_count = sorted([ (k, v) for k, v in count.items() ])


for hour, count in sort_count:
    print(f"{hour} {count}")

