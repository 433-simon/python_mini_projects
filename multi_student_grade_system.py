students = []      # Empty list for putting different students 
total_marks = 0
max_marks= 400
percentage = 0
while True:
    student_name = input("Enter name of student : ")
    physics_mark = int(input("Enter marks of physics : "))
    chemistry_mark = int(input("Enter marks of chemistry : "))
    maths_mark=  int(input("Enter marks of maths : "))
    physical_education_marks = int(input("Enter marks of physical eduction  : "))

    data = {
    "name" : student_name,
    "physics" : physics_mark,
    "chemistry" : chemistry_mark,
    "maths" : maths_mark,
    "physical_education" : physical_education_marks
    }
    # students.append(data)
    total_marks = (
    data["maths"] +
    data["physics"] +
    data["physical_education"] +
    data["chemistry"] 
    )   
    print(f"total marks of students are : {total_marks}")
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
    students.append(data)
    choice = input("Do you want to add more students : ")

    
    if choice.lower() != "yes" :
        break;
print("\n Students data : ")
print(students)
