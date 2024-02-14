#Digital Root
number = int(input("Enter an integer: "))
def digital_root(number):
    sum = 0
    number = str(number)
    digits = list(number)
    for [i] in digits:
        sum = sum + int(i)
    return sum
print(digital_root(number))