import pickle
from vaidotas_a_biudzetas.pajamuirasas import PajamuIrasas
from vaidotas_a_biudzetas.islaidusarasas import IslaiduIrasas
import datetime


class Biudzetas:
    def __init__(self):
        self.zurnalas = []

    def prideti_pajamu_irasa(self, data, suma, siuntejas, papildoma_informacija):
        irasas = PajamuIrasas(suma, data, siuntejas, papildoma_informacija)
        self.zurnalas.append(irasas)
        self.issaugoti_duomenis()
        print(f"Pajamų įrašas {irasas} sėkmingai pridėtas.")

    def prideti_islaidu_irasa(self, data, suma, atsiskaitymo_budas, isigyta_preke_paslauga):
        irasas = IslaiduIrasas(suma, data, atsiskaitymo_budas, isigyta_preke_paslauga)
        self.zurnalas.append(irasas)
        self.issaugoti_duomenis()
        print(f"Išlaidų įrašas {irasas} sėkmingai pridėtas.")

    def gauti_balansa(self):
        try:
            with open("biudzetas.pkl", "rb") as file:
                self.zurnalas = pickle.load(file)
            print("Duomenys įkelti")
        except (FileNotFoundError, EOFError):
            print("Failas nerastas")
            self.zurnalas = []
        pajamos = sum(irasas.suma for irasas in self.zurnalas if isinstance(irasas, PajamuIrasas))
        islaidos = sum(irasas.suma for irasas in self.zurnalas if isinstance(irasas, IslaiduIrasas))
        balansas = pajamos - islaidos
        return f"{balansas} Eur"

    def parodyti_ataskaita(self):
        try:
            with open("biudzetas.pkl", "rb") as file:
                self.zurnalas = pickle.load(file)
            print("Duomenys įkelti")
        except (FileNotFoundError, EOFError):
            print("Failas nerastas")
            self.zurnalas = []
        if not self.zurnalas:
            print("Žurnalas tuščias. Nėra įrašų ataskaitai.")
            return
        print(" " * 40, "Biudžeto Ataskaita:")
        print("-" * 100)
        for k, irasas in enumerate(self.zurnalas, start=1):
            print(f"{k}. {irasas}")
        print("-" * 100)
        balansas = self.gauti_balansa()
        print(f"Balansas: {balansas}\n")

    def issaugoti_duomenis(self):
        with open("biudzetas.pkl", "wb") as file:
            pickle.dump(self.zurnalas, file)

    def ikelti_duomenis(self):
        try:
            with open("biudzetas.pkl", "rb") as file:
                self.zurnalas = pickle.load(file)
            print("Duomenys įkelti")
        except (FileNotFoundError, EOFError):
            print("Failas nerastas")
            self.zurnalas = []

biudzetas = Biudzetas()
biudzetas.ikelti_duomenis()

while True:
    print("Biudžeto programa")
    print("1. Įvesti pajamas")
    print("2. Įvesti išlaidas")
    print("3. Rodyti balansą")
    print("4. Rodyti biudžeto ataskaitą")
    print("5. Išeiti")
    print("----------------------------")

    pasirinkimas = input("Pasirinkite veiksmą (1-5): ")

    if pasirinkimas == "1":
        data_input = input("Įveskite datą (YYYY-MM-DD): ")
        try:
            data = datetime.datetime.strptime(data_input, "%Y-%m-%d").date()
        except ValueError:
            print("Klaida: įveskite teisingą datą formatu YYYY-MM-DD.")
            continue
        try:
            suma = abs(float(input("Įveskite pajamų sumą: ")))
            siuntejas = input("Įveskite siuntėją: ").upper()
            papildoma_informacija = input("Įveskite papildomą informaciją apie gautas pajamas: ").upper()
            biudzetas.prideti_pajamu_irasa(data, suma, siuntejas, papildoma_informacija)
            print(f"{suma} Eur pajamos iš {siuntejas} sėkmingai pridėtos.\n")
        except ValueError:
            print(f"Klaida: įveskite skaičių.\n")

    elif pasirinkimas == "2":
        data_input = input("Įveskite datą (YYYY-MM-DD): ")
        try:
            data = datetime.datetime.strptime(data_input, "%Y-%m-%d").date()
        except ValueError:
            print("Klaida: įveskite teisingą datą formatu YYYY-MM-DD.")
            continue
        try:
            suma = abs(float(input("Įveskite išlaidų sumą: ")))
            atsiskaitymo_budas = input("Įveskite atsiskaitymo būdą (grynais, pavedimu, kortele): ").upper()
            isigyta_preke_paslauga = input("Įsigyta prekė ar paslauga: ").upper()
            biudzetas.prideti_islaidu_irasa(data, suma, atsiskaitymo_budas, isigyta_preke_paslauga)
            print(f"{suma} Eur išlaidos už {isigyta_preke_paslauga} sėkmingai pridėtos.\n")
        except ValueError:
            print(f"Klaida: įveskite skaičių.\n")

    elif pasirinkimas == "3":
        balansas = biudzetas.gauti_balansa()
        print(f"\nJūsų balansas yra: {balansas}\n")

    elif pasirinkimas == "4":
        biudzetas.parodyti_ataskaita()

    elif pasirinkimas == "5":
        print("Išeinama iš programos.")
        break

    else:
        print("Neteisingas pasirinkimas. Bandykite dar kartą.\n")
