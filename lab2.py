#IT 3883/Section 01
#Kaito Hamm
#Lab 2 
#Determine and display an employee's salary raise and new salary based on their performance ranking.

# ask the user for the employee's ranking and current salary
ranking = float(input("Enter the employee's annual performance ranking (0 to 5): "))
current_salary = float(input("Enter the employee's current annual salary: "))

if ranking < 0 or ranking > 5:
    print("Ranking must be between 0 and 5. Please try again.")
else:
    # Determine the pay raise percentage based on the ranking
    if ranking == 1:
        raise_percentage = 1.25
    elif ranking == 2:
        raise_percentage = 2.00
    elif ranking == 3:
        raise_percentage = 2.5
    elif ranking == 4:
        raise_percentage = 3.25
    elif ranking == 5:
        raise_percentage = 3.5
    else:  # Ranking is 0
        raise_percentage = 0.0

    # Calculate the raise amount and the new salary
    raise_amount = (raise_percentage / 100) * current_salary
    new_salary = current_salary + raise_amount

    # Output the raise percentage, raise amount, and new salary
    print(f"Employee Ranking: {ranking}")
    print(f"Raise Percentage: {raise_percentage}%")
    print(f"Raise Amount: ${raise_amount:.2f}")
    print(f"New Annual Salary: ${new_salary:.2f}")
