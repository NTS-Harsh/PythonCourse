# Stores the data in key-value pair

empty_dict = {}

person = {
    "name":"Harsh",
    "age": 22,
    "city":"Kolhapur"
}
print(person)
print(person["name"])
person["name"] = "Rohit"
print(person)

# Iterate keys only
for key in person:
    print(key)

# Iterate keys and values
for key,value in person.items():
    print(f"{key} : {value}")

# Iterate through values
for val in person.values():
    print(val)

# Nested dictionary
students = {
    "1001":{"name":"Harsh","age":22},
    "1002":{"name":"Rohit","age":20}
}

print(students["1001"]["name"])
print(students)

for key,val in students.items():
    print(f"ID : {key}")
    print(f"Name: {val["name"]}")
    print(f"Age: {val["age"]}")

print(students[0])