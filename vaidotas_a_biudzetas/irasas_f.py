class Irasas:
    def __init__(self, suma, data) -> None:
        self.suma = suma
        self.data = data

    def __str__(self) -> str:
        return f"Data: {self.data}, Suma: {self.suma} Eur"