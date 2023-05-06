import tkinter as tk

# Define a function to perform addition
def add(num1, num2):
    return num1 + num2


# Define a function to perform subtraction
def subtract(num1, num2):
    return num1 - num2


# Define a function to perform multiplication
def multiply(num1, num2):
    return num1 * num2


# Define a function to perform division
def divide(num1, num2):
    return num1 / num2


# Define a function to handle button clicks
def button_click(number):
    current = entry_box.get()
    entry_box.delete(0, tk.END)
    entry_box.insert(0, str(current) + str(number))


# Define a function to handle operation buttons
def button_operation(operation):
    global num1
    global operator
    num1 = float(entry_box.get())
    operator = operation
    entry_box.delete(0, tk.END)


# Define a function to handle the equals button
def button_equals():
    global result
    num2 = float(entry_box.get())
    entry_box.delete(0, tk.END)
    if operator == '+':
        result = add(num1, num2)
    elif operator == '-':
        result = subtract(num1, num2)
    elif operator == '*':
        result = multiply(num1, num2)
    elif operator == '/':
        result = divide(num1, num2)
    entry_box.insert(0, result)


# Define a function to handle the clear button
def button_clear():
    entry_box.delete(0, tk.END)


# Create a new window and set its properties
window = tk.Tk()
window.title("Calculator")
window.geometry("300x200")

# Create an entry box for displaying input and output
entry_box = tk.Entry(window, width=30)
entry_box.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Create buttons for the numbers
button_1 = tk.Button(window, text="1", padx=10, pady=5, command=lambda: button_click(1))
button_2 = tk.Button(window, text="2", padx=10, pady=5, command=lambda: button_click(2))
button_3 = tk.Button(window, text="3", padx=10, pady=5, command=lambda: button_click(3))
button_4 = tk.Button(window, text="4", padx=10, pady=5, command=lambda: button_click(4))
button_5 = tk.Button(window, text="5", padx=10, pady=5, command=lambda: button_click(5))
button_6 = tk.Button(window, text="6", padx=10, pady=5, command=lambda: button_click(6))
button_7 = tk.Button(window, text="7", padx=10, pady=5, command=lambda: button_click(7))
button_8 = tk.Button(window, text="8", padx=10, pady=5, command=lambda: button_click(8))
button_9 = tk.Button(window, text="9", padx=10, pady=5, command=lambda: button_click(9))
button_0 = tk.Button(window, text="0", padx=10, pady=5, command=lambda: button_click(0))

# Create buttons for the operations
button_add = tk.Button(window, text="+", padx=10, pady=5, command=lambda: button_operation('+'))
button_subtract = tk.Button(window, text="-", padx=10, pady=5, command=lambda: button_operation('-'))
button_multiply = tk.Button(window, text="*", padx=10, pady=5, command=lambda: button_operation('*'))
button_divide = tk.Button(window, text="/", padx=10, pady=5, command=lambda: button_operation('/'))
button_equals = tk.Button(window, text="=", padx=10, pady=5, command=button_equals)
button_clear = tk.Button(window, text="C", padx=10, pady=5, command=button_clear)

# Place the buttons on the window
button_1.grid(row=1, column=0)
button_2.grid(row=1, column=1)
button_3.grid(row=1, column=2)
button_add.grid(row=1, column=3)

button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)
button_subtract.grid(row=2, column=3)

button_7.grid(row=3, column=0)
button_8.grid(row=3, column=1)
button_9.grid(row=3, column=2)
button_multiply.grid(row=3, column=3)

button_0.grid(row=4, column=0)
button_clear.grid(row=4, column=1)
button_equals.grid(row=4, column=2)
button_divide.grid(row=4, column=3)

# Start the window
window.mainloop()
