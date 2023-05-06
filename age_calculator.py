import tkinter as tk
import datetime

# Define a function to calculate the age
def calculate_age():
    birth_year = int(entry.get())
    current_year = datetime.date.today().year
    age = current_year - birth_year
    result_label.config(text="Your age is: " + str(age))

# Create the main window
root = tk.Tk()
root.title("Age Calculator")

# Create a label for the birth year input
input_label = tk.Label(root, text="Enter your birth year:", font=("Helvetica", 18, "bold"), fg="blue", padx=20, pady=20)
input_label.pack()

# Create an entry field for the birth year input
entry = tk.Entry(root, font=("Helvetica", 18, "bold"), fg="blue", justify="center")
entry.pack()

# Create a button to calculate the age
calculate_button = tk.Button(root, text="Calculate", command=calculate_age)
calculate_button.pack()

# Create a label to display the age calculation result
result_label = tk.Label(root, text="", font=("Helvetica", 18, "bold") , fg="green", padx=20, pady=20)
result_label.pack()

# Run the main loop to start the GUI
root.mainloop()
