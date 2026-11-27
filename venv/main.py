import tkinter as tk

reset_display = False


def click(event):
    global reset_display

    current = entry.get()
    button_text = event.widget["text"]

    # Reset the calculator to 0.
    if button_text == 'c':
        entry.delete(0, tk.END)
        entry.insert(tk.END, '0')
        reset_display = False

    elif button_text == '=':
        try:
            # Convert % to division by 100 before calculating.
            expression = current.replace('%', '/100')
            result = eval(expression)  # Calculate the answer.
            entry.delete(0, tk.END)
            entry.insert(tk.END, str(result))
            # Start a new calculation when the next button is pressed.
            reset_display = True

        except Exception:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Error")
            reset_display = True

    else:
        # Clear the old answer or error before entering a new calculation.
        if reset_display:
            entry.delete(0, tk.END)
            current = ''
            reset_display = False

        if current == '0':
            current = ''

        # Replace the last operator if another operator is pressed.
        operators = "+-*/%"
        if current and current[-1] in operators and button_text in operators:
            current = current[:-1]

        # An expression cannot start with *, /, or %.
        if current == '' and button_text in "*/%":
            return

        # Show the updated calculation.
        entry.delete(0, tk.END)
        entry.insert(tk.END, current + button_text)


# Create the calculator window.
root = tk.Tk()  # Main window
root.title("Simple Calculator")
root.geometry("300x400")  # Width x height
root.resizable(False, False)  # Keep the window a fixed size.
root.configure(bg="#f0f0f0")  # Set the window background color.

# Add the display where calculations and answers appear.
entry = tk.Entry(root, bd=5, font=('Times New Roman', 20), justify='right', width=16, bg="#b9f1eb")
entry.pack(pady=5)

# Group the buttons in a frame.
btnFrame = tk.Frame(root)
btnFrame.pack(padx=10,pady=10)

# Arrange the button labels in rows.
buttons = [['c', '(', ')', '/'],
           ['7', '8', '9', '*'],
           ['4', '5', '6', '-'],
           ['1', '2', '3', '+'],
           ['.', '0', '%', '=']]
# Create each button and place it in the grid.
for i in range(len(buttons)):
    for j in range(len(buttons[i])):
        btn = tk.Button(btnFrame, text=buttons[i][j], font=('Times New Roman', 16), width=3, height=1)
        btn.grid(row=i, column=j, padx=10, pady=10)
        btn.bind("<Button-1>",click)  # Run click() when the button is pressed.

root.mainloop()  # Keep the calculator open and responsive.