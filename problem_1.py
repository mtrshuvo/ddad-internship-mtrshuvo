def factorial(n):
        if n==1:
            return n
        elif n==0:
            return 1
        else:
            return n*factorial(n-1)

def input_value():
    number = int(input("Enter value: "))
    if number >= 0 and number <=10 :
        print(factorial(number))
    else:
        print("Enter between upto 10")
try:
    input_value()       
except ValueError:
    print("Enter valid number")


    
