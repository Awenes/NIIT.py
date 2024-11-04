# Registration Form

name = input("Enter full name: ").strip().title()

sex = input("Enter gender: ").strip()

email = input("Enter Email: ").strip().lower()

password = input("Enter password: ").strip()

form = {

    "p1": name,

    "p2":  sex,

    "p3":  email,

    "p4":  password

}


def viewData(dictionary):

    print("Profile Details")

    for property in dictionary:

        print("_____", dictionary[property])


print("(i) Registration Successful")
viewData(form)
input()
