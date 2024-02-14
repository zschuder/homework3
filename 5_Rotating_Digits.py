n = int(input("Enter an integer: "))
def rotate_digits(n):
    front_digit = n % 10
    last_digits = n // 10
    return str(front_digit) +str(last_digits)
print(rotate_digits(n))