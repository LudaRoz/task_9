class Road:
    _length = 0
    _width = 0

    def asphaltMass(self, length, width):
        self._length = length
        self._width = width
        mass = length * width * 25 * 5
        print(mass)


road = Road()
road.asphaltMass(20, 5000)

