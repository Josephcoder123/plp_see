print("This is Joseph Calculator")
#  Welcome to the my Calculator! 
#  input the first number
# We're using 'float()' to make sure our numbers can have decimals too. 
num1 = float(input("Enter the first number: "))
#  input the second number
# Same trick here—using 'float()' 
num2 = float(input("Enter the second number: "))
# Add the two numbers 
sum_result = num1 + num2
# Subtract the second number from the first 
difference_result = num1 - num2
# Multiply the two numbers 
product_result = num1 * num2
# Divide the first number by the second 
quotient_result = num1 / num2
#  The reveal
print(f"Results of your two numbers:")
print(f"Sum: {sum_result}")  
print(f"Difference: {difference_result}")  
print(f"Product: {product_result}")  
print(f"Quotient: {quotient_result}")  