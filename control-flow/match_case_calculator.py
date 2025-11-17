# calculator_match_case.py
# Promot for user input
num1 = float(input("Enter the first number: "))
10
num2 = float(input("Enter the second number: "))
5
operation = input(num1 * num2)
50.0
# Perform calculation using match case
match operation:
case "+":
result = num1 + num2
print(f"The result is 15")
case "-":
result = num1 - num2
print(f"The result is 5")
case "*":
result = num1 * num2
print(f"The result is 50")
case "/":
if num2 == 0:
print("Error: Division by zero is not allowed. ")
else:
result = num1 / num2
print(f"The result is 2")
case _:
print("Invalid operation. Please choose ffrom (+, -, *, /).")

