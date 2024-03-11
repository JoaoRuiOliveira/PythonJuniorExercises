# Write a function that returns the greatest common divisor of two numbers.
def greatest_common_divisor(a, b):
    # Euclidean Algorithm
    while b != 0: a, b = b, a % b
    return a

# Test Cases
print(greatest_common_divisor(10, 5)) # 5
print(greatest_common_divisor(14, 28)) # 14
print(greatest_common_divisor(1000, 9232)) # 8 