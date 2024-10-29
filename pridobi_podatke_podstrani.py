import requests
import re
from bs4 import BeautifulSoup

# Seznam držav v slovenščini
drzave = ['albanija', 'andora', 'avstrija', 'belgija', 'belorusija', 'bih', 'bolgarija',
          'ceska', 'crna-gora', 'danska', 'estonija', 'finska', 'francija', 'gibraltar',
          'grcija', 'hrvaska', 'irska', 'islandija', 'italija', 'kosovo', 'latvija',
          'liechtenstein', 'litva', 'luksemburg', 'madzarska', 'malta', 'moldavija',
          'monako', 'nemcija', 'nizozemska', 'norveska', 'poljska', 'portugalska',
          'romunija', 'rusija', 'severna-makedonija', 'slovaska', 'slovenija', 'spanija',
          'srbija', 'svedska', 'svica', 'turcija', 'ukrajina', 'v-britanija']

# Osnovni URL za podatke o kaznih po državah
osnovni_url = 'https://www.amzs.si/na-poti/prikaz-prometnih-podatkov-po-evropskih-drzavah/'

# Funkcija za pridobitev kazni iz podstrani posamezne države
def pridobi_kazni_za_drzavo(drzava):
    url = osnovni_url + drzava
    response = requests.get(url)
    
    if response.status_code == 200:
        html = response.text
        
        drzava = drzava.capitalize()

        match drzava:
            case "Bih":
                drzava = "BIH"
            case "Ceska":
                drzava = "Češka"
            case "Crna-gora":
                drzava = "Črna Gora"
            case "Grcija":
                drzava = "Grčija"
            case "Hrvaska":
                drzava = "Hrvaška"
            case "Madzarska":
                drzava = "Madžarska"
            case "Nemcija":
                drzava = "Nemčija"
            case "Norveska":
                drzava = "Norveška"
            case "Severna-makedonija":
                drzava = "Severna Makedonija"
            case "Slovaska":
                drzava = "Slovaška"
            case "Spanija":
                drzava = "Španija"
            case "Svedska":
                drzava = "Švedska"
            case "Svica":
                drzava = "Švica"
            case "Turcija":
                drzava = "Turčija"
            case "V-britanija":
                drzava = "V. Britanija"

        # Uporaba BeautifulSoup za analizo HTML
        soup = BeautifulSoup(html, 'html.parser')

        # Iskanje valute
        valuta = soup.find(string=re.compile(r'Valuta')).find_next().text.strip()
        
        # Najdi kazni za vožnjo pod vplivom alkohola
        alkohol = soup.find(string=re.compile(r'Vožnja pod vplivom alkohola'))
        if alkohol:
            alkohol = alkohol.find_next().text.strip()

        # Najdi kazni za prehitro vožnjo v naselju za 20 km/h
        voznja = soup.find(string=re.compile(r'Prehitra vožnja v naselju za 20 km/h'))
        if voznja:
            voznja = voznja.find_next().text.strip()
        
        # Najdi kazni za neuporabo varnostnega pasu
        pas = soup.find(string=re.compile(r'Neuporaba varnostnega pasu'))
        if pas:
            pas = pas.find_next().text.strip()

        # Najdi kazni za uporabo mobilnega telefona
        telefon = soup.find(string=re.compile(r'Uporaba mobilnega telefona'))
        if telefon:
            telefon = telefon.find_next().text.strip()

        # Vrnitev podatkov kot slovar
        return {
            'drzava': drzava,
            'valuta': valuta,
            'alkohol': alkohol,
            'voznja': voznja,
            'pas': pas,
            'telefon': telefon
        }
    else:
        print(f"Napaka pri dostopu do strani za državo {drzava}: {response.status_code}")
        return None

# Pridobi kazni za vse države v seznamu
# for drzava in drzave:
#    print(pridobi_kazni_za_drzavo(drzava))
#    print("\n" + "-"*50 + "\n")