import time


class TrafficLight:
    color = 'Red', 'Yellow', 'Green'

    def running(self):
        self.__id = id
        for index in TrafficLight.color:
            print(index)
            if index == 'Red':
                time.sleep(7)
            elif index == 'Yellow':
                time.sleep(2)
            elif index == 'Green':
                time.sleep(10)


car = TrafficLight()
car.running()
print('-----')
car.running()
