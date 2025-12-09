# Home Work from GPT!
# Challenge leavel : Medium
#topic: if/else, - Grade calculator

student_name = input("enter student name: ")
marks_math = float(input("enter your math marks: "))
marks_science = float(input("enter your science marks: "))
marks_english = float(input("enter your english marks: "))
mark_hindi = float(input("enter your hindi marks: "))
mark_sst = float(input("enter your sst marks: "))
total_marks = marks_math + marks_science + marks_english + mark_hindi + mark_sst
percentage = (total_marks/500) * 100

if percentage >= 90-100:
    grade = "A"
elif percentage >= 80-89:
    grade = "B"
elif percentage >= 70-79:
    grade = "C"
elif percentage >= 60-69:
    grade = "D"
else:
    grade = "F"

print (f" Hello {student_name}!")
print (f" your total marks are: {total_marks}")
print (f" your percentage is: {percentage:.2f}%")
print (f" your grade is: {grade}")
