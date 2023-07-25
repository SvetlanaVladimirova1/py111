# Доработаем задачи 5-6. Создайте класс-фабрику.
# ○ Класс принимает тип животного (название одного из созданных классов)
# и параметры для этого типа.
# ○ Внутри класса создайте экземпляр на основе переданного типа и
# верните его из класса-фабрики.
from h5_8 import Fish


class Fabric(Fish):
    def __init__(self, name: str, longe: int):
        self.name = name
        self.longe = longe


rez1 = Fabric('карась', 4)
rez2 = Fabric('щука', 14)
rez3 = Fabric('акула', 100)
fish_list = [rez1, rez2, rez3]
for fish in fish_list:
    print(fish.show_spec())




