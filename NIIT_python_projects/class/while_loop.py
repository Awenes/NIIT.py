i = 0
n = input("Enter Number: ").strip()
a = int(n)
while i <= 12:
    if i % a == 0:
        print(i)
    i += 1

input()
