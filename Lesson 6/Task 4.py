"""
Lesson6.Task4.
Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed, color, name, is_police (
булево).  А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась,
повернула (куда). Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar. Добавьте в базовый класс
метод show_speed, который должен показывать текущую скорость автомобиля. Для классов TownCar и WorkCar переопределите
метод show_speed. При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении
скорости. Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам,
выведите результат. Выполните вызов методов и также покажите результат.
"""


class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        return f'начала движение'

    def stop(self):
        return f'остановилась'

    def turn_right(self):
        return f'повернула налево'

    def turn_left(self):
        return f'повернула направо'

    def show_speed(self):
        return f'Текущая скорость составляет {self.speed}'


class TownCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        print(f'Текущая скорость {self.name} соствляет {self.speed}')

        if self.speed > 40:
            return f'{self.name} превышение ограничения скорости!'


class SportCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)


class WorkCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        print(f'Текущая скорость {self.name} составляет {self.speed}')

        if self.speed > 60:
            return f'{self.name} превышение ограничения скорости!'


class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def police(self):
        if self.is_police:
            return f'{self.name} полицейская машина'
        else:
            return f'{self.name} не является полицейской машиной'


town = TownCar(80, 'Белый', 'Geely', False)
sport = SportCar(230, 'Красный', 'Mustang', False)
work = WorkCar(70, 'Синий', 'Volkswagen', True)
police = PoliceCar(110, 'Черный', 'Audi', True)
print(town.show_speed())
print(work.show_speed())
print(sport.show_speed())
print(police.show_speed())
print(f'Машина {sport.color} {sport.name} {sport.go()}. {sport.show_speed()}. Полицейская машина? {sport.is_police}')
print(
    f'Машина {police.color} {police.name} {police.go()}, {police.turn_left()}. Полицейская машина? {police.is_police}')
print(f'Машина {town.color} {town.name} {town.go()}, {town.turn_right()}. {town.show_speed()}')
print(f'Машина {work.color} {work.name} {work.stop()}')
