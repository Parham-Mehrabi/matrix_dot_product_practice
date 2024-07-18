""" my costume widgets """
from tkinter import Label, Frame, StringVar, OptionMenu, LEFT, Tk
from utils import matrices
from colors import BACK_GROUND_COLOR_1, CYAN_1, BLACK, RED


class BlueLabel(Label):
    def __init__(self, master, **kwargs):
        kwargs.setdefault("bg", BACK_GROUND_COLOR_1)
        kwargs.setdefault("fg", CYAN_1)
        kwargs.setdefault("font", ("MonoSpace", 18, 'bold'))
        super().__init__(master, **kwargs)

class XSgin(Label):
    def __init__(self, master, **kwargs):
        kwargs.setdefault("bg", BACK_GROUND_COLOR_1)
        kwargs.setdefault("text", "X")
        kwargs.setdefault("fg", BLACK)
        kwargs.setdefault("font", ("Aryal", 25, 'bold'))
        super().__init__(master, **kwargs)



def matrices_frame(master:Tk) -> Frame:
    _matrices_frame = Frame(master)
    matrix_1 = StringVar()
    matrix_1.set("select the first matrix")
    matrix_num1 = OptionMenu(_matrices_frame, matrix_1, *matrices)
    x_sign = XSgin(_matrices_frame, fg=RED)
    matrix_2 = StringVar()
    matrix_2.set("select the second matrix")
    matrix_num2 = OptionMenu(_matrices_frame, matrix_2, *matrices)
    matrix_num1.pack(side=LEFT)
    x_sign.pack(side=LEFT)
    matrix_num2.pack(side=LEFT)
    return _matrices_frame, matrix_1, matrix_2
