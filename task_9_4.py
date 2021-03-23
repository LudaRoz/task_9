class Car:
    speed = 0
    color = ''
    name = ''
    is_police = True

    def go(self):
        print('Go')

    def stop(self):
        print('Stop')

    def turn(self, direction):
        self.direction = direction
        print(f'Turn {direction}')

    def show_speed(self, speed):
        self.speed = speed
        print(f'Your speed is {self.speed}.')


class TownCar(Car):
    def __init__(self, color, name):
        self.color = Car.color
        self.name = Car.name
        is_police = False
        print(f'Color is {color}, Name of car is {name}, Is police {is_police}')

    def show_speed(self, speed):
        Car.speed = speed
        if speed > 60:
            print(f'Alert. You are speed up!!! Your speed is {speed}.')
        else:
            Car.show_speed(self, speed)


class SportCar(Car):
    def __init__(self, color, name):
        self.color = Car.color
        self.name = Car.name
        is_police = False
        print(f'Color is {color}, Name of car is {name}, Is police {is_police}')


class WorkCar(Car):
    def __init__(self, color, name):
        self.color = Car.color
        self.name = Car.name
        is_police = False
        print(f'Color is {color}, Name of car is {name}, Is police {is_police}')

    def show_speed(self, speed):
        self.speed = Car.speed
        if speed > 40:
            print(f'Alert. You are speed up!!! Your speed is {speed}.')
        else:
            Car.show_speed(self, speed)


class PoliceCar(Car):
    def __init__(self, color, name):
        self.color = Car.color
        self.name = Car.name
        is_police = True
        print(f'Color is {color}, Name of car is {name}, Is police {is_police}')


car_1 = WorkCar('Red', 'Mazda')
car_1.show_speed(50)
car_1.show_speed(10)
car_1.stop()


car_2 = TownCar('Green', 'BMW')
car_2.show_speed(100)
car_2.show_speed(40)
car_2.turn('left')
car_2.go()

car_3 = PoliceCar('White', 'Nissan')
