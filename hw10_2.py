# Возьмите 1-3 любые задачи из прошлых семинаров (например сериализация
# данных), которые вы уже решали. Превратите функции в методы класса, а
# параметры в свойства. Задачи должны решаться через вызов методов
# экземпляра.
class Quadr:

    def __init__(self, a: float, b: float, c: float):
        self.a = a
        self.b = b
        self.c = c

    def show_dis(self):
        discriminant = self.b ** 2 - 4 * self.a * self.c
        if discriminant == 0:
            return -self.b / (2 * self.a)
        elif discriminant != 0:
            x1 = (-self.b + discriminant ** 0.5) / (2 * self.a)
            x2 = (-self.b - discriminant ** 0.5) / (2 * self.a)
            return x1, x2


rez1 = Quadr(1,2,1)
print(rez1.show_dis())
