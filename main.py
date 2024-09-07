import math

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

def circle_area(radius):
    return math.pi * radius ** 2

def average(numbers):
    return sum(numbers) / len(numbers) if numbers else 0




