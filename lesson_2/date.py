# 1. Реализовать класс Date и TimeDelta
# 2. Протестировать (полностью покрыть тестами). Не забудь проверить даты на корректность.

# При разработке использовать github
# * Настроить Travis CI для проекта на странице github
# * Создать пакет (модуль) из проекта и выгрузить на https://test.pypi.org/

# * - подробно разберем на следующей практике

from typing import Optional, overload

import logging
logger = logging.getLogger(__name__)


class TimeDelta:
    def __init__(self, days: Optional[int] = None, months: Optional[int] = None, years: Optional[int] = None):
        ...


class Date:
    """Класс для работы с датами"""

    # @overload
    # def __init__(self, day: int, month: int, year: int):
    #     """Создание даты из трех чисел"""
    #
    # @overload
    # def __init__(self, date: str):
    #     """Создание даты из строки формата dd.mm.yyyy"""

    def __init__(self, *args):
        # Проверяем на 3 значения между точками. Если не равно 3, то ошибка.

        logger.debug("Делим на 3 части: день месяц и год")
        if len(args) == 3 and (isinstance(i, int) for i in args):
            self.day, self.month, self.year = (args[0]), int(args[1]), int(args[2])
            logger.info("День: %s , Месяц: %s , Год: %s ," % (self.day, self.month, self.year))
        elif len(args) == 1 and isinstance(args[0], str):
            values = args[0].split(".")
            if len(values) != 3:
                raise ValueError("Некорректное значение")
            self.day, self.month, self.year = (values[0]), int(values[1]), int(values[2])
            logger.info("День: %s , Месяц: %s , Год: %s ," % (self.day, self.month, self.year))
        else:
            raise ValueError("Некорректное значение")

    def __str__(self) -> str:
        return f"{self.day}'.'{self.month}'.'{self.year}"

    def __repr__(self) -> str:
        """Возвращает дату в формате Date(day, month, year)"""

    @classmethod
    def is_leap_year(self, year: int) -> bool:
        """Проверяет, является ли год високосным"""
        if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
            return True
        else:
            return False

    @classmethod
    def get_max_day(self, month: int, year: int) -> int:
        """Возвращает максимальное количество дней в месяце для указанного года"""

    @classmethod
    def is_valid_date(self, day: int, month: int, year: int):
        """Проверяет, является ли дата корректной"""

    @property
    def day(self):
        return self._day

    @day.setter
    def day(self, value: int):
        """value от 1 до 31. Проверять значение и корректность даты"""
        if not (1 <= value <= 31):
            raise ValueError("Не верная дата")
        self._day = value

    @property
    def month(self):
        return self.month

    @month.setter
    def month(self, value: int):
        """value от 1 до 12. Проверять значение и корректность даты"""
        print(self.day, value)
        # if self.month > 12 and self.month < 1:
        #     raise ValueError("Некорректное значение")

    @property
    def year(self):
        return self.year

    @year.setter
    def year(self, value: int):
        """value от 1 до ... . Проверять значение и корректность даты"""
        if not (1000 <= value <= 3000):
            raise ValueError("Не верный год")
        self.year = value

    def __sub__(self, other: "Date") -> int:
        """Разница между датой self и other (-)"""

    def __add__(self, other: TimeDelta) -> "Date":
        """Складывает self и некий timedeltа. Возвращает НОВЫЙ инстанс Date, self не меняет (+)"""

    def __iadd__(self, other: TimeDelta) -> "Date":
        """Добавляет к self некий timedelta меняя сам self (+=)"""


def _main():
    logging.basicConfig()
    logger.setLevel(logging.DEBUG)

    logger.debug("start main")
    date = Date(01.02.1995)
    logger.debug("create date : 1, 2, 1995")

    #date2 = Date("3.2.1995")



if __name__ == "__main__":
    _main()
