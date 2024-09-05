class Position:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self) -> str:
        return f"Position({self.x}, {self.y})"

    def __str__(self) -> str:
        return f"{self.x}, {self.y}"
    
    def __eq__(self, other: object) -> bool:
        if isinstance(other, Position):
            return other.x == self.x and other.y == self.y
        return False
    
if __name__ == "__main__":
    ...