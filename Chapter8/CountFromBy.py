class CountFromBy:

    def __init__(self, start: int = 0, step: int = 1) -> None:
        """initialize object with provided or default data"""
        self.counter = start
        self.step = step

    def __repr__(self) -> str:
        return str(self.counter)

    def increment(self) -> None:
        self.counter += self.step
