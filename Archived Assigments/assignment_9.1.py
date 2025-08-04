
row = dict()
row["a"] = 1
print(row.items())

name = input("Enter file:")
# name = "mbox-short.txt"
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)

# print(handle)

count = dict()

for line in handle:
    if line.startswith("From "):
        email = line.split(" ")[1]
        count[email] = count.get(email, 0) + 1

# print(count)

max_email = 0       
max_value = 0

for email in count:
    # print(email)
    if count[email] > max_value:
        max_value = count[email]
        max_email = email


# print(f"{max_email} {max_value}")