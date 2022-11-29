number = int(input("Enter the no to check if it is palindrome: "))

number2 = number 

reverse = 0
while number > 0:
    a = number % 10
    reverse = reverse*10 + a

    number = number // 10

if reverse == number2:
    print(f"the Number {number2} is palindrome number ")

else:
    print(f"the number {number2} is not a palindrome number.")