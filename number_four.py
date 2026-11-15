#a) sum of the first N natural numbers
def sum_n(n):
    if n == 0:
        return 0
    return n + sum_n(n - 1)

n = 5
print("Sum =", sum_n(n))

#b) factorial of a number
def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

print(factorial(5))

#c) Fibonacci series
def fibonacci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)

print(fibonacci(6))

#d) N terms of a Fibonacci series
def fibonacci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)

n = 7

for i in range(n):
    print(fibonacci(i), end=" ")


