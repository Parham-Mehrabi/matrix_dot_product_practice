from tkinter import Tk, OptionMenu, StringVar, Button, Checkbutton, BooleanVar
from colors import BACK_GROUND_COLOR_1
from widgets import BlueLabel
from utils import matrices


def main():
    root = Tk()
    root.title('matrices practice')
    root.geometry("800x620+100+100")
    root.config({"bg": BACK_GROUND_COLOR_1})
    BlueLabel(root, text="select difficulty").pack()
    matrix_1 = StringVar()
    matrix_1.set("select the first matrix")
    matrix_num1 = OptionMenu(root, matrix_1, *matrices)
    matrix_2 = StringVar()
    matrix_2.set("select the second matrix")
    matrix_num2 = OptionMenu(root, matrix_2, *matrices)
    have_zero_var = BooleanVar()
    have_zero_var.set(True)
    btn_have_zero = Checkbutton(root, text="allow zero", variable=have_zero_var)
    have_negative_var = BooleanVar()
    have_negative_var.set(True)
    btn_negative = Checkbutton(root, text="allow negative items", variable=have_negative_var)

    btn_generate = Button(root, text="generate")
    
    matrix_num1.pack(pady=2)
    matrix_num2.pack(pady=2)
    btn_have_zero.pack(pady=2)
    btn_negative.pack(pady=2)
    btn_generate.pack(pady=2)
    root.mainloop()


if __name__ == '__main__':
    main()
