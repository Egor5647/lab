class ConiferousTree:
    """
    Базовый класс для хвойных деревьев.
    """

    def __init__(self, name: str, age: int) -> None:
        """
        Инициализация базового класса.

        :param name: Название дерева
        :param age: Возраст дерева
        """
        self._name: str = name  # Инкапсулированный атрибут, доступ к которому ограничен
        self.age: int = age

    def __str__(self) -> str:
        """
        Переопределённый метод для строкового представления объекта.
        В дочерних классах добавляет специфическую информацию о типе дерева.
        """
        return f"Хвойное дерево: {self._name}, возраст: {self.age} лет"

    def __repr__(self) -> str:
        """
        Переопределённый метод для точного строкового представления объекта.
        В дочерних классах добавляет дополнительные атрибуты для удобства отладки.
        """
        return f"ConiferousTree(name={self._name}, age={self.age})"

    def produce_resin(self) -> str:
        """
        Переопределённый метод, возвращающий описание выделяемой смолы.
        Разные хвойные деревья выделяют смолу с разными свойствами,
        поэтому метод должен быть специфичным для каждого вида.
        """
        """
        Метод, который должен быть переопределён в дочерних классах.
        """
        raise NotImplementedError("Этот метод должен быть реализован в дочернем классе")


class Spruce(ConiferousTree):
    """
    Дочерний класс для ели.
    """

    def __init__(self, name: str, age: int, height: float) -> None:
        """
        Расширенный конструктор для класса Spruce.

        :param name: Название ели
        :param age: Возраст ели
        :param height: Высота ели
        """
        super().__init__(name, age)
        self.height: float = height

    def __str__(self) -> str:
        return f"Ель: {self._name}, высота: {self.height} м, возраст: {self.age} лет"

    def __repr__(self) -> str:
        return f"Spruce(name={self._name}, age={self.age}, height={self.height})"

    def produce_resin(self) -> str:
        """
        Переопределённый метод, возвращающий описание выделяемой смолы.
        """
        return "Ель выделяет душистую смолу."


class Pine(ConiferousTree):
    """
    Дочерний класс для сосны.
    """

    def __init__(self, name: str, age: int, needle_length: float) -> None:
        """
        Расширенный конструктор для класса Pine.

        :param name: Название сосны
        :param age: Возраст сосны
        :param needle_length: Длина иголок сосны
        """
        super().__init__(name, age)
        self.needle_length: float = needle_length

    def __str__(self) -> str:
        return f"Сосна: {self._name}, длина иголок: {self.needle_length} см, возраст: {self.age} лет"

    def __repr__(self) -> str:
        return f"Pine(name={self._name}, age={self.age}, needle_length={self.needle_length})"

    def produce_resin(self) -> str:
        """
        Переопределённый метод, возвращающий описание выделяемой смолы.
        """
        return "Сосна выделяет клейкую смолу."


if __name__ == "__main__":
    spruce: Spruce = Spruce("Ель обыкновенная", 50, 30.5)
    pine: Pine = Pine("Сосна обыкновенная", 80, 5.2)

    print(spruce)  # Ель: Ель обыкновенная, высота: 30.5 м, возраст: 50 лет
    print(pine)  # Сосна: Сосна обыкновенная, длина иголок: 5.2 см, возраст: 80 лет

    print(spruce.produce_resin())  # Ель выделяет душистую смолу.
    print(pine.produce_resin())  # Сосна выделяет клейкую смолу.
