def fibonacci(n):
    first, second = 0, 1
    count = 0
    
    while count<n:
        print(first, end=" ")
        result = first + second
        first = second
        second = result
        count += 1

def input_value():
    number = int(input("Enter value: "))
    if number > 0 and number <=20 :
        fibonacci(number)
    else:
        print("Enter value any value betwwen 1 to 20")

try:
    input_value()       
except ValueError:
    print("Enter valid number")
