""" my costume widgets """
from tkinter import Label
from colors import BACK_GROUND_COLOR_1, CYAN_1


class BlueLabel(Label):
    def __init__(self, master, **kwargs):
        kwargs.setdefault("bg", BACK_GROUND_COLOR_1)
        kwargs.setdefault("fg", CYAN_1)
        kwargs.setdefault("font", ("MonoSpace", 18, 'bold'))
        super().__init__(master, **kwargs)