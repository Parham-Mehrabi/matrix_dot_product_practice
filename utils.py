from typing import Tuple
from tkinter import messagebox, Label, Frame, LEFT
from colors import RED
import numpy as np
from widgets import Shape, MatrixFrame, AnswerFrame, EqualSign, XSign



def validate_shapes(m1, m2):
    matrix_1 = Shape.from_str(m1)
    matrix_2 = Shape.from_str(m2)
    return matrix_1.col == matrix_2.row

def create_random_matrices(m1, m2, zeros, max_matrix_num, negative) -> Tuple[np.ndarray, np.ndarray]:
    start_range = (-1 * max_matrix_num) if negative else 1
    end_range = max_matrix_num
    if start_range == 1 and zeros: start_range -= 1
    matrix_1_shape = Shape.from_str(m1)
    matrix_2_shape = Shape.from_str(m2)
    matrix_1 = np.random.randint(start_range, end_range, size=(matrix_1_shape.to_tuple()))
    matrix_2 = np.random.randint(start_range, end_range, size=(matrix_2_shape.to_tuple()))

    return matrix_1, matrix_2

created_questions = []

def handle_generate(m1, m2, zeros, negative, max_matrix_num, main_window):
    global created_questions

    if len(m1) > 5 or len(m2) > 5:
        return messagebox.showerror("select both shapes", "select both matrices shapes")

    if not validate_shapes(m1, m2):
        return messagebox.showerror("Invalide shapes", f"you cannot multiply a matrix with shape {m1} to a matrix with shape {m2}")
    
    matrix_1, matrix_2 = create_random_matrices(m1, m2, zeros, max_matrix_num, negative)

    for widget in created_questions:
        widget.destroy()

    m1f = MatrixFrame(main_window, matrix_1)
    xs = XSign(main_window, fg=RED)
    m2f = MatrixFrame(main_window, matrix_2)
    es = EqualSign(main_window, fg=RED)
    answer_matrix = matrix_1.dot(matrix_2)
    af = AnswerFrame(main_window, answer_matrix)
    m1f.pack(side=LEFT, padx=15)
    xs.pack(side=LEFT, padx=5)
    m2f.pack(side=LEFT, padx=15)
    es.pack(side=LEFT, padx=5)
    af.pack(side=LEFT, padx=15)
    created_questions = [m1f, xs, m2f, es, af]

