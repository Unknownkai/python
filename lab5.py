#IT 3883/Section 01
#Kaito Hamm
#Lab 5

# Function to collect student information
def collect_student_data():
    # Prompting user for student details
    first_name = input("Enter First Name: ")
    last_name = input("Enter Last Name: ")
    student_id = input("Enter Student ID: ")
    gpa = input("Enter GPA: ")

    # Creating a dictionary to hold the student data
    student_data = {
        'First Name': first_name,
        'Last Name': last_name,
        'Student ID': student_id,
        'GPA': gpa
    }

    return student_data

# Function to print student data
def print_student_data(student_data):
    print("\nStudent Information:")
    for key, value in student_data.items():
        print(f"{key}: {value}")

# Main program
if __name__ == "__main__":
    # Collecting data for 3 students
    students = []
    for i in range(3):
        print(f"\n--- Enter details for Student {i + 1} ---")
        student_data = collect_student_data()
        students.append(student_data)

    # Printing the data for all students
    for i, student in enumerate(students):
        print(f"\n--- Student {i + 1} ---")
        print_student_data(student)

    # Removing GPA and printing again
    for i, student in enumerate(students):
        student.pop('GPA')  # Remove GPA
        print(f"\n--- Student {i + 1} (GPA removed) ---")
        print_student_data(student)
