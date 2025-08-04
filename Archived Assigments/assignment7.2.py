'''
7.2 Write a program that prompts for a file name, then opens that 
file and reads through the file, looking for lines of the form:
X-DSPAM-Confidence:    0.8475
Count these lines and extract the floating point values from each of 
the lines and compute the average of those values and produce an 
output as shown below. Do not use the sum() function or a variable 
named sum in your solution.

You can download the sample data at http://www.py4e.com/code3/mbox-short.txt when you are testing below enter mbox-short.txt as the file name.
'''

# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
# fname = "mbox-short.txt"
fh = open(fname)

numbers = []

for line in fh:
    if not line.startswith("X-DSPAM-Confidence:"):
        continue

    # print(line)
    index = line.find(":") + 1
    number = line[index:].strip()
    try:
        number = float(number)
        # print(number)
    except:
        print("oops")
        print(f"Index used: {index}")
        print(f"Not a float: {line[index:]}")
        continue
    numbers.append(number)

total = 0

for num in numbers:
    total = total + num
    
average = total / len(numbers) 
print(f"Average spam confidence: {average}")
# print("Done")
