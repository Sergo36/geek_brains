class Road:
    def __init__(self, lenght, width):
        self._lenght = lenght
        self._width = width
        self.__depth = 5
        self.__massOfAsphalt = 50

    def setMassOfAsphalt(self, massOfAsphalt):
        self.__massOfAsphalt = massOfAsphalt
    def setDepth(self, depth):
        self.__depth = depth

    def mass(self):
        return self._width * self._lenght * self.__depth * self.__massOfAsphalt

road1 = Road(10, 20)
road2 = Road(10, 30)
road2.setDepth(10)
road3 = Road(50, 20)
road3.setMassOfAsphalt(40)
print(road1.mass())
print(road2.mass())
print(road3.mass())
