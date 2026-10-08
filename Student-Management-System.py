print("     Good Morning Dear Friend ")
print("             Welcome To")
print("-----STUDENT MANAGEMENT SYSTEM-----")
print()
print("=======Menu=======")
print()
print()


students=[]
while True:

    print("1. Add Student\n"
    "2. View Student\n"
"3. Search Student\n"
"4. Average Marks\n"
"5. Find Topper\n"
"6. Delete Student\n"
"7. Total number of Students"
"8. Exit")
    print()
    a=int(input("Enter Your Choice: "))
    if a==1:
        name=input("Enter Student Name: ")
        age=int(input("Enter Student Age: "))
        marks=int(input("Enter Students Marks: "))
        students.append([name,age,marks])
    

    elif a==2:
        b=1
        for student in students:
            print()
            print("--------------------------------------")
            print()
            print(f"Student {b}")
            print(f"Name: {student[0]}")
            print(f"Age: {student[1]}")
            print(f"Marks: {student[2]}")
            print()
            b+=1

    elif a==3:
        search=input("Enter Student Name : ")
        print()
        found = False
        for student in students:

            
            if student[0]==search :
                found=True
                print("Student Name Found Successfully...")
                print()
                print(f"Name: {student[0]}")
                print(f"Age: {student[1]}")
                print(f"Marks: {student[2]}")
        if found == False:
                print("Student Name Not Found...")
                print()
    elif a==4:
        if len(students)==0:
            print("No Student Found")
        else: 
            total=0
            for student in students:
            
               total = total + student[2]
        
            average = total/len(students)
            print(f"Average makrs is {average}")


    elif a==5:
        if len(students)==0:
            print("No Student Available...")
        else: 
            marks=[]
            for student in students:
                marks.append(student[2])
        
            high=max(marks)

            for student in students:
                if student[2] == high:
                    print(f"Name of the Student: {student[0]}")
                    print(f"Highest Marks are: {high}")

    elif a==6:
        delete=input("Enter Student name which neede to be deleted: ")
        
        for student in students:
            if student[0]==delete:
                students.remove(student)

    elif a==7:
        print(f"Total numbers of students are {len(students)}")    

    elif a==8:
        break

    else :
        print("You are entering Non-Answerable Value ")
        print("Please enter for 1 to 7")