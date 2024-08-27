# Fibbonacci sequence calculation
n=int(input("Enter the nth term of Fibonacci Sequence:"))
a, b = 0, 1
fibonacci = []
for i in range(n):
    fibonacci.append(a)
    a, b = b, a + b
print(f"Fibbonacci sequence of {n} numbers: {fibonacci}")  

# Find (minimum) and (maximum) in  (list)
numbers=[]
print("Enter the list value")
while True:
  x=input()
  if x==" ":
    break
  else:
    numbers.append(int(x))
print(f"Minimum value: {min(numbers)}")
print(f"Maximum value: {max(numbers)}")

# Basic arithmetic calculations
x = int(input("Enter x value: "))
y = int(input("Enter y value: "))
sum = x + y
difference = x - y
product = x * y
if y ==0:
    quotient="undefined number"
else:
    quotient = x / y
print(f"Sum: {sum}, Difference: {difference}, Product: {product}, Quotient: {quotient}")

# Prime number check
num = int(input("Enter a number: "))
is_prime = True
if num==1:
    print("1 is not a prime number")
else:
    for i in range(2, num//2):
        if (num % i) == 0:
            is_prime = False
            break
    if is_prime:
        print(f"{num} is a prime number")
    else:
        print(f"{num} is not a prime number")

original_string = input("Enter text: ")
reversed_string = ""
for i in range(len(original_string)-1, 0, -1):
    reversed_string += original_string[i]
reversed_string += original_string[0]
print("Original string:", original_string)
print("Reversed string:", reversed_string)

# Sum of squares of first n natural numbers
n = int(input("Enter a number: "))
sum_of_squares = 0
for i in range(1,n+1): 
    sum_of_squares += i**2  
print(f"Sum of squares of first {n} natural numbers: {sum_of_squares}")

# Count the number of vowels in a string
string = input("Enter a string: ")
vowels = "aeiouAEIOU"
vowel_count = 0
for char in string:
    if char in vowels:
        vowel_count += 1
print(f"Number of vowels in the string: {vowel_count}")

# Palindrome check
word = input("Enter a word: ")
is_palindrome = True
for i in range(len(word)//2):
    print(word[i], word[-i-1]) 
    if word[i] != word[-i-1]: 
        is_palindrome = False
        break
if is_palindrome:
    print(f"{word} is a palindrome")
else:
    print(f"{word} is not a palindrome")

# Sum of positive elements in a list
numbers=[]
print("Enter the list value")
while True:
  x=input()
  if x==" ":
    break
  else:
    numbers.append(int(x))
sum_elements = 0
for num in numbers: 
    if num > 0:
        sum_elements += num
print(f"Sum of elements: {sum_elements}")

# Factorial calculation
n = int(input("Enter number: "))
if n<0:
    print("ERROR:Unvalid number")
else:
    factorial = 1
    for i in range(1,n + 1):
        factorial *= i
print(f"Factorial of {n} is: {factorial}")

# Multiplication table
num = int(input("Enter number: "))
for i in range(1, 11):
    print(f"{num} x {i} = {num * i}")

# Checking if a number is even or odd
number = int(input("Enter a number: "))
if number%2 == 0:  
    print(f"{number} is even")
else:
    print(f"{number} is odd") 


# Appending four elements to the end of the list
my_list = [1, 2, 3]
my_list.append(4)  
my_list.append(5) 
print(f"My list = {my_list}")

# Comparing different types
value1 = int(input("Enter first value: "))
value2 = int(input("Enter second value: "))
if value1 == value2:
    print("Values are equal")
else:
    print("Values are not equal")



# Count even numbers from Zero to 50
count = 0
while True:
    if count >= 50:
        break
    else:
        count += 2
    print(count) 


# Sum of first n natural numbers
n = int(input("Enter a number: "))
sum_natural = 0
for i in range(n+1):
    sum_natural += i  
print(f"Sum of first {n} natural numbers: {sum_natural}")

# Calculate the average of a list of numbers
numbers = [3, 7, 2, 9, 12]
sum_numbers = 0
for number in numbers:
    sum_numbers += number
average = sum_numbers // len(numbers)  # Runtime error: TypeError
print(f"Median of numbers: {average}")


# Sum of digits of a number
num = int(input("Enter a number: "))
sum_of_digits = 0
while num > 0:
    sum_of_digits += num % 10
    num = num // 10  
print(f"Sum of digits: {sum_of_digits}")

# Check if a number is a perfect square
num = int(input("Enter a number: "))
if num**0.5 * num**0.5 == num :
    print(f"{num} is a perfect square")
else:
    print(f"{num} is not a perfect square")


# Remove duplicates from a list
numbers=[]
print("Enter the list value")
while True:
  x=input()
  if x==" ":
    break
  else:
    numbers.append(int(x))
unique_numbers = []
for number in numbers:
    if number not in unique_numbers:
        unique_numbers.append(number)  # AttributeError: 'list' object has no attribute 'add'
print(f"Unique numbers: {unique_numbers}")

# Swap two variables
a = input("Enter number a: ")
b = input("Enter number b:")
a = b
b = a
print(f"After swapping: a = {a}, b = {b}")
