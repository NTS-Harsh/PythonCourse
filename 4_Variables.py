# Variable names

# 1. Camel Case
myVariableName = "Camel Case"

# 2. Pascal Case
MyVariableName = "Pascal Case"

# 3. Snake case
my_variable_name = "Snake case"

# many values to multiple variables
a,b,c = 10, 20, 30
print(a, b, c)

# one value to multiple variables
x = y = z = 100
print(x, y, z)

# unpacking a collection
my_list = [1, 2, 3]
a, b, c = my_list
print(a, b, c)

# Global and Local Variables
z = 10
def my_function():
    global x
    x = 50  # Global variable
    y = 25  # Local variable
    print("Inside function:", x, y)

print("Outside function:", y) 
y = 15 
print(y)  
my_function()
print("Outside function:", x)
