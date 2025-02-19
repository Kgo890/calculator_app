import tkinter as tk


# called when a number or operator has been called
def on_button_click(value):
    current_text = entry.get()
    entry.delete(0, tk.END)
    entry.insert(tk.END, current_text + value)


# clears the all the numbers
def clear_entry():
    entry.delete(0, tk.END)


def calculate():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")


# Create the main window
window = tk.Tk()
window.title("Calculator")

# Entry widget for displaying the input and result
entry = tk.Entry(window, width=20, font=('Arial', 16), bd=5, insertwidth=4)
entry.grid(row=0, column=0, columnspan=4)

# Buttons
buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', '.', '=', '+'
]

row_val = 1
col_val = 0

for button in buttons:
    tk.Button(window, text=button, width=5, height=2, command=lambda b=button: on_button_click(b)).grid(row=row_val,
                                                                                                        column=col_val)
    col_val += 1
    if col_val > 3:
        col_val = 0
        row_val += 1

# Clear button
tk.Button(window, text='Clear', width=5, height=2, command=clear_entry).grid(row=row_val, column=col_val)

# Calculate button
tk.Button(window, text='Result', width=5, height=2, command=calculate).grid(row=row_val, column=col_val + 1)

# Run the main loop
window.mainloop()
