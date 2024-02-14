#power of a number
#x = int(input("Enter a base: "))
#y = int(input("Enter an exponent: "))
#def power(x, y):
#    answer = 1
#    for i in range(y):
#        answer = answer * x 
#    return answer
#print(power(2,3))

#Power of a Number
x = int(input("Enter a base value:"))
y = int(input("Enter of an exponent value:"))
def power_function(x, y): 
    answer = 1
    for i in range(y):
        answer = answer * x
    return answer
print(power_function(x,y))