def palindrome(word):
    if len(word)<1:
        return True
    else:
        if word[0] == word[-1]:
            return palindrome(word[1:-1])
        else:
            return False

def input_value():
    value = str(input("Enter string value: ")).lower()
    if(palindrome(value)==True):
        if len(value)%2==0:
            print("Even palindrome")

        else:
            print("Odd palindrome")

    else:
        print("Not a palindrome")

input_value()