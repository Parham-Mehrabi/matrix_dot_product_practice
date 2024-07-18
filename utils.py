from typing import Tuple
from tkinter import messagebox, Label, Frame, LEFT
from colors import RED
import numpy as np
from widgets import Shape, MatrixFrame, AnswerFrame, EqualSign, XSign



def validate_shapes(m1, m2):
    matrix_1 = Shape.from_str(m1)
    matrix_2 = Shape.from_str(m2)
    return matrix_1.col == matrix_2.row

def create_random_matrices(m1, m2, zeros, negative) -> Tuple[np.ndarray, np.ndarray]:
    start_range = -11 if negative else 1
    end_range = 12
    if start_range and zeros: start_range -= 1
    matrix_1_shape = Shape.from_str(m1)
    matrix_2_shape = Shape.from_str(m2)
    matrix_1 = np.random.randint(start_range, end_range, size=(matrix_1_shape.to_tuple()))
    matrix_2 = np.random.randint(start_range, end_range, size=(matrix_2_shape.to_tuple()))

    return matrix_1, matrix_2

def handle_generate(m1, m2, zeros, negative, main_window):
    if len(m1) > 5 or len(m2) > 5:
        return messagebox.showerror("select both shapes", "select both matrices shapes")

    if not validate_shapes(m1, m2):
        return messagebox.showerror("Invalide shapes", f"you cannot multiply a matrix with shape {m1} to a matrix with shape {m2}")
    
    matrix_1, matrix_2 = create_random_matrices(m1, m2, zeros, negative)
    MatrixFrame(main_window, matrix_1).pack(side=LEFT, padx=15)
    XSign(main_window, fg=RED).pack(side=LEFT, padx=5)
    MatrixFrame(main_window, matrix_2).pack(side=LEFT, padx=15)
    EqualSign(main_window, fg=RED).pack(side=LEFT, padx=5)
    answer_matrix = matrix_1.dot(matrix_2)
    AnswerFrame(main_window, answer_matrix).pack(side=LEFT, padx=15)
