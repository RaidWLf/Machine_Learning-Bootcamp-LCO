listSize1 = int(input("enter the size of list 1: "))
listSize2 = int((input("enter the size of list 2: ")))

list1 = []
list2 = []

for i in range(listSize1):
    list1+=[int(input("enter the input for list 1: "))]

for i in range(listSize2):
    list2+=[int(input("enter the input for list 2: "))]

mergeList = []
mergeList+= list1+list2

mergeList.sort()

print(mergeList)