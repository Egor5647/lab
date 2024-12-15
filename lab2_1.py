import doctest


class Bottle:
    def __init__(self, capacity_volume: float, occupied_volume: float):
        """
        Создание и подготовка к работе объекта "Бутылка"

        :param capacity_volume: Объем бутылки
        :param occupied_volume: Объем жидкости внутри бутылки

        Примеры:
        >>> bottle = Bottle(1000, 500)
        """
        if not isinstance(capacity_volume, (int, float)):
            raise TypeError("Объем бутылки должен быть типа int или float")
        if capacity_volume <= 0:
            raise ValueError("Объем бутылки должен быть положительным числом")
        self.capacity_volume = capacity_volume

        if not isinstance(occupied_volume, (int, float)):
            raise TypeError("Количество жидкости должно быть типа int или float")
        if occupied_volume < 0:
            raise ValueError("Количество жидкости не может быть отрицательным числом")
        if occupied_volume > capacity_volume:
            raise ValueError("Количество жидкости не может превышать объем бутылки")
        self.occupied_volume = occupied_volume

    def is_full(self) -> bool:
        """
        Проверка, полна ли бутылка.

        :return: True, если бутылка полна, иначе False

        Примеры:
        >>> bottle = Bottle(1000, 1000)
        >>> bottle.is_full()
        True
        """
        return self.occupied_volume == self.capacity_volume

    def pour_in(self, volume: float) -> None:
        """
        Добавление жидкости в бутылку.

        :param volume: Объем добавляемой жидкости
        :raise ValueError: Если объем добавляемой жидкости превышает доступное пространство

        Примеры:
        >>> bottle = Bottle(1000, 500)
        >>> bottle.pour_in(400)
        >>> bottle.occupied_volume
        900
        """
        if volume <= 0:
            raise ValueError("Добавляемый объем должен быть положительным числом")
        if self.occupied_volume + volume > self.capacity_volume:
            raise ValueError("Объем превышает вместимость бутылки")
        self.occupied_volume += volume

    def pour_out(self, volume: float) -> None:
        """
        Удаление жидкости из бутылки.

        :param volume: Объем удаляемой жидкости
        :raise ValueError: Если объем жидкости для удаления больше, чем содержимое бутылки

        Примеры:
        >>> bottle = Bottle(1000, 500)
        >>> bottle.pour_out(200)
        >>> bottle.occupied_volume
        300
        """
        if volume <= 0:
            raise ValueError("Удаляемый объем должен быть положительным числом")
        if volume > self.occupied_volume:
            raise ValueError("Недостаточно жидкости в бутылке")
        self.occupied_volume -= volume


if __name__ == "__main__":
    doctest.testmod()



import doctest
class BankCard:
    def __init__(self, card_number: str, balance: float):
        """
        Создание объекта "Банковская карта"

        :param card_number: Номер карты (16 цифр)
        :param balance: Баланс карты

        Примеры:
        >>> card = BankCard("1234567812345678", 1000.0)
        """
        if not isinstance(card_number, str) or len(card_number) != 16 or not card_number.isdigit():
            raise ValueError("Номер карты должен быть строкой из 16 цифр")
        if not isinstance(balance, (int, float)) or balance < 0:
            raise ValueError("Баланс должен быть неотрицательным числом")
        self.card_number = card_number
        self.balance = balance

    def deposit(self, amount: float) -> None:
        """
        Пополнение карты.

        :param amount: Сумма для пополнения
        :raise ValueError: Если сумма отрицательная

        Примеры:
        >>> card = BankCard("1234567812345678", 1000.0)
        >>> card.deposit(500)
        >>> card.balance
        1500.0
        """
        if amount <= 0:
            raise ValueError("Сумма для пополнения должна быть положительной")
        self.balance += amount

    def withdraw(self, amount: float) -> None:
        """
        Снятие средств с карты.

        :param amount: Сумма для снятия
        :raise ValueError: Если сумма превышает баланс

        Примеры:
        >>> card = BankCard("1234567812345678", 1000.0)
        >>> card.withdraw(200)
        >>> card.balance
        800.0
        """
        if amount <= 0:
            raise ValueError("Сумма для снятия должна быть положительной")
        if amount > self.balance:
            raise ValueError("Недостаточно средств на карте")
        self.balance -= amount


if __name__ == "__main__":
    doctest.testmod()



import doctest
class Smartphone:
    def __init__(self, brand: str, battery_capacity: int):
        """
        Создание объекта "Смартфон"

        :param brand: Бренд смартфона
        :param battery_capacity: Ёмкость аккумулятора в мАч

        Примеры:
        >>> phone = Smartphone("Samsung", 4000)
        """
        if not isinstance(brand, str) or not brand:
            raise ValueError("Бренд должен быть непустой строкой")
        if not isinstance(battery_capacity, int) or battery_capacity <= 0:
            raise ValueError("Ёмкость аккумулятора должна быть положительным целым числом")
        self.brand = brand
        self.battery_capacity = battery_capacity
        self.battery_level = 100

    def use(self, hours: int) -> None:
        """
        Использование смартфона, что снижает заряд аккумулятора.

        :param hours: Количество часов использования
        :raise ValueError: Если часы отрицательные или заряд закончился

        Примеры:
        >>> phone = Smartphone("Samsung", 4000)
        >>> phone.use(2)
        >>> phone.battery_level
        80
        """
        if hours <= 0:
            raise ValueError("Время использования должно быть положительным")
        if self.battery_level <= 0:
            raise ValueError("Батарея разряжена")
        self.battery_level = max(0, self.battery_level - hours * 10)

    def charge(self) -> None:
        """
        Полная зарядка смартфона.

        Примеры:
        >>> phone = Smartphone("Samsung", 4000)
        >>> phone.use(2)
        >>> phone.charge()
        >>> phone.battery_level
        100
        """
        self.battery_level = 100


if __name__ == "__main__":
    doctest.testmod()