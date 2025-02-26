class Device:
    def __init__(self, brand: str, model: str, year: int) -> None:
        """Инициализация базового класса Device.
        :param brand: Марка устройства
        :param model: Модель устройства
        :param year: Год выпуска
        """
        self._brand = brand
        self._model = model
        self._year = year

    def get_info(self) -> str:
        """Возвращает информацию об устройстве.
        :return: Строка с информацией об устройстве
        """
        return f"{self._brand} {self._model}, год: {self._year}"

    def __str__(self) -> str:
        """Возвращает строковое представление устройства.
        :return: Строка с маркой и моделью
        """
        return f"{self._brand} {self._model}"

    def __repr__(self) -> str:
        """Возвращает формальное строковое представление устройства.
        :return: Форматированная строка для представления объекта Device
        """
        return f"Device(brand='{self._brand}', model='{self._model}', year={self._year})"


class Smartphone(Device):
    def __init__(self, brand: str, model: str, year: int, os: str) -> None:
        """Инициализация дочернего класса Smartphone.
        :param brand: Марка смартфона
        :param model: Модель смартфона
        :param year: Год выпуска
        :param os: Операционная система
        """
        super().__init__(brand=brand, model=model, year=year)
        self.os = os 

    def get_info(self) -> str:
        """Возвращает информацию о смартфоне, включая его ОС.
        :return: Строка с информацией о смартфоне
        """
        return f"{super().get_info()}, ОС: {self.os}"

    def __str__(self) -> str:
        """Возвращает строковое представление смартфона с указанием ОС.
        :return: Строка с маркой, моделью и ОС
        """
        return f"{self._brand} {self._model} (ОС: {self.os})"


class Laptop(Device):
    def __init__(self, brand: str, model: str, year: int, ram: int) -> None:
        """Инициализация дочернего класса Laptop.
        :param brand: Марка ноутбука
        :param model: Модель ноутбука
        :param year: Год выпуска
        :param ram: Оперативная память в ГБ
        """
        super().__init__(brand=brand, model=model, year=year)
        self.ram = ram  # Публичный атрибут

    def get_info(self) -> str:
        """Возвращает информацию о ноутбуке, включая объем ОЗУ.
        :return: Строка с информацией о ноутбуке
        """
        return f"{super().get_info()}, ОЗУ: {self.ram} ГБ"

    def __str__(self) -> str:
        """Возвращает строковое представление ноутбука с указанием ОЗУ.
        :return: Строка с маркой, моделью и объемом ОЗУ
        """
        return f"{self._brand} {self._model} (ОЗУ: {self.ram} ГБ)"


if __name__ == "__main__":
    smartphone = Smartphone(brand="Samsung", model="Galaxy S22", year=2022, os="Android")
    laptop = Laptop(brand="Apple", model="MacBook Pro", year=2020, ram=16)

    print(smartphone.get_info())
    print(laptop.get_info())
    print(str(smartphone))
    print(repr(smartphone))
    print(str(laptop))
    print(repr(laptop))