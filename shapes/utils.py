from .shape import Shape

def calculate_area(shape):
    if isinstance(shape, Shape):
        return shape.area()
    else:
        raise ValueError("Такой фигуры нет")