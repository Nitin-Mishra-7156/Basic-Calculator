import tkinter as tk
from tkinter import messagebox
import math

def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    if b == 0:
        return "Number cannot be divided by zero"
    else:
        return a / b

def power(a, b):
    return a ** b

def update_entry_label():
    user_input = operation_var.get()
    if user_input == 'pow':
        num1_label.config(text="Enter the Number:")
        num2_label.config(text="Enter the Exponent(Power) number:")
        entry_num2.config(state='normal')
    elif user_input == 'sqrt':
        num2_label.config(text="Enter Second Number:")
        entry_num2.delete(0, tk.END)
        entry_num2.config(state='disabled')
    else:
        num2_label.config(text="Enter Second Number:")
        entry_num2.config(state='normal')

def calculate():
    user_input = operation_var.get()

    if user_input == "quit":
        root.destroy()
    elif user_input in ['add', 'sub', 'mul', 'div', 'pow', 'sqrt']:
        try:
            num1 = float(entry_num1.get())

            # Powering the Number
            if user_input == 'pow':
                pow_val = float(entry_num2.get())
                result = power(num1, pow_val)
                result_label.config(text=f"Result: {result}")
                return

            # Square-root of a number
            if user_input == 'sqrt':
                result = math.sqrt(num1)
                result_label.config(text=f"Result: {result}")
                return

            num2 = float(entry_num2.get())

            # Add, Sub, Mul, Div of a number
            if user_input == 'add':
                result = add(num1, num2)
            elif user_input == 'sub':
                result = sub(num1, num2)
            elif user_input == 'mul':
                result = mul(num1, num2)
            elif user_input == 'div':
                result = div(num1, num2)

            result_label.config(text=f"Result: {result}")

        except ValueError:
            messagebox.showerror("Error", "Please enter valid numbers.")
    else:
        messagebox.showerror("Error", "Enter a valid operation.")

# Create the main window
root = tk.Tk()
root.title("Calculator")

# Set window size to full screen
# root.geometry("{0}x{1}+0+0".format(root.winfo_screenwidth(), root.winfo_screenheight()))
# Set the initial size of the window
root.geometry("400x300")

# GUI components
operation_var = tk.StringVar()
operation_var.set("add")

operation_label = tk.Label(root, text="Select Operation:")
operation_label.pack()

operation_menu = tk.OptionMenu(root, operation_var, 'add', 'sub', 'mul', 'div', 'pow', 'sqrt')
operation_menu.pack()

num1_label = tk.Label(root, text="Enter First Number:")
num1_label.pack()

entry_num1 = tk.Entry(root)
entry_num1.pack()

num2_label = tk.Label(root, text="Enter Second Number:")
num2_label.pack()

entry_num2 = tk.Entry(root)
entry_num2.pack()

calculate_button = tk.Button(root, text="Calculate", command=calculate)
calculate_button.pack()

result_label = tk.Label(root, text="Result:")
result_label.pack()

# Set up trace on the operation_var to update entry labels
operation_var.trace_add('write', lambda *args: update_entry_label())

# Start the GUI application
root.mainloop()
