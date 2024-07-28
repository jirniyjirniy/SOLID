"""Принцип подстановки Лисков
    Функции, которые 'используют базовый тип', должны иметь возможность 'использовать подтипы' базового типа,
     не зная об этом.
"""


"""Как не делать"""
class Vehicle:
    def __init__(self, name: str, speed: float):
        self.name = name
        self.speed = speed

    def get_name(self) -> str:
        return f'Название машины {self.name}'

    def get_speed(self) -> float:
        return f'Скорость машины {self.speed}'

    def engine(self):
        pass

    def start_engine(self):
        self.engine()


class Car(Vehicle):
    def start_engine(self):
        pass


class Bicycle(Vehicle):
    def start_engine(self):
        pass


"""Как делать"""
class Vehicle:
    def __init__(self, name: str, speed: float):
        self.name = name
        self.speed = speed

    def get_name(self) -> str:
        return f'Название машины {self.name}'

    def get_speed(self) -> float:
        return f'Скорость машины {self.speed}'


class VehicleWithoutEngine(Vehicle):
    def start_moving(self):
        raise NotImplemented


class VehicleWithEngine(Vehicle):
    def engine(self):
        pass

    def start_engine(self):
        self.engine()


class Car(VehicleWithEngine):
    def start_engine(self):
        pass


class Bicycle(VehicleWithoutEngine):
    def start_moving(self):
        pass
    