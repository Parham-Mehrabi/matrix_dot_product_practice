""" my costume widgets """
from tkinter import Label
from colors import BACK_GROUND_COLOR_1


class BlueLabel(Label):
    def __init__(self, master, **kwargs):
        kwargs.setdefault("bg", BACK_GROUND_COLOR_1)
        super().__init__(master, **kwargs)