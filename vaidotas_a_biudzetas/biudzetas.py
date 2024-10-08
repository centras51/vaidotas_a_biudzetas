import streamlit as st
import pickle
from vaidotas_a_biudzetas.pajamuirasas import PajamuIrasas
from vaidotas_a_biudzetas.islaidusarasas import IslaiduIrasas
import datetime
from typing import Literal

st.set_page_config(layout="wide")



class Biudzetas:
    def __init__(self):
        self.zurnalas = []

    def prideti_pajamu_irasa(self, data, suma, siuntejas, papildoma_informacija):
        irasas = PajamuIrasas(suma, data, siuntejas, papildoma_informacija)
        self.zurnalas.append(irasas)
        self.issaugoti_duomenis()

    def prideti_islaidu_irasa(self, data, suma, atsiskaitymo_budas, isigyta_preke_paslauga):
        irasas = IslaiduIrasas(suma, data, atsiskaitymo_budas, isigyta_preke_paslauga)
        self.zurnalas.append(irasas)
        self.issaugoti_duomenis()

    def gauti_balansa(self):
        try:
            with open("biudzetas.pkl", "rb") as file:
                self.zurnalas = pickle.load(file)
        except (FileNotFoundError, EOFError):
            self.zurnalas = []
        pajamos = sum(irasas.suma for irasas in self.zurnalas if isinstance(irasas, PajamuIrasas))
        islaidos = sum(irasas.suma for irasas in self.zurnalas if isinstance(irasas, IslaiduIrasas))
        balansas = pajamos - islaidos
        return f"{balansas} Eur"

    def parodyti_ataskaita(self):
        try:
            with open("biudzetas.pkl", "rb") as file:
                self.zurnalas = pickle.load(file)
        except (FileNotFoundError, EOFError):
            self.zurnalas = []
        if not self.zurnalas:
            return "Žurnalas tuščias. Nėra įrašų ataskaitai."
        ataskaita = " " * 40 + "Biudžeto Ataskaita:\n"
        ataskaita += "-" * 100 + "\n"
        for k, irasas in enumerate(self.zurnalas, start=1):
            ataskaita += f"{k}. {irasas}\n"
        ataskaita += "-" * 100 + "\n"
        balansas = self.gauti_balansa()
        ataskaita += f"Balansas: {balansas}\n"
        return ataskaita

    def issaugoti_duomenis(self):
        with open("biudzetas.pkl", "wb") as file:
            pickle.dump(self.zurnalas, file)

    def ikelti_duomenis(self):
        try:
            with open("biudzetas.pkl", "rb") as file:
                self.zurnalas = pickle.load(file)
        except (FileNotFoundError, EOFError):
            self.zurnalas = []

biudzetas = Biudzetas()
biudzetas.ikelti_duomenis()

st.title("Biudžeto valdymo programa")
col1, col2 = st.columns(2)

with col1:
    st.subheader("Įvesti pajamas")
    with st.form(key="pajamu_forma"):
        pajamu_data = st.date_input("Pasirinkite datą", datetime.date.today())
        pajamu_suma = st.number_input("Įveskite pajamų sumą", min_value=0.0, format="%.2f")
        pajamu_siuntejas = st.text_input("Įveskite siuntėją").upper()
        pajamu_info = st.text_area("Papildoma informacija").upper()
        if st.form_submit_button("Pridėti pajamas"):
            biudzetas.prideti_pajamu_irasa(pajamu_data, pajamu_suma, pajamu_siuntejas, pajamu_info)
            st.success(f"Pajamų įrašas pridėtas: {pajamu_suma} Eur iš {pajamu_siuntejas}")



with col2:
    st.subheader("Įvesti išlaidas")
    with st.form(key="islaidu_forma"):
        islaidu_data = st.date_input("Pasirinkite datą", datetime.date.today(), key="islaidu_data")
        islaidu_suma = st.number_input("Įveskite išlaidų sumą", min_value=0.0, format="%.2f", key="islaidu_suma")
        islaidu_budas = st.radio("Apmokėjimo būdas", ('Grynais', 'Kortele', 'Pavedimu'), key="horizontal_radio")
        islaidu_prekes = st.text_area("Įsigyta prekė ar paslauga").upper()
        if st.form_submit_button("Pridėti išlaidas"):
            biudzetas.prideti_islaidu_irasa(islaidu_data, islaidu_suma, islaidu_budas, islaidu_prekes)
            st.success(f"Išlaidų įrašas pridėtas: {islaidu_suma} Eur už {islaidu_prekes}. Apmokėjimas {islaidu_budas}")

if st.button("Rodyti balansą"):
    balansas = biudzetas.gauti_balansa()
    st.info(f"Jūsų balansas: {balansas}")

if st.button("Rodyti biudžeto ataskaitą"):
    ataskaita = biudzetas.parodyti_ataskaita()
    st.text(ataskaita)
