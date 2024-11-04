bio = {"name": "John", "sex": 'M', "email": "john@email.com", "phone": "08055972", "address": "USA"}
for key in bio.keys():
    print(key)

for value in bio.values():
    print(value)

for (key, value) in bio.items():
    print(key, "is", value)

for (key, value) in bio.items():
    if key == "name" or key == "phone":
        print(bio[key])

    if key == "name" or key == "phone":
        print(value)

    if bio[key] == "USA":
        print(key)

    if bio[key] == "USA":
        print(bio[key])


fees = [150, 120, 150, 230]
size = len(fees)
print(fees[size-1])
