# Read entire file
file = open("data.txt","r") # Openening the file in read mode
data = file.read()
print(data)
file.close()

# Read first 5 characters
file = open("data.txt", "r")
print(file.read(5))
file.close()

print()
# Read line by line
file = open("data.txt", "r")
print(file.readline())  # First line
print(file.readline())  # Second line
file.close()

# Read all lines into a list
file = open("data.txt", "r")
lines = file.readlines()
print(lines)
file.close()


print("\nWriting to the file")
# Overwrite file
f = open("data1.txt", "w")  # If file is not present then write mode create the file and write into it
f.write("Hello, Harsh!\n")
f.write("Learning file handling.\n")
f.close()

# Append to file
f = open("data1.txt", "a")
f.write("Adding more text at the end.\n")  # Adding data at the last
print("Appended more text into the file")
f.close()


# Using with automatically closes the file after use.
print("\nReading the file using with\n")
with open("data.txt", "r") as f:
    content = f.read()
    print(content)

print("\nAppending the data using with")
with open("data.txt", "a") as f:
    f.write("Line added using 'with'.\n")


# Checking the file is empty or not
print("\nChecking the file is empty or not\n")
with open("data.txt","r") as file:
    content = file.read()

if not content:
    print("File is empty")
else:
    print("File has the content")
