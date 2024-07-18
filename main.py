from tkinter import Tk, OptionMenu, StringVar, Button, Checkbutton, BooleanVar, LEFT, Frame
from colors import BACK_GROUND_COLOR_1
from widgets import BlueLabel, matrices_frame
from utils import matrices




def main():
    root = Tk()
    root.title('matrices practice')
    root.geometry("800x620+100+100")
    root.config({"bg": BACK_GROUND_COLOR_1})
    BlueLabel(root, text="select difficulty").pack()
    have_zero_var = BooleanVar()
    have_zero_var.set(True)
    btn_have_zero = Checkbutton(root, text="allow zero", variable=have_zero_var)
    have_negative_var = BooleanVar()
    have_negative_var.set(True)
    btn_negative = Checkbutton(root, text="allow negative items", variable=have_negative_var)
    btn_generate = Button(root, text="generate")

    _matrices_frame = matrices_frame(root)
    
    _matrices_frame.pack(pady=2)
    btn_have_zero.pack(pady=2)
    btn_negative.pack(pady=2)
    btn_generate.pack(pady=2)
    root.mainloop()


if __name__ == '__main__':
    main()
