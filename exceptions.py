x = 0
while x == 0:
    try:
        num_1 = int(input())
        a = 5 // num_1
        print("here is our number, daddy: " + str(a))
    except ZeroDivisionError:
        print("Enter smth diff from 0 u dumass")