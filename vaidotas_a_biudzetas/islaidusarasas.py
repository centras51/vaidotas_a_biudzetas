from vaidotas_a_biudzetas.irasas_f import Irasas


class IslaiduIrasas(Irasas):
    def __init__(self, suma, data, atsiskaitymo_budas, isigyta_preke_paslauga) -> None:
        super().__init__(suma, data)
        self.atsiskaitymo_budas = atsiskaitymo_budas
        self.isigyta_preke_paslauga = isigyta_preke_paslauga

    def __str__(self):
        return (
            f"Data: {self.data}, Išlaidos - Suma: {self.suma} Eur, Atsiskaitymo būdas: {self.atsiskaitymo_budas}, "
            f"Įsigyta prekė/paslauga: {self.isigyta_preke_paslauga}")