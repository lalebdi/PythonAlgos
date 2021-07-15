user = {"firstname": "Jane", "lastname": "Doe", "age": 33, "email": "jdoe@example.com", "city": "NYC"}

print(user)
print(user["age"])

# Changing a value
user["age"] = 25
print(user)

# Adding a value
user["address"] = "Times Square"
print(user)

# Deleting an element
user.pop("age")
print(user)

# user.clear()
# print(user)

print(user.keys())
print(user.values())
print(user.items())

print(user.get("email"))