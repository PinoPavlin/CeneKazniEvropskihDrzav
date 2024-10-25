import csv
import re
from pridobi_podatke_podstrani import pridobi_kazni_za_drzavo, drzave

# Ime datoteke, kamor bomo shranili podatke
csv_file = "kazni_evropske_drzave_eur.csv"

# Pretvornik valut
conversion_rates = {
    'EUR': 1,       # Evro je referenčna valuta
    'USD': 0.925,   # Primer tečaja za ameriški dolar (1 USD = 0.92 EUR)
    'GBP': 1.198,
    'ALL': 0.01,
    'BYN': 0.281,
    'BAM': 0.511,
    'BGN': 0.511,
    'CZK': 0.039,
    'DKK': 0.134,
    'ISK': 0.007,
    'CHF': 1.067,
    'HUF': 0.002,
    'MDL': 0.052,
    'NOK': 0.084,
    'PLN': 0.23,
    'RON': 0.2,
    'RUB': 0.01,
    'MKD': 0.016,
    'RSD': 0.009,
    'SEK': 0.087,
    'TRY': 0.027,
    'UAH': 0.022,
}

# Funkcija za pretvorbo cen v EUR
def pretvori_v_eur(cena, valuta):
    if not cena:
        return 0
    try:
        # Preveri, ali obstaja interval (npr. "50 - 150")
        match = re.search(r'(\d+.\d*)\s*-\s*(\d+.\d*)', cena)
        if match:
            # print(match.group(1).replace(".",""))
            # Vrni prvo številko kot minimum in jo pretvori v EUR
            return round(float(match.group(1).replace(".","").replace(",",".")) * conversion_rates.get(valuta), 2)
        # Preveri, če je cena samo ena številka
        match = re.search(r'\d+.\d*', cena)
        if match:
            # print(match.group(0).replace(".",""))
            return round(float(match.group(0).replace(".","").replace(",",".")) * conversion_rates.get(valuta), 2)
    except Exception as e:
        return "Napaka pri obdelavi"
    return 0

# Funkcija za zapisovanje podatkov v CSV z minimalnimi kaznimi, pretvorjenimi v EUR
def shrani_v_csv_eur(podatki):
    with open(csv_file, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        # Zapis glave tabele
        writer.writerow(['Država', 'Valuta', 'Min kazni za alkohol (EUR)', 'Min kazni za prehitro vožnjo (EUR)', 'Min kazni za varnostni pas (EUR)', 'Min kazni za mobilni telefon (EUR)'])
        # Zapis podatkov za vsako državo
        for val in podatki:
            writer.writerow([
                val['drzava'],
                val['valuta'],
                pretvori_v_eur(val['alkohol'], val['valuta']),
                pretvori_v_eur(val['voznja'], val['valuta']),
                pretvori_v_eur(val['pas'], val['valuta']),
                pretvori_v_eur(val['telefon'], val['valuta'])
            ])

# Glavna funkcija za pridobitev podatkov in shranjevanje v CSV
def zberi_podatke_in_shrani_eur():
    vsi_podatki = []

    for drzava in drzave:
        kazni = pridobi_kazni_za_drzavo(drzava)

        if kazni:
            vsi_podatki.append(kazni)

    shrani_v_csv_eur(vsi_podatki)
    print(f"Podatki uspešno shranjeni v datoteko {csv_file}.")

# Zaženi program
zberi_podatke_in_shrani_eur()
