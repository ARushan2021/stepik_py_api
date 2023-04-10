class Car:
    """Создаем класс автомобилей"""
    def __init__(self, model, release_year, engine_capacity, mileage):
        self.model = model
        self.release_year = release_year
        self.engine_capacity = engine_capacity
        self.mileage = mileage
        self.number_of_wheels = 4

    def description_car(self):
        """Получение описания автомобиля"""
        description = f'модель авто - {self.model}, ' \
                      f'год выпуска - {self.release_year}, ' \
                      f'объем двигателя - {self.engine_capacity}, ' \
                      f'пробег - {self.mileage}, ' \
                      f'кол.во колес - {self.number_of_wheels}'
        return description


class Truck(Car):
    """Создаем класс грузовиков"""
    def __init__(self, model, release_year, engine_capacity, mileage):
        super().__init__(model, release_year, engine_capacity, mileage)
        self.number_of_wheels = 8


kalina = Car("lada_kalina", 2010, 1.5, 100000)
print(kalina.description_car())

gazel = Truck('gaz', 2011, 1.8, 150000)
print(gazel.description_car())
