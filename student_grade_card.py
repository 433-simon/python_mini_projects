print("Welcome to Student Grade Card Manager!")
total_marks = 0
max_marks= 400
percentage = 0
student_dict = {
"student_name" : input("Enter the name of the student : ") ,
"physics_mark" : int(input("Enter marks of physics : ")),
"chemistry_mark" : int(input("Enter marks of chemistry : ")),
"maths_mark" : int(input("Enter marks of maths : ")),
"physical_education_marks" : int(input("Enter marks of physical eduction  : "))
}
print(f"Name of Student is : {student_dict["student_name"]}")
print(f" Your marks of maths are {student_dict["maths_mark"]}")
print(f" Your marks of chemistry are {student_dict["chemistry_mark"]}")
print(f" Your marks of physics are {student_dict["physics_mark"]}")
print(f" Your marks of physical_eduction are {student_dict["physical_education_marks"]}")
print(student_dict)
total_marks = (
    student_dict["maths_mark"] +
    student_dict["physics_mark"] +
    student_dict["chemistry_mark"] +
    student_dict["physical_education_marks"]
)
print(f"Your total marks are {total_marks}")
percentage = (total_marks/max_marks)*100
final_percentage=int(percentage)
print(f"Your final percentage is {final_percentage}%")

if final_percentage >= 90:
    print(" You got A grade")
elif final_percentage >= 80 and final_percentage < 90 :
    print(" You got B grade")
elif final_percentage >= 70 and final_percentage < 80 :
    print(" You got C grade")
elif final_percentage >= 60 and final_percentage < 70:
    print("You got D grade")
else :
    print("You are fail")