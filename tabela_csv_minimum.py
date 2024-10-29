import csv
import re
from pridobi_podatke_podstrani import pridobi_kazni_za_drzavo, drzave

# Ime datoteke, kamor bomo shranili podatke
csv_datoteka = "kazni_evropske_drzave_minimum.csv"

# Funkcija za pridobitev minimuma iz kazni
def pridobi_minimum(cena):
    if not cena:
        return 0
    try:
        # Preveri, ali obstaja interval (npr. "50 - 150")
        match = re.search(r'(\d+.\d*)\s*-\s*(\d+.\d*)', cena)
        if match:
            # Vrni prvo številko kot minimum
            return match.group(1)
        # Preveri, če je cena samo ena številka
        match = re.search(r'\d+.\d*', cena)
        if match:
            return match.group(0)
    except Exception as e:
        return "Napaka pri obdelavi"
    return 0

# Funkcija za zapisovanje podatkov v CSV z minimalnimi kaznimi
def shrani_v_csv_minimum(podatki):
    with open(csv_datoteka, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        # Zapis glave tabele
        writer.writerow(['Država', 'Valuta', 'Min kazni za alkohol', 'Min kazni za prehitro vožnjo', 'Min kazni za varnostni pas', 'Min kazni za mobilni telefon'])
        # Zapis podatkov za vsako državo
        for vrednost in podatki:
            writer.writerow([
                vrednost['drzava'], 
                vrednost['valuta'], 
                pridobi_minimum(vrednost['alkohol']),
                pridobi_minimum(vrednost['voznja']),
                pridobi_minimum(vrednost['pas']),
                pridobi_minimum(vrednost['telefon'])
            ])

# Glavna funkcija za pridobitev podatkov in shranjevanje v CSV
def zberi_podatke_in_shrani_minimum():
    vsi_podatki = []

    for drzava in drzave:
        kazni = pridobi_kazni_za_drzavo(drzava)

        if kazni:
            vsi_podatki.append(kazni)

    shrani_v_csv_minimum(vsi_podatki)
    print(f"Podatki uspešno shranjeni v datoteko {csv_datoteka}.")

# Zaženi program
zberi_podatke_in_shrani_minimum()
