class Worker:
    name = ''
    surname = ''
    position = ''
    income_tuple = {"wage": 0, "bonus": 0}
    __income = income_tuple


class Position(Worker):
    def get_full_name(self, name, surname, position):
        self.name = Worker.name
        self.surname = Worker.surname
        self.position = Worker.position
        full_name = name + ' ' + surname
        print(f'Full name: {full_name}\nPosition: {position}')

    def get_total_income(self, wage, bonus):
        Worker.income_tuple[wage] = wage
        Worker.income_tuple[bonus] = bonus
        income = 0
        for value in Worker.income_tuple.values():
            income += value
        self.__income = income
        print(f'Income: {self.__income}')


worker = Position()
worker.get_full_name('Misha', 'Qwerty', 'Boss')
worker.get_total_income(8465, 10)
