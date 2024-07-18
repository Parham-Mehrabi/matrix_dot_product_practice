
class Shape:
    def __init__(self, row, col) -> None:
        self.row = row
        self.col = col
    
    def __str__(self) -> str:
        return f"{self.row} x {self.col}"
    
    def __repr__(self) -> str:
        return f"{self.row} x {self.col}"

    @staticmethod
    def from_str(str_shape:str):
        try:
            row, col = [int(i.strip()) for i in str_shape.split("x")]
        except:
            raise ValueError("the input should be in format of 'row x col'")
        return Shape(row, col)

matrices = [Shape(j, i) for j in range(1, 6) for i in range(1, 8)]


def validate_shapes(m1, m2):
    matrix_1 = Shape.from_str(m1)
    matrix_2 = Shape.from_str(m2)
    return matrix_1.col == matrix_2.row
