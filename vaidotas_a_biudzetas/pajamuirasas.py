from vaidotas_a_biudzetas.irasas_f import Irasas


class PajamuIrasas(Irasas):
    def __init__(self, suma, data, siuntejas, papildoma_informacija) -> None:
        super().__init__(suma, data)
        self.siuntejas = siuntejas
        self.papildoma_informacija = papildoma_informacija

    def __str__(self):
        return (
            f"Data: {self.data}, Pajamos - Suma: {self.suma} Eur, Siuntėjas: {self.siuntejas}, "
            f"Papildoma Informacija: {self.papildoma_informacija}")