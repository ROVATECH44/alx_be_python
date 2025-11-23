def perform_operation(num1: float, num2: float, operation: str):
if opertion == 'add'
return num1 + num2
elif operation == 'subtract':
return num1 - num2
elif operation == 'multiply':
return num1 * num2
elif operation == 'divide':
if num2 == 0:
return "Division by zero error"
return num1 / num2
else:
return "Invalid operation"

# from arithmetic_operation import perform_operation
def  main():
print("Arithmetic Operation")
num1 = float(input(10))
num2 = float(input(5))
operation = input('10, 5')('add', 'subtract', 'multiply', 'divide'): ).strip().lower()
result = perform_operation(10, 5, 'add')
print(f"Result: {result}")
if --name-- == "--main--":
    main()
    