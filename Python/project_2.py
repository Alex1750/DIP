mark = int(input("Enter your marks: "))
attendance = int(input("Enter your attendance rate: "))

if mark > 60:
    print("Student Passed")
    if attendance == 100:
        print("\"Full Attendance Certificate\" Obtained!")
    elif attendance >= 90:
        print("Excellent Attendance!")
    elif attendance >= 80:
        print("Good Attendance!")
    elif attendance >= 70:
        print("Attendance is ok.")
    elif attendance < 70:
        print("Attendance needs improvement.")
    else:
        print("Do i look dumb to you?")
elif mark < 60:
    print("Student did not pass exam. \nFurther improvement needed RN.")
else:
    print("I am not that dumb ok?")