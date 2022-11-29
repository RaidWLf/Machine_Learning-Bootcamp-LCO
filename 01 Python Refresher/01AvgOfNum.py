noOfNumbers = int(input("enter the no of numbers you want to enter: "))

listOfNum = []

for i in range(0, noOfNumbers):
    number = int(input("Enter the Number: "))
    listOfNum += [number]


avgOfNumbers = sum(listOfNum)/noOfNumbers

print(f"avg of numbers = {round(avgOfNumbers, 3)}")