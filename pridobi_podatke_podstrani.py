import requests
import re
from bs4 import BeautifulSoup

# Seznam držav v slovenščini (delne države, dodaj ostale po potrebi)
drzave = ['slovenija', 'avstrija', 'nemcija', 'italija', 'francija', 'spanija', 'hrvaska', 'danska']

# Osnovni URL za podatke o kaznih po državah
base_url = 'https://www.amzs.si/na-poti/prikaz-prometnih-podatkov-po-evropskih-drzavah/'

# Funkcija za pridobitev kazni iz podstrani posamezne države
def pridobi_kazni_za_drzavo(drzava):
    url = base_url + drzava
    response = requests.get(url)
    
    if response.status_code == 200:
        html_content = response.text
        
        drzava = drzava.capitalize()

        match drzava:
            case "Spanija":
                drzava = "Španija"
            case "Hrvaska":
                drzava = "Hrvaška"
            case "Nemcija":
                drzava = "Nemčija"

        # Uporaba BeautifulSoup za analizo HTML
        soup = BeautifulSoup(html_content, 'html.parser')

        # Iskanje valute
        currency = soup.find(string=re.compile(r'Valuta')).find_next().text.strip()
        
        # Najdi kazni za vožnjo pod vplivom alkohola
        alcohol_fines = soup.find(string=re.compile(r'Vožnja pod vplivom alkohola')).find_next().text.strip()

        # Najdi kazni za prehitro vožnjo v naselju za 20 km/h
        voznja_fines = soup.find(string=re.compile(r'Prehitra vožnja v naselju za 20 km/h')).find_next().text.strip()
        
        # Najdi kazni za neuporabo varnostnega pasu
        seatbelt_fines = soup.find(string=re.compile(r'Neuporaba varnostnega pasu')).find_next().text.strip()

        # Najdi kazni za uporabo mobilnega telefona
        telefon_fines = soup.find(string=re.compile(r'Uporaba mobilnega telefona')).find_next().text.strip()
        
        # Prikaz rezultatov za alkohol
        if alcohol_fines:
            print(f"Kazni za vožnjo pod vplivom alkohola v državi {drzava} (v {currency}):")
            print(f"Kazen: {alcohol_fines}")
        else:
            print(f"Nobenih podatkov o kaznih za alkohol za državo {drzava}.")

        # Prikaz rezultatov za prehitro voznjo
        if voznja_fines:
            print(f"Kazni za prehitro vožnjo v naselju za 20 km/h v državi {drzava} (v {currency}):")
            print(f"Kazen: {voznja_fines}")
        else:
            print(f"Nobenih podatkov o kaznih za prehitro vožnjo v naselju za 20 km/h za državo {drzava}.")
        
        # Prikaz rezultatov za varnostni pas
        if seatbelt_fines:
            print(f"Kazni za neuporabo varnostnega pasu v državi {drzava} (v {currency}):")
            print(f"Kazen: {seatbelt_fines}")
        else:
            print(f"Nobenih podatkov o kaznih za varnostni pas za državo {drzava}.")

        # Prikaz rezultatov za telefon
        if telefon_fines:
            print(f"Kazni za uporabo mobilnega telefona v državi {drzava} (v {currency}):")
            print(f"Kazen: {telefon_fines}")
        else:
            print(f"Nobenih podatkov o kaznih za uporabo mobilnega telefona za državo {drzava}.")
        
    else:
        print(f"Napaka pri dostopu do strani za državo {drzava}: {response.status_code}")

# Pridobi kazni za vse države v seznamu
for drzava in drzave:
    pridobi_kazni_za_drzavo(drzava)
    print("\n" + "-"*50 + "\n")