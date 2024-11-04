list_of_ns = ["FS","PA","CA","OJ","IF","OJ"]
size_of_list = len(list_of_ns)
for name in list_of_ns:
    if name == "IF" or name == "OJ":
        print(name,"Also came late")
    else:
        print(name)
print(size_of_list)

input()