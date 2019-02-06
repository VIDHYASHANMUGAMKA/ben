nu1 = input('Enter First Number: ')
nu2 = input('Enter Second Number: ')

print("Value of num1 before swapping: ", nu1)
print("Value of num2 before swapping: ", nu2)

# swapping two numbers using temporary variable
t = nu1
nu1 = nu2
nu2 = t

print("Value of num1 after swapping: ", nu1)
print("Value of num2 after swapping: ", nu2)
