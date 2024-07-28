"""Принцип открытости/закрытости
    Вы должны иметь возможность 'расширить' поведение классов, 'не изменяя' его
"""


class Discount:
    def __init__(self, customer, price):
        self.customer = customer
        self.price = price

    def give_discount(self):
        return self.price * 0.2

    # Надо добавить ВИП-скидку
    # Сталдо хуже
    def give_discount(self):
        if self.customer == 'vip':
            return self.price * 0.4


"""Решение, создать класс наследник"""
class VIPDiscount(Discount):
    def get_discount(self):
        return super().get_discount() * 2