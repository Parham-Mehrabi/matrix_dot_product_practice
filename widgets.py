""" my costume widgets """
from tkinter import Label, Frame, StringVar, OptionMenu, LEFT, Tk
from colors import BACK_GROUND_COLOR_1, CYAN_1, BLACK, RED
import numpy as np


class BlueLabel(Label):
    def __init__(self, master, **kwargs):
        kwargs.setdefault("bg", BACK_GROUND_COLOR_1)
        kwargs.setdefault("fg", CYAN_1)
        kwargs.setdefault("font", ("MonoSpace", 18, 'bold'))
        super().__init__(master, **kwargs)


class XSign(Label):
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
    x_sign = XSign(_matrices_frame, fg=RED)
    matrix_2 = StringVar()
    matrix_2.set("select the second matrix")
    matrix_num2 = OptionMenu(_matrices_frame, matrix_2, *matrices)
    matrix_num1.pack(side=LEFT)
    x_sign.pack(side=LEFT)
    matrix_num2.pack(side=LEFT)
    return _matrices_frame, matrix_1, matrix_2

class EqualSign(Label):
    def __init__(self, master, **kwargs):
        kwargs.setdefault("bg", BACK_GROUND_COLOR_1)
        kwargs.setdefault("text", "=")
        kwargs.setdefault("fg", BLACK)
        kwargs.setdefault("font", ("Aryal", 25, 'bold'))
        super().__init__(master, **kwargs)

class MatrixFrame(Frame):
    def __init__(self, master, matrix:np.ndarray):
        super().__init__(master)
        self.matrix = matrix
        self.create_widgets()

    def create_widgets(self):
        row, col = self.matrix.shape
        for i in range(row):
            for j in range(col):
                Label(self, text=str(self.matrix[i, j]),
                    borderwidth=1,
                    relief="solid",
                    font=("Aryal", 22, "bold")
                    ).grid(row=i, column=j, padx=2, pady=2, sticky='ew')
                

class AnswerFrame(Frame):
    def __init__(self, master, answer:np.ndarray):
        super().__init__(master)
        self.answer = answer
        self.create_widgets()

    def create_widgets(self):
        row, col = self.answer.shape
        for i in range(row):
            for j in range(col):
                label = Label(self, text="?", borderwidth=1, relief="solid", font=("Arial", 22, "bold"))
                label.grid(row=i, column=j, padx=2, pady=2, sticky='ew')
                label.bind("<Button-1>", lambda event, row=i, col=j: event.widget.config(text=self.answer[row, col]))
class Shape:
    def __init__(self, row, col) -> None:
        self.row = row
        self.col = col
    
    def __str__(self) -> str:
        return f"{self.row} x {self.col}"
    
    def __repr__(self) -> str:
        return f"{self.row} x {self.col}"
    
    def to_tuple(self) -> tuple:
        return self.row, self.col

    @staticmethod
    def from_str(str_shape:str):
        try:
            row, col = [int(i.strip()) for i in str_shape.split("x")]
        except:
            raise ValueError("the input should be in format of 'row x col'")
        return Shape(row, col)
    

matrices = [Shape(j, i) for j in range(1, 6) for i in range(1, 6)]