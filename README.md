# PrviRepozitorij

_Avtor_: **[https://github.com/PinoPavlin](Pino Pavlin)**

## Uvod

Na spletni strani [https://www.amzs.si/na-poti/Potovalne-informacije-po-evropskih-drzavah](AMZS) so za evropske države prikazani nekateri podatki o potovalnih informacijah, kot so:

- Vstopni dokumenti
- Prometni predpisi
- Prevoz otrok v vozilu
- Cestnine
- itd.

---

Osebno me najbolj zanimajo številke, cene in statistika, zato so mi v oči takoj padle različne kazni za posamezne države (zavihek Prometni predpisi), kot so:

- **Vožnja pod vplivom alkohola**
- **Prehitra vožnja v naselju za 20 km/h**
- **Neuporaba varnostnega pasu**
- **Uporaba mobilnega telefona**
- itd.

---

Ob pregledu vseh držav sem ugotovil, da se ravno podatki za te štiri kazni pojavljajo v največ državah, zato sem se odločil, da **_bom v projektni nalogi uporabljal zgolj cene zgoraj-navedenih kazni_**. Upošteval sem tudi dejstvo, da določene države nimajo valute EUR, zato sem poskrbel tudi za to in po [https://www.visaeurope.si/support/consumer/travel-support/exchange-rate-calculator.html](aktualnih menjalnih tečajih) pretvoril cene v EUR (_pri tem sem nastavil bančno pristojbino na 0%_).

## Navodila

Uporabnik mora naložiti knjižnice:

- `requests`
- `re`
- `beautifulsoup4`
- `csv`
- `matplotlib.pyplot`

## Opis datotek

1. Program [https://github.com/PinoPavlin/PrviRepozitorij/blob/main/pridobi_podatke_podstrani.py](pridobi_podatke_podstrani.py) iz [https://www.amzs.si/na-poti/Potovalne-informacije-po-evropskih-drzavah](spletne strani) pobere podatke za vse naštete države za cene zgoraj-omenjenih kazni.

2. Program [https://github.com/PinoPavlin/PrviRepozitorij/blob/main/tabela_csv.py](tabela_csv.py) vse zbrane podatke iz [https://github.com/PinoPavlin/PrviRepozitorij/blob/main/pridobi_podatke_podstrani.py](pridobi_podatke_podstrani.py) še zapiše v csv datoteko.

3. Program [https://github.com/PinoPavlin/PrviRepozitorij/blob/main/tabela_csv_minimum.py](tabela_csv_minimum.py) v datoteko zapiše zgolj minimalne cene kazni (če obstajajo!).

4. Program [https://github.com/PinoPavlin/PrviRepozitorij/blob/main/pretvori_v_EUR.py](pretvori_v_EUR.py) v datoteko zapiše pretvorjene cene kazni v EUR.

5. Program [https://github.com/PinoPavlin/PrviRepozitorij/blob/main/grafi.py](grafi.py) izriše grafe za vse štiri tipe kazni zgolj za določene kazni zaradi preglednosti samega grafa.

## Opozorila

1. V datoteki [https://github.com/PinoPavlin/PrviRepozitorij/blob/main/kazni_evropske_drzave.csv](kazni_evropske_drzave.csv) se lahko opazi **nekaj praznih polj**. To pomeni, da ta podatek za državo na [https://www.amzs.si/na-poti/Potovalne-informacije-po-evropskih-drzavah](spletni strani) ne obstaja!

2. V datotekah [https://github.com/PinoPavlin/PrviRepozitorij/blob/main/kazni_evropske_drzave_eur.csv](kazni_evropske_drzave_eur.csv), [https://github.com/PinoPavlin/PrviRepozitorij/blob/main/kazni_evropske_drzave_eur_sortirano.csv](kazni_evropske_drzave_eur_sortirano.csv) in [https://github.com/PinoPavlin/PrviRepozitorij/blob/main/kazni_evropske_drzave_minimum.csv](kazni_evropske_drzave_minimum.csv) se lahko opazi **nekaj ničel**. To pomeni, da tega podatka za državo na [https://www.amzs.si/na-poti/Potovalne-informacije-po-evropskih-drzavah](spletni strani) ni ali pa podatek ne vsebuje števil (torej je kazen zgolj ubesedena, npr. _odvisno od mesečnega prihodka_)!

3. Zaradi lažje uporabe podatkov in sortiranja se v datotekah [https://github.com/PinoPavlin/PrviRepozitorij/blob/main/tabela_csv_minimum.py](tabela_csv_minimum.py), [https://github.com/PinoPavlin/PrviRepozitorij/blob/main/pretvori_v_EUR.py](pretvori_v_EUR.py) in [https://github.com/PinoPavlin/PrviRepozitorij/blob/main/grafi.py](grafi.py) uporabljajo zgolj minimalne vrednosti kazni za posamezne države (če le te obstajajo!).

4. Shranjevanje v .csv datoteko včasih lahko vzame nekaj sekund več.

5. Nekatere cene kazni se ne ujemajo s cenami, ki jih prikaže "Google". Vsi podatki, ki jih program pobere iz spletne strani in jih pretvori v EUR pa se po aktualnih menjalnih tečajih ujemajo s cenami, ki so zapisane na [https://www.amzs.si/na-poti/Potovalne-informacije-po-evropskih-drzavah](AMZS spletni strani), zato je to kvečjemu napaka veljavnosti podatkov na njihovi spletni strani.
