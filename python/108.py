# Check Armstrong Number

def is_armstrong(number):
    digits = str(number)
    power = len(digits)

    total = sum(int(digit) ** power for digit in digits)

    return total == number


number = int(input("Enter a number: "))

if is_armstrong(number):
    print(number, "is an Armstrong number")
else:
    print(number, "is not an Armstrong number")