# Gender Classification

gender = input("Enter gender here: ").strip()
title = ''

if gender == 'm' or gender == 'male':
    title = 'Sir'
elif gender == 'f' or gender == 'female':
    title = 'Madam'
else:
    title = 'Sir/Madam'

print("Dear ", title)
input()
