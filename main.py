import tkinter as tk


# Function to perform arithmetic operations
def calculate():
    try:
        num1 = float(entry_num1.get())  # Get the first number from the entry field and convert it to a float
        num2 = float(entry_num2.get())  # Get the second number from the entry field and convert it to a float
        operation = operator.get()  # Get the selected operation from the dropdown menu

        if operation == "Addition":
            result.set(num1 + num2)  # Perform addition and update the result variable
        elif operation == "Subtraction":
            result.set(num1 - num2)  # Perform subtraction and update the result variable
        elif operation == "Multiplication":
            result.set(num1 * num2)  # Perform multiplication and update the result variable
        elif operation == "Division":
            if num2 == 0:
                result.set("Cannot divide by zero")
            else:
                result.set(num1 / num2)  # Perform division and update the result variable
    except ValueError:
        result.set("Invalid input")  # Handle invalid input and display an error message


# Create the main window
root = tk.Tk()
root.title("Calculator")

# Create input fields and labels
label_num1 = tk.Label(root, text="Enter number 1:")
label_num2 = tk.Label(root, text="Enter number 2:")
entry_num1 = tk.Entry(root)  # Entry field for the first number
entry_num2 = tk.Entry(root)  # Entry field for the second number

label_num1.grid(row=0, column=0)  # Place the label for the first number in the grid
entry_num1.grid(row=0, column=1)  # Place the entry field for the first number in the grid
label_num2.grid(row=1, column=0)  # Place the label for the second number in the grid
entry_num2.grid(row=1, column=1)  # Place the entry field for the second number in the grid

# Create a dropdown for selecting the operation
operator = tk.StringVar()
operator.set("Addition")  # Default operation
operator_menu = tk.OptionMenu(root, operator, "Addition", "Subtraction", "Multiplication", "Division")  # Dropdown menu
operator_label = tk.Label(root, text="Select operation:")  # Label for the dropdown
operator_label.grid(row=2, column=0)  # Place the label in the grid
operator_menu.grid(row=2, column=1)  # Place the dropdown menu in the grid

# Create a button to calculate the result
calculate_button = tk.Button(root, text="Calculate", command=calculate)  # Button to trigger the calculation
calculate_button.grid(row=3, column=0, columnspan=2)  # Place the button in the grid

# Display the result
result = tk.StringVar()  # Variable to store the result
result_label = tk.Label(root, text="Result:")  # Label to display "Result:"
result_value = tk.Label(root, textvariable=result)  # Label to display the calculated result
result_label.grid(row=4, column=0)  # Place the "Result:" label in the grid
result_value.grid(row=4, column=1)  # Place the result value label in the grid

# Run the GUI application
root.mainloop()
