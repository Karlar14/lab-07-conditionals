num1 = int(input("Enter a number: " ))
num2 = int(input("Enter another number: "))
operation = input("Choose an operation: ")

if operation == "x":
  print(int(num1 * num2))
elif operation == "/":
  print(int(num1 / num2))
elif operation == "%":
  print(int(num1 % num2))
