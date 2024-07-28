"""Принцип разделения интерфейсов
    Создайте детализированные 'интерфейсы, спецефичные' для конкретного клиента.
"""

"""Как не делать"""
class Shape:
    def draw_circle(self):
        raise NotImplementedError

    def draw_rectangle(self):
        raise NotImplementedError


class Circle(Shape):
    def draw_circle(self):
        pass

    def draw_rectangle(self):
        pass


"""Как делать"""
class Shape:
    def draw(self):
        raise NotImplementedError


class Circle:
    def draw(self):
        pass


class Square(Shape):
    def draw(self):
        pass
