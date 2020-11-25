class Worker:
    def __init__(self, name, surname, position, income):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = income


class Position(Worker):
    def get_full_name(self):
        return F"{self.name} {self.surname}"

    def get_total_income(self):
        return self._income["wage"]+ self._income["bonus"]

income = {"wage": 50, "bonus": 10}

pos = Position("Sergey", "Repin", "Developer", income)
print(pos.get_full_name())
print(pos.get_total_income())

