
class Shape:
    def __init__(self, row, col) -> None:
        self.row = row
        self.col = col
    
    def __str__(self) -> str:
        return f"{self.row} x {self.col}"
    
    def __repr__(self) -> str:
        return f"{self.row} x {self.col}" 

matrices = [Shape(i, j) for j in range(1, 6) for i in range(1, 8)]
