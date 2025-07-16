a = float(input("Enter first number: "))
b = float(input("Enter second number: "))

print(f"Addition: {a + b}")
print(f"Subtraction: {a - b}")
print(f"Multiplication: {a * b}")
print(f"Division: {'Cannot divide by zero' if b == 0 else a / b}")

