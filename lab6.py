#IT 3883/Section 01
#Kaito Hamm
#Lab 6

import tkinter as tk

# Function to check the age and display the message
def check_age():
    age = int(age_entry.get())
    if age > 65:
        result_label.config(text="Senior Citizen")
    elif age > 18:
        result_label.config(text="Old Enough to Vote")
    else:
        result_label.config(text="Not Old Enough to Vote")

# Create the main window
root = tk.Tk()
root.title("Age Checker")

# Add an input label and entry box
tk.Label(root, text="Enter your age:").pack()
age_entry = tk.Entry(root)
age_entry.pack()

# Add a button to check the age
check_button = tk.Button(root, text="Check", command=check_age)
check_button.pack()

# Add a label to display the result
result_label = tk.Label(root, text="")
result_label.pack()

# Run the application
root.mainloop()
