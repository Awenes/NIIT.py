# multiplication table

n = input("Enter Number: ").strip()
a = int(n)

i = 1
while i <= 12:
    z = str(i)+' x '+str(a)+' = '
    print(z, i * a)
    i += 1

input()
