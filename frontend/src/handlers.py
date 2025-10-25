class MyHandler:
    """
    A simple handler class that manages an integer and a string value.

    Attributes:
        a (int): An integer value that can be increased.
        b (str): A string value that can be appended to.
    """

    def __init__(self, a: int, b: str):
        self.a = a
        self.b = b

    def display(self) -> None:
        """
        Print the current values of `a` and `b` to the console.
        """
        print(self.a, self.b)

    def increase(self, value: int) -> None:
        """
        Increase the integer value `a` by a given amount.

        Args:
            value (int): The amount to add to `a`.
        """
        self.a += value

    def append(self, value: str) -> None:
        """
        Append a string to the existing string value `b`.

        Args:
            value (str): The string to append to `b`.
        """
        self.b += value


class MyFakeHandler:
    """
    A mock handler class used for demonstration or testing purposes.

    Attributes:
        x (float): A floating-point value that can be scaled.
        y (list[str]): A list of strings that can be extended.
    """

    def __init__(self, x: float, y: list[str]):
        self.x = x
        self.y = y

    def show(self) -> None:
        """
        Display the current values of `x` and `y`.
        """
        print(f"x: {self.x}, y: {self.y}")

    def scale(self, factor: float) -> None:
        """
        Multiply the float value `x` by a given factor.

        Args:
            factor (float): The multiplier to apply to `x`.
        """
        self.x *= factor

    def extend(self, items: list[str]) -> None:
        """
        Extend the list `y` with additional string items.

        Args:
            items (list[str]): A list of strings to add to `y`.
        """
        self.y.extend(items)
