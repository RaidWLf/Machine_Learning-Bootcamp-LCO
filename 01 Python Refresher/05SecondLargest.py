noOfNumbers = int(input("Enter the no of numbers you want to put: "))

listOfNumbers = []

for i in range (noOfNumbers):
    listOfNumbers += [int(input("enter the number: "))]

listOfNumbers.sort()

maximum = listOfNumbers[-2]

print(f"Second largest number in the list {listOfNumbers} is {maximum}")