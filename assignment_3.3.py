'''
3.3 Write a program to prompt for a score between 0.0 and 1.0. If the score is out of range, print an error. If the score is between 0.0 and 1.0, print a grade using the following table:
Score Grade
>= 0.9 A
>= 0.8 B
>= 0.7 C
>= 0.6 D
< 0.6 F
If the user enters a value out of range, print a suitable error message and exit. For the test, enter a score of 0.85.

'''

def grade_score(int): 
 if int >= .9:
    return "A"
 elif int >= .8:
    return "B"
 elif int >= .7:
    return "C"
 elif int >= .6:
    return "D"
 else:
    return "F"

def get_score():
    score = 0
    s = 0
    
    try:
        score = input("Enter Score: ")
        s = float(score)
    except :
        print("ERROR please enter a real number")
        s = get_score()
    return s

s = get_score()
while s >= 1 or s <= 0:
    print("Number must be between 0-1")
    s = get_score()

g = grade_score(s)
print(g)


