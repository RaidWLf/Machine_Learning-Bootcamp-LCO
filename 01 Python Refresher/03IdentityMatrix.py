sizeOfMatrix = int(input("Enter the no size of identity matrix: "))

for row in range(sizeOfMatrix):
    for col in range(sizeOfMatrix):
        if row == col:
            print("1", end=" ")
        else:
            print("0", end=" ")
    print() # used for changing 
        