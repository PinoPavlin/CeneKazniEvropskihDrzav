import requests
import re

# Seznam držav v slovenščini (delne države, dodaj ostale po potrebi)
drzave = ['slovenija', 'avstrija', 'nemcija', 'italija', 'francija', 'spanija']

# Osnovni URL za podatke o kaznih po državah
base_url = 'https://www.amzs.si/na-poti/prikaz-prometnih-podatkov-po-evropskih-drzavah/'

# Regularni izraz za kazen za "Vožnja pod vplivom alkohola"
alcohol_pattern = re.compile(r'Vožnja pod vplivom alkohola.*?(\d+[,\.]?\d*)\s*(\w+)', re.DOTALL)

# Regularni izraz za kazen za "Prehitra vožnja v naselju za 20 km/h"
voznja_pattern = re.compile(r'Prehitra vožnja v naselju za 20 km/h.*?(\d+[,\.]?\d*)\s*(\w+)', re.DOTALL)

# Regularni izraz za kazen za "Neuporaba varnostnega pasu"
seatbelt_pattern = re.compile(r'Neuporaba varnostnega pasu.*?(\d+[,\.]?\d*)\s*(\w+)', re.DOTALL)

# Regularni izraz za kazen za "Uporaba mobilnega telefona"
telefon_pattern = re.compile(r'Uporaba mobilnega telefona.*?(\d+[,\.]?\d*)\s*(\w+)', re.DOTALL)

# Funkcija za pridobitev kazni iz podstrani posamezne države
def pridobi_kazni_za_drzavo(drzava):
    url = base_url + drzava
    response = requests.get(url)
    
    if response.status_code == 200:
        html_content = response.text
        
        # Najdi kazni za vožnjo pod vplivom alkohola
        alcohol_fines = alcohol_pattern.findall(html_content)

        # Najdi kazni za prehitro vožnjo v naselju za 20 km/h
        voznja_fines = voznja_pattern.findall(html_content)
        
        # Najdi kazni za neuporabo varnostnega pasu
        seatbelt_fines = seatbelt_pattern.findall(html_content)

        # Najdi kazni za uporabo mobilnega telefona
        telefon_fines = telefon_pattern.findall(html_content)
        
        # Prikaz rezultatov za alkohol
        if alcohol_fines:
            print(f"Kazni za vožnjo pod vplivom alkohola v državi {drzava.capitalize()}:")
            for fine in alcohol_fines:
                print(f"Kazen: {fine[0]}{fine[1]}")
        else:
            print(f"Nobenih podatkov o kaznih za alkohol za državo {drzava.capitalize()}.")

        # Prikaz rezultatov za prehitro voznjo
        if voznja_fines:
            print(f"Kazni za prehitro vožnjo v naselju za 20 km/h v državi {drzava.capitalize()}:")
            for fine in voznja_fines:
                print(f"Kazen: {fine[0]}{fine[1]}")
        else:
            print(f"Nobenih podatkov o kaznih za prehitro vožnjo v naselju za 20 km/h za državo {drzava.capitalize()}.")
        
        # Prikaz rezultatov za varnostni pas
        if seatbelt_fines:
            print(f"Kazni za neuporabo varnostnega pasu v državi {drzava.capitalize()}:")
            for fine in seatbelt_fines:
                print(f"Kazen: {fine[0]}{fine[1]}")
        else:
            print(f"Nobenih podatkov o kaznih za varnostni pas za državo {drzava.capitalize()}.")

        # Prikaz rezultatov za telefon
        if telefon_fines:
            print(f"Kazni za uporabo mobilnega telefona v državi {drzava.capitalize()}:")
            for fine in telefon_fines:
                print(f"Kazen: {fine[0]}{fine[1]}")
        else:
            print(f"Nobenih podatkov o kaznih za uporabo mobilnega telefona za državo {drzava.capitalize()}.")
        
    else:
        print(f"Napaka pri dostopu do strani za državo {drzava.capitalize()}: {response.status_code}")

# Pridobi kazni za vse države v seznamu
for drzava in drzave:
    pridobi_kazni_za_drzavo(drzava)
    print("\n" + "-"*50 + "\n")