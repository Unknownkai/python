#IT 3883/Section 01
#Kaito Hamm
#Lab 3
#six students test scores, calculates their average, assigns letter grades for each test and the overall average

#variable for student name
student_name = ""

#Function to calculate average score
def calculate_average(scores):
    return sum(scores) / len(scores)

#Function to determine the letter grade based on a score
def get_letter_grade(score):
    if 90 <= score <= 100:
        return 'A'
    elif 80 <= score < 90:
        return 'B'
    elif 70 <= score < 80:
        return 'C'
    elif 60 <= score < 70:
        return 'D'
    else:
        return 'F'

#Function to handle a single student's data
def process_student(name, scores):
    global student_name
    student_name = name
    print(f"\nStudent: {student_name}")
    
    #Display each score with corresponding letter grade
    for i, score in enumerate(scores, 1):
        grade = get_letter_grade(score)
        print(f"Test {i}: {score} - Grade: {grade}")
    
    #Calculate and display average score
    average = calculate_average(scores)
    average_grade = get_letter_grade(average)
    print(f"Average Score: {average:.2f} - Grade: {average_grade}")

#Main program
def main():
    for _ in range(6):  # Assume 6 students
        name = input("\nEnter student's name: ")
        scores = []
        for i in range(1, 7):
            score = float(input(f"Enter score for test {i}: "))
            scores.append(score)
        process_student(name, scores)

#Run the main program
if __name__ == "__main__":
    main()
