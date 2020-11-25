from  time import time


def nextTime():
    cnt = 0
    list = [7000,2000,9000]
    while True:
        yield list[cnt]
        cnt += 1
        if cnt > 2:
            cnt = 0

curent_mili_time = lambda: int(round(time() * 1000))
time = {0:"red",
        1:"yelow",
        2:"green"}
list[7000,2000,9000]
class TrafficLight:
    def __init__(self, color):
        self.__color = color
        self.__lastTime = curent_mili_time()
        self.currentColor = 0

    def running(self):
        currentLastTime = self.__lastTime
        currentTime = curent_mili_time

        while currentLastTime < currentTime:
            currentTime += list[cnt]
            cnt = cnt %3
        self.currentColor

