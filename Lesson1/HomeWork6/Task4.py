Direction = {"Left": -1,
             "Right": 1}
Cardinal = {0: "Север",
            1: "Восток",
            2: "Юг",
            3: "Запад"}


class Car():
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police
        self.cardinal = 0
    def _setPolice(self, is_police):
        self.is_police = is_police

    def get_speed(self):
        return self.speed
    def go(self):
        self.speed += 10
        print("Скорость автомобиля " + str(self.speed))
    def stop(self):
        self.speed = 0
        print("Автомобиль остановлися")
    def turn(self, direction):
        self.cardinal = self.cardinal + direction
        if self.cardinal < 0:
            self.cardinal = 3
        if self.cardinal > 3:
            self.cardinal = 0
        print("Машина едент в сторону " + Cardinal[self.cardinal])

class TownCar(Car):
    def get_speed(self):
        if (self.speed > 60):
            print("Превышение скорости")
        return self.speed

class SportCar(Car):
    pass

class WorkCar(Car):
    def get_speed(self):
        if (self.speed > 40):
            print("Превышение скорости")
        return self.speed

class PoliceCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name, True)

myCar = Car(50, "red", "myCar", False)

print(myCar.get_speed())
myCar.go()
myCar.turn(Direction["Left"])
myCar.turn(Direction["Left"])
myCar.turn(Direction["Right"])
myCar.turn(Direction["Left"])
myCar.turn(Direction["Left"])
myCar.turn(Direction["Left"])
myCar.stop()
print(myCar.get_speed())

myTownCar = TownCar(70, "green", "myTownCar", False)
print(myTownCar.get_speed())

myWorkCar = WorkCar(50, "green", "myTownCar", False)
print(myTownCar.get_speed())

myPoliceCar = PoliceCar(170, "green", "myTownCar")
print(myTownCar.get_speed())
print(myPoliceCar.is_police)