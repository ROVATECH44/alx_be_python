# Prompt User for Pattern Size
size = int(input("Enter the size of the pattern: "))
4
#Initialize row counter
row = 0
# Use a while loop to iterate through rows
while row < size:
# Use a for loop to print asterisks side by side
for col in range(size):
print("+", end="")
# Move to the next line after each row
print()
row += 1

