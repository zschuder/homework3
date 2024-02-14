weight = int(input("Enter a weight (kg): "))
height = int(input("Enter a height (m): "))
def bmi(weight,height):
    if weight <= 0 or height <= 0:
        print("Please enter a valid weight and/or height")
    else:
        return (weight / (height**2))
print(str(bmi(weight,height))+" (kg/(m^2))")