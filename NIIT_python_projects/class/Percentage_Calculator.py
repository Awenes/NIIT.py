# Percentage Calculator


def perc(amount, percent):

    res = (percent/100) * amount
    return "{:,.2f}".format(res)

income = input("Enter amount: ").strip()
amount = float(income)

percentage = input("Enter percentage: ").strip()
percent = float(percentage)

    
print("The Percentage Value is: ", perc(amount, percent))
input()
