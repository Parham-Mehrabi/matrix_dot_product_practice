from tkinter import Tk, Button, Checkbutton, BooleanVar, LEFT, Frame, messagebox
from colors import BACK_GROUND_COLOR_1
from widgets import BlueLabel, matrices_frame
from utils import validate_shapes



def handle_generate(m1, m2):
    if len(m1) > 5 or len(m2) > 5:
        return messagebox.showerror("select both shapes", "select both matrices shapes")

    if not validate_shapes(m1, m2):
        return messagebox.showerror("Invalide shapes", f"you cannot multiply a matrix with shape {m1} to a matrix with shape {m2}")


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
    _matrices_frame, matrix_1, matrix_2 = matrices_frame(root)

    btn_generate = Button(root, text="generate", command=lambda: handle_generate(m1=matrix_1.get(), m2=matrix_2.get()))

    _matrices_frame.pack(pady=2)
    btn_have_zero.pack(pady=2)
    btn_negative.pack(pady=2)
    btn_generate.pack(pady=2)
    root.mainloop()


if __name__ == '__main__':
    main()
