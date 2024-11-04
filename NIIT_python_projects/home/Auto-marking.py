results = [98, 70, 69, 50, 20, 70]
for score in results:
    if score >= 70:
        print(score, "A")

    if score in range(60, 70):
        print(score, "B")

    if score in range(50, 60):
        print(score, "C")

    if score in range(40, 50):
        print(score, "D")

    if score in range(30, 40):
        print(score, "E")

    if score <= 29:
        print(score, "F")

input()
