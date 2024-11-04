scores = [6, 7, 22, 10, 20, 12, 14, 55, 56, 50, 57, 5.1]
size = len(scores)
En = sum(scores)
avg = En/size

print("Sum of series:", En)
print("Number of scores:", size)
print(avg)

for result in scores:
    if result >= avg:
        print(result)

for result in scores:
    if result >= 50:
        print(result, "Pass")

    else:
        print(result, "Fail")
