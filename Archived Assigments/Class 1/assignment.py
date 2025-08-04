'''

5.2 Write a program that repeatedly prompts a user for integer numbers until the 
user enters 'done'. Once 'done' is entered, print out the largest and smallest of the 
numbers. If the user enters anything other than a valid number catch it with a 
try/except and put out an appropriate message and ignore the number. Enter 7, 2, 
bob, 10, and 4 and match the output below.

'''
def get_int():
    try:
        # "Enter a number: "
        i = input()
        if i == "done":
            return i

        i = int(i)
    except: 
        print("Invalid input")
        i = get_int()
    return i

numbers = []

while True:
    num = get_int()
    if num == "done":
        break
    # print(num)
    numbers.append(num)

largest = max(numbers)
smallest = min(numbers)

print("Maximum is", largest)
print("Minimum is", smallest)