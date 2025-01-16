#IT 3883/Section 01
#Kaito Hamm
#Lab 4
#six students test scores, calculates their average, assigns letter grades for each test and the overall average

def analyze_student_data():
    with open('students.txt', 'r') as infile:
        with open('student_status.txt', 'w') as outfile:
            outfile.write("First Name,Last Name,Student ID,GPA,Academic Status\n")  # Writing headers
            
            next(infile)  # Skip the header line in the input file
            for line in infile:
                # Split the line into respective fields
                first_name, last_name, student_id, gpa = line.strip().split(',')
                gpa = float(gpa)  # Convert GPA to a float
                
                # Determine academic status
                if gpa >= 3.5:
                    status = "Dean's List"
                elif gpa < 2.0:
                    status = "Probation"
                else:
                    status = "Regular Standing"
                
                # Write to the output file
                outfile.write(f"{first_name},{last_name},{student_id},{gpa},{status}\n")

# Run the program
analyze_student_data()
