'''

3.1 Write a program to prompt the user for hours and rate per hour using input to compute gross pay. 
Pay the hourly rate for the hours up to 40 and 1.5 times the hourly rate for all hours worked above 40 hours. 
Use 45 hours and a rate of 10.50 per hour to test the program (the pay should be 498.75). 
You should use input to read a string and float() to convert the string to a number. 
Do not worry about error checking the user input - assume the user types numbers properly.

'''
def get_hrs():
    hrs = 0
    h = 0
    try:
        hrs = input("Enter Hours:")
        h = float(hrs)
    except:
        print("Error please use real numbers")
        hrs = get_hrs()

    return h 

def get_rt():
    rt = 0
    r = 0
    try:
        rt = input("Enter Hourly Rate:")
        r = float(rt)
    except:
        print("Error please use real numbers")
        r = get_rt()

    return r 


h = get_hrs()
r = get_rt()

pay = 0

if h >= 40:
    pay = (40 * r) + ( ( h % 40 ) * ( r * 1.5 ) )
else :
    pay = (40 * r)
print(pay)
