# -*- config: utf-8 -*-

from termcolor import colored
class House:

    def __init__(self):
        self.numberOfFloors = 10


house = House()

for floor in range(1, house.numberOfFloors + 1):
    print(colored('Текущий этаж равен', 'green', force_color=True), colored(floor, 'red', force_color=True))