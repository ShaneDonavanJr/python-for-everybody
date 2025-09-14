# import re

# text = open("regex_sum_2246526.txt")
# all_num = []
# count = 0

# for line in text:
#     count = count + 1
#     line_num = re.findall("[0-9]+", line)
#     all_num.extend(line_num)

# print(all_num)
# print(f"Total lines: {count}")

# all_num = [ int(num) for num in all_num ]

# total = 0
# for num in all_num:
#     total = total + num

# print(total)


import re
print ( sum( [ int(a) for a in re.findall( "[0-9]+" ,  open("regex_sum_2246526.txt").read() ) ] ) )

