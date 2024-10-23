import csv
from pridobi_podatke_podstrani import pridobi_kazni_za_drzavo, drzave

# Ime datoteke, kamor bomo shranili podatke
csv_file = "kazni_evropske_drzave.csv"

# Funkcija za zapisovanje podatkov v CSV
def shrani_v_csv(podatki):
    with open(csv_file, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        # Zapis glave tabele
        writer.writerow(['Država', 'Valuta', 'Kazni za alkohol', 'Kazni za prehitro vožnjo', 'Kazni za varnostni pas', 'Kazni za mobilni telefon'])
        print(podatki)
        # Zapis podatkov za vsako državo
        for val in podatki:
            writer.writerow([val['drzava'], val['valuta'], val['alkohol'], val['voznja'], val['pas'], val['telefon']])

# Glavna funkcija za pridobitev podatkov in shranjevanje v CSV
def zberi_podatke_in_shrani():
    vsi_podatki = []

    for drzava in drzave:
        kazni = pridobi_kazni_za_drzavo(drzava)

        if kazni:
            vsi_podatki.append(kazni)

    shrani_v_csv(vsi_podatki)
    print(f"Podatki uspešno shranjeni v datoteko {csv_file}.")

# Zaženi program
zberi_podatke_in_shrani()