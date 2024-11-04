# Age Classification

age = input("Enter age: ").strip()
age_as_int = int(age)
classification = ''

if age_as_int < 13:
    classification = 'Adolescent'
elif 13 <= age_as_int <= 18:
    classification = 'Teenager'
elif 19 <= age_as_int <= 49:
    classification = 'Adult'
elif 50 <= age_as_int <= 75:
    classification = 'Senior'
else:
    classification = 'Elder'

print("Your gender class is:", classification)
input()
