import tkinter as tk

def on_button_click(operator):
    num1 = float(entry_num1.get())
    num2 = float(entry_num2.get())

    if operator == '+':
        result = num1 + num2
    elif operator == '-':
        result = num1 - num2
    elif operator == '*':
        result = num1 * num2
    elif operator == '/':
        if num2 != 0:
            result = num1 / num2
        else:
            result = "Error: Division by zero"

    label_result.config(text="Result: " + str(result))


root = tk.Tk()
root.title("Calculater")


label_num1 = tk.Label(root, text="number 1: ")
label_num1.pack()

entry_num1 = tk.Entry(root)
entry_num1.pack()

label_num2 = tk.Label(root, text="number 2: ")
label_num2.pack()

entry_num2 = tk.Entry(root)
entry_num2.pack()

button_add = tk.Button(root, text="Increase", command=lambda: on_button_click('+'))
button_subtract = tk.Button(root, text="Decrease", command=lambda: on_button_click('-'))
button_multiply = tk.Button(root, text="multiplication", command=lambda: on_button_click('*'))
button_divide = tk.Button(root, text="Division", command=lambda: on_button_click('/'))

button_add.pack()
button_subtract.pack()
button_multiply.pack()
button_divide.pack()

label_result = tk.Label(root, text="")
label_result.pack()

root.mainloop()
