def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

# Taking input from user
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

# Calculating GCD
result = gcd(num1, num2)

print("The GCD of", num1, "and", num2, "is:", result)
