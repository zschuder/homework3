#min and max but with loops
#myList = [2,1,5,3]
#minimum = myList[0]
#maximum = myList[1]
#def find_min_max(myList,minimum,maximum):
#    for i in myList:
#        if i < minimum:
#            minimum = i
#        elif i > maximum:
#            maximum = i 
#    return minimum, maximum
#print(find_min_max(myList,minimum,maximum))

#min and max but with loops
myList = []
n = int(input("Enter number of elements in list: "))
for i in range(n):
    nums = int(input("Enter an element: "))
    myList.append(nums)
print(myList)
minimum = myList[0]
maximum = myList[1]

#min for loop function
#def find_min_forLoop(myList,minimum):
#    for i in myList:
#        if i < minimum:
#            minimum = i
#    return minimum
#print(find_min_forLoop(myList,minimum))

#min while loop function
#def find_min_whileLoop(myList,minimum):
#    i = 0
#    while i != len(myList):
#        if myList[i] < minimum:
#            minimum = myList[i]
#        return minimum
#print(find_min_whileLoop(myList,minimum))

#max for loop function
#def find_max_forLoop(myList,maximum):
#    for i in myList:
#        if i > maximum:
#            maximum = i 
#    return maximum
#print(find_max_forLoop(myList,maximum))

#max while loop function
def find_max_whileLoop(myList,maximum):
    i = 0
    while i != len(myList):
        if myList[i] > maximum:
            maximum = myList[i]
        return maximum
print(find_max_whileLoop(myList,maximum))
