from dataclasses import dataclass

@dataclass(order=True)
class Student:
    name: str           # ім’я студента
    surname: str        # прізвище студента
    discipline: str     # назва дисципліни
    mark: int           # оцінка з дисципліни
    exam: str = "іспит" # передвстановлене значення

    def get_info(self) -> str:
        """Метод для виведення стислої інформації"""
        return f"Student({self.name}, {self.surname}, {self.discipline}, {self.exam}, {self.mark})"

    # def __repr__(self):
    #     return self.get_info()
    def get_message(self) -> str:
        """Метод для виведення інформації по алгоритму"""

        if self.mark in range(0,60):
            letter, markname = "FX", "незадовільно"
        elif self.mark in range(60, 68):
            letter, markname = "E", "задовільно"
        elif self.mark in range(68, 75):
            letter, markname = "D", "задовільно"
        elif self.mark in range(75, 83):
            letter, markname = "C", "добре"
        elif self.mark in range(83, 90):
            letter, markname = "B", "добре"
        elif self.mark in range(90, 101):
            letter, markname = "A", "відмінно"
        else:
            raise ValueError("Некоретне значення")

        if self.exam == "залік" and self.mark < 60:
            markname = "незараховано"
        elif self.exam == "залік":
            markname = "зараховано"

        return f'"Студент {self.name} {self.surname} ' \
               f'по предмету {self.discipline} отримав ' \
               f'оцінку "{markname}" ({letter}, {self.mark})"'

    @property
    def mark(self):
        # print("getter")
        return self.__mark

    @mark.setter
    def mark(self, value):
        # print("setter")
        if type(value) != int:
            raise TypeError
        elif value < 0 or value > 100:
            raise ValueError
        else:
            self.__mark = value

