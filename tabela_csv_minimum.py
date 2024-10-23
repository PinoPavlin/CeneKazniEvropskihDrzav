import csv
import re
from pridobi_podatke_podstrani import pridobi_kazni_za_drzavo, drzave

# Ime datoteke, kamor bomo shranili podatke
csv_file = "kazni_evropske_drzave_minimum.csv"

# Funkcija za pridobitev minimuma iz kazni
def pridobi_minimum(cena):
    if not cena:
        return "Podatek ni podan"
    try:
        # Preveri, ali obstaja interval (npr. "50 - 150")
        match = re.search(r'(\d+)\s*-\s*(\d+)', cena)
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
    with open(csv_file, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        # Zapis glave tabele
        writer.writerow(['Država', 'Valuta', 'Min kazni za alkohol', 'Min kazni za prehitro vožnjo', 'Min kazni za varnostni pas', 'Min kazni za mobilni telefon'])
        # Zapis podatkov za vsako državo
        for val in podatki:
            writer.writerow([
                val['drzava'], 
                val['valuta'], 
                pridobi_minimum(val['alkohol']),
                pridobi_minimum(val['voznja']),
                pridobi_minimum(val['pas']),
                pridobi_minimum(val['telefon'])
            ])

# Glavna funkcija za pridobitev podatkov in shranjevanje v CSV
def zberi_podatke_in_shrani_minimum():
    vsi_podatki = []

    for drzava in drzave:
        kazni = pridobi_kazni_za_drzavo(drzava)

        if kazni:
            vsi_podatki.append(kazni)

    shrani_v_csv_minimum(vsi_podatki)
    print(f"Podatki uspešno shranjeni v datoteko {csv_file}.")

# Zaženi program
zberi_podatke_in_shrani_minimum()
