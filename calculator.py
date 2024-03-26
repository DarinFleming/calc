import tkinter as tk

calculator = tk.Tk()
calculator.title = 'Calculator'

display = tk.Entry(calculator)
display.grid(columnspan=5)


# button functions
def button_click(char):
    current = display.get()
    display.delete(0, tk.END)
    display.insert(0, current + char)

def button_clear():
    display.delete(0, tk.END)

def button_equal():
    #eval logic
    try:
        result = eval(display.get())
        display.delete(0, tk.END)
        display.insert(0, result)
    except:
        display.delete(0, tk.END)
        display.insert(0, "Error")


# Clear display
buttonClear = tk.Button(calculator, text='clear', command=button_clear)
buttonClear.grid(row=1, column=3)

# Equal button
buttonEqual = tk.Button(calculator, text='=', command=button_equal)
buttonEqual.grid(row=2, column=3)


# Math functions
buttonAdd = tk.Button(calculator, text='+', command=lambda: button_click('+'))
buttonAdd.grid(row=3, column=3)

buttonMinus = tk.Button(calculator, text='-', command=lambda: button_click('-'))
buttonMinus.grid(row=4, column=3)

buttonMultiply = tk.Button(calculator, text='*', command=lambda: button_click('*'))
buttonMultiply.grid(row=4, column=2)

buttonDivide = tk.Button(calculator, text='/', command=lambda: button_click('/'))
buttonDivide.grid(row=4, column=1)



# Numbers list
button_0 = tk.Button(calculator, text='0', command=lambda: button_click('0'))
button_0.grid(row=4, column = 0)

button_9 = tk.Button(calculator, text='9', command=lambda: button_click('9'))
button_9.grid(row=3, column = 2)

button_8 = tk.Button(calculator, text='8', command=lambda: button_click('8'))
button_8.grid(row=3, column = 1)

button_7 = tk.Button(calculator, text='7', command=lambda: button_click('7'))
button_7.grid(row=3, column = 0)

button_6 = tk.Button(calculator, text='6', command=lambda: button_click('6'))
button_6.grid(row=2, column = 2)

button_5 = tk.Button(calculator, text='5', command=lambda: button_click('5'))
button_5.grid(row=2, column = 1)

button_4 = tk.Button(calculator, text='4', command=lambda: button_click('4'))
button_4.grid(row=2, column = 0)

button_3 = tk.Button(calculator, text='3', command=lambda: button_click('3'))
button_3.grid(row=1, column = 2)

button_2 = tk.Button(calculator, text='2', command=lambda: button_click('2'))
button_2.grid(row=1, column = 1)

button_1 = tk.Button(calculator, text='1', command=lambda: button_click('1'))
button_1.grid(row=1, column = 0)





calculator.mainloop()
