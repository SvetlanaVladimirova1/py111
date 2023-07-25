# Создайте три (или более) отдельных классов животных.
# Например рыбы, птицы и т.п.
# У каждого класса должны быть как общие свойства,
# например имя, так и специфичные для класса.
# Для каждого класса создайте метод, выводящий
# информацию специфичную для данного класса.
class Animal:
    def __init__(self, name: str):
        self.name = name

    def show_spec(self):
         pass


class Fish(Animal):
    LITLE = 10
    HIGHT = 100

    def __init__(self, name: str, longe: int):
        super().__init__(name)
        self.longe = longe

    def show_spec(self):
        if self.longe <= self.LITLE:
            return 'Мелководная'
        elif self.longe >=  self.HIGHT:
            return 'Глубоководная'
        else:
            return 'Средневодная'


class Bird(Animal):
    def __init__(self, name: str, length: int):
        super().__init__(name)
        self.length = length

    def show_spec(self):
        return self.length * 2


