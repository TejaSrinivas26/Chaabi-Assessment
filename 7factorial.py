#lambda function to calculate factorial
factorial = lambda n: 1 if n == 0 else n * factorial(n - 1)
#lambda function takes a number 'n' as input and recursively calculates its factorial.

# Test the factorial lambda function
number = 5  
result = factorial(number)  
print(result)  # Print the result

# Output:
# 120
