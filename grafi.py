import matplotlib.pyplot as plt

# Podatki za izris (te vrednosti lahko prilagodite)
podatki = {
    'drzava':   ['Slovenija', 'Avstrija', 'Hrvaška', 'Italija', 'Madžarska', 'Monako', 'Nemčija', 'Španija'],
    'alkohol':  [300,           300,        90,         532,        200,        200,    500,        500],
    'voznja':   [120,           35,         130,        169,        60,         45,     30,         100],
    'pas':      [120,           35,         130,        80,         20,         22.5,   30,         200],
    'telefon':  [250,           50,         130,        161,        30,         22.5,   100,        200]
}

# Metoda za izris kazni zaradi alkohola
def graf_alkohol():
    plt.figure(figsize=(10, 6))
    plt.barh(podatki['drzava'], podatki['alkohol'], color='salmon')
    plt.title('Kazni za vožnjo pod vplivom alkohola po državah')
    plt.xlabel('Države')
    plt.ylabel('Kazni (EUR)')
    plt.show()

graf_alkohol()

# Metoda za izris kazni zaradi prehitre vožnje
def graf_voznja():
    plt.figure(figsize=(10, 6))
    plt.barh(podatki['drzava'], podatki['voznja'], color='skyblue')
    plt.title('Kazni za prehitro vožnjo po državah')
    plt.xlabel('Države')
    plt.ylabel('Kazni (EUR)')
    plt.show()

graf_voznja()

# Metoda za izris kazni zaradi neuporabe varnostnega pasu
def graf_pasu():
    plt.figure(figsize=(10, 6))
    plt.barh(podatki['drzava'], podatki['pas'], color='lightgreen')
    plt.title('Kazni za neuporabo varnostnega pasu po državah')
    plt.xlabel('Države')
    plt.ylabel('Kazni (EUR)')
    plt.show()

graf_pasu()

# Metoda za izris kazni zaradi uporabe mobilnega telefona
def graf_telefon():
    plt.figure(figsize=(10, 6))
    plt.barh(podatki['drzava'], podatki['telefon'], color='orchid')
    plt.title('Kazni za uporabo mobilnega telefona po državah')
    plt.xlabel('Države')
    plt.ylabel('Kazni (EUR)')
    plt.show()

graf_telefon()