#IT 3883/Section 01
#Kaito Hamm
#Lab 4
#six students test scores, calculates their average, assigns letter grades for each test and the overall average

def save_student_data():
    with open('students.txt', 'w') as file:
        file.write("First Name,Last Name,Student ID,GPA\n")  # Adding headers
        for i in range(8):
            print(f"Enter details for Student {i + 1}:")
            first_name = input("First Name: ")
            last_name = input("Last Name: ")
            student_id = input("Student ID: ")
            gpa = float(input("GPA: "))
            
            # Save the record to the file
            file.write(f"{first_name},{last_name},{student_id},{gpa}\n")

# Run the program
save_student_data()
