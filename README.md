# Projektna naloga - Cene kazni evropskih držav

_Avtor_: **[Pino Pavlin](https://github.com/PinoPavlin)**

## Uvod in ideja

Na spletni strani [AMZS](https://www.amzs.si/na-poti/Potovalne-informacije-po-evropskih-drzavah) so za evropske države prikazani nekateri podatki o potovalnih informacijah, kot so:

- Vstopni dokumenti
- Prometni predpisi
- Prevoz otrok v vozilu
- Cestnine
- itd.

---

### Osebne želje in odločitev

Osebno me najbolj zanimajo številke, cene in statistika, zato so mi v oči takoj padle različne kazni za posamezne države (zavihek **Prometni predpisi**), kot so:

- **Vožnja pod vplivom alkohola**
- **Prehitra vožnja v naselju za 20 km/h**
- **Neuporaba varnostnega pasu**
- **Uporaba mobilnega telefona**
- itd.

Ob pregledu vseh držav sem ugotovil, da se ravno podatki za te štiri kazni pojavljajo v največ državah, zato sem se odločil, da **_bom v projektni nalogi uporabljal zgolj cene zgoraj-navedenih kazni_**. Upošteval sem tudi dejstvo, da določene države nimajo valute EUR, zato sem poskrbel tudi za to in po [aktualnih menjalnih tečajih](https://www.visaeurope.si/support/consumer/travel-support/exchange-rate-calculator.html) pretvoril cene v EUR (_pri tem sem nastavil bančno pristojbino na 0%_).

## Navodila

Uporabnik mora naložiti knjižnice:

- `requests`
- `re`
- `beautifulsoup4`
- `csv`
- `matplotlib.pyplot`
- `pandas`

## Opis datotek

1. Program [pridobi_podatke_podstrani.py](https://github.com/PinoPavlin/PrviRepozitorij/blob/main/pridobi_podatke_podstrani.py) iz [spletne strani](https://www.amzs.si/na-poti/Potovalne-informacije-po-evropskih-drzavah) pobere podatke za vse naštete države za cene zgoraj-omenjenih kazni.

2. Program [tabela_csv.py](https://github.com/PinoPavlin/PrviRepozitorij/blob/main/tabela_csv.py) vse zbrane podatke iz [pridobi_podatke_podstrani.py](https://github.com/PinoPavlin/PrviRepozitorij/blob/main/pridobi_podatke_podstrani.py) še zapiše v csv datoteko.

3. Program [tabela_csv_minimum.py](https://github.com/PinoPavlin/PrviRepozitorij/blob/main/tabela_csv_minimum.py) v datoteko zapiše zgolj minimalne cene kazni (če obstajajo!).

4. Program [pretvori_v_EUR.py](https://github.com/PinoPavlin/PrviRepozitorij/blob/main/pretvori_v_EUR.py) v datoteko zapiše pretvorjene cene kazni v EUR.

5. Program [grafi.py](https://github.com/PinoPavlin/PrviRepozitorij/blob/main/grafi.py) izriše grafe za vse štiri tipe kazni zgolj za določene države zaradi preglednosti samega grafa.

6. Datoteka [AnalizaPodatkov.ipynb](https://github.com/PinoPavlin/CeneKazniEvropskihDrzav/blob/main/AnalizaPodatkov.ipynb) predstavi vse dobljene podatke in jih prikaže tudi grafično.

## Opozorila !!!

1. V datoteki [kazni_evropske_drzave.csv](https://github.com/PinoPavlin/PrviRepozitorij/blob/main/kazni_evropske_drzave.csv) se lahko opazi **nekaj praznih polj**. To pomeni, da ta podatek za državo na [spletni strani](https://www.amzs.si/na-poti/Potovalne-informacije-po-evropskih-drzavah) ne obstaja!

2. V datotekah [kazni_evropske_drzave_eur.csv](https://github.com/PinoPavlin/PrviRepozitorij/blob/main/kazni_evropske_drzave_eur.csv), [kazni_evropske_drzave_eur_sortirano.csv](https://github.com/PinoPavlin/PrviRepozitorij/blob/main/kazni_evropske_drzave_eur_sortirano.csv) in [kazni_evropske_drzave_minimum.csv](https://github.com/PinoPavlin/PrviRepozitorij/blob/main/kazni_evropske_drzave_minimum.csv) se lahko opazi **nekaj ničel**. To pomeni, da tega podatka za državo na [spletni strani](https://www.amzs.si/na-poti/Potovalne-informacije-po-evropskih-drzavah) ni ali pa podatek ne vsebuje števil (torej je kazen zgolj ubesedena, npr. _odvisno od mesečnega prihodka_)!

3. Zaradi lažje uporabe podatkov in sortiranja se v datotekah [tabela_csv_minimum.py](https://github.com/PinoPavlin/PrviRepozitorij/blob/main/tabela_csv_minimum.py), [pretvori_v_EUR.py](https://github.com/PinoPavlin/PrviRepozitorij/blob/main/pretvori_v_EUR.py) in [grafi.py](https://github.com/PinoPavlin/PrviRepozitorij/blob/main/grafi.py) uporabljajo zgolj minimalne vrednosti kazni za posamezne države (če le te obstajajo!).

4. Shranjevanje v .csv datoteko včasih lahko vzame nekaj sekund več.

5. Nekatere cene kazni se ne ujemajo s cenami, ki jih prikaže "Google". Vsi podatki, ki jih program pobere iz spletne strani in jih pretvori v EUR pa se po [aktualnih menjalnih tečajih](https://www.visaeurope.si/support/consumer/travel-support/exchange-rate-calculator.html) ujemajo s cenami, ki so zapisane na [AMZS spletni strani](https://www.amzs.si/na-poti/Potovalne-informacije-po-evropskih-drzavah), zato je to kvečjemu napaka veljavnosti podatkov na njihovi spletni strani.

6. V .csv datotekah je zaradi preglednosti in efektivnosti v glavi napisano malenkost drugače kot je v originalu napisano na [AMZS spletni strani](https://www.amzs.si/na-poti/Potovalne-informacije-po-evropskih-drzavah), npr.:

- Kazni za alkohol = Vožnja pod vplivom alkohola
- Kazni za prehitro vožnjo = Prehitra vožnja v naselju za 20 km/h
- Kazni za varnostni pas = Neuporaba varnostnega pasu
- Kazni za mobilni telefon = Uporaba mobilnega telefona

7. V datotekah [kazni_evropske_drzave_eur.csv](https://github.com/PinoPavlin/PrviRepozitorij/blob/main/kazni_evropske_drzave_eur.csv) in [kazni_evropske_drzave_eur_sortirano.csv](https://github.com/PinoPavlin/PrviRepozitorij/blob/main/kazni_evropske_drzave_eur_sortirano.csv) je kljub pretvorbi v EUR še vedno zapisana matična valuta države.

8. V datoteki [kazni_evropske_drzave_eur_sortirano.csv](https://github.com/PinoPavlin/PrviRepozitorij/blob/main/kazni_evropske_drzave_eur_sortirano.csv) je sortirano padajoče po ceni kazni za neuporabo varnostnega pasu.
