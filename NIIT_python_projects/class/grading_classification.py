# Grading Classification

score = input("Enter grade: ").strip()
grade = int(score)
classification = ''

if grade < 20:
    classification = 'F'
elif 20 <= grade < 40:
    classification = 'D'
elif 40 <= grade < 60:
    classification = 'C'
elif 60 <= grade < 80:
    classification = 'B'
else:
    classification = 'A'

print("Your score class is:", classification)
input()
