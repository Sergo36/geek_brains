class Stationery():
    def __init__(self, title):
        self.title = title
    def draw(self):
        print("Запуск отрисовки")

class Pen(Stationery):
    def draw(self):
        print("Запуск отрисовки ручкой")

class Pencil(Stationery):
    def draw(self):
        print("Запуск отрисовки карандашом")

class Handle(Stationery):
    def draw(self):
        print("Запуск отрисовки маркером")

Stationery1 = Stationery("Объект")
Stationery2 = Pen("Моя ручка")
Stationery3 = Pencil("Мой карандаш")
Stationery3 = Handle("Мой маркер")

Stationery1.draw()
Stationery2.draw()
Stationery3.draw()
Stationery3.draw()