a = 5 
b = 2

# Arithmetic Operators
print("Arithmetic Operators:")
print("Addition : ",a + b)  # Addition
print("Subtraction : ",a - b)  # Subtraction
print("Multiplication : ",a * b)  # Multiplication
print("Division : ",a / b)  # Division
print("Floor Division : ",a // b)  # Floor Division
print("Modulus : ",a % b)  # Modulus
print("Exponentiation : ",a ** b)  # Exponentiation

# Bitwise Operators
print("\nBitwise Operators:")
print("Bitwise AND : ",a & b)  # Bitwise AND
print("Bitwise OR : ",a | b)  # Bitwise OR
print("Bitwise XOR : ",a ^ b)  # Bitwise XOR
print("Bitwise NOT : ",~a)  # Bitwise NOT --> Not giving the correct answer due to 64 bit os

print(13&10)
print(13|10)
print(13^14)
print(~10)

# Comparison Operators
print("\nComparison Operators:")
print("Equal : ",a == b)  # Equal
print("Not Equal : ",a != b)  # Not Equal
print("Greater than : ",a > b)  # Greater than
print("Less than : ",a < b)  # Less than
print("Greater than or equal to : ",a >= b)  # Greater than or equal to
print("Less than or equal to : ",a <= b)  # Less than or equal

# Assignment Operators
print("\nAssignment Operators:")
a += 5  # Add and assign
print("After += 5, a =", a) 
a -= 3  # Subtract and assign
print("After -= 3, a =", a)
a *= 2  # Multiply and assign
print("After *= 2, a =", a)
a /= 4  # Divide and assign
print("After /= 4, a =", a)
a //= 2  # Floor divide and assign
print("After //= 2, a =", a)
a %= 3  # Modulus and assign
print("After %= 3, a =", a)
a **= 2  # Exponentiate and assign
print("After **= 2, a =", a)
