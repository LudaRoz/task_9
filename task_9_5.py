class Stationery:
    title = 'Stationery'

    def draw(self):
        print(f'Запуск отрисовки {Stationery.title}')


class Pen(Stationery):
    def __init__(self, title):
        self.title = title

    def draw(self):
        print(f'Запуск отрисовки {self.title}')


class Pencil(Stationery):
    def __init__(self, title):
        self.title = title

    def draw(self):
        print(f'Запуск отрисовки {self.title}')


class Handle(Stationery):
    def __init__(self, title):
        self.title = title

    def draw(self):
        print(f'Запуск отрисовки {self.title}')


pen = Pen('pen')
pen.draw()

pencil = Pencil('pencil')
pencil.draw()

handle = Handle('handle')
handle.draw()

stationery = Stationery()
stationery.draw()
