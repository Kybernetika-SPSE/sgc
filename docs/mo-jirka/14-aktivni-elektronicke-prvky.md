# Otázka 14

## Aktivní elektronické prvky

- správce: Jirka
- stav: převedeno z archivu do nové stránky
- původní zdroj: [14. Aktivní elektronické prvky](../archiv/skripta-kyb/kybernetika/chapters/14.%20Aktivní%20elektronické%20prvky.md)

---

# Aktivní součástky
- jsou elektronické součástky schopné zesilovat signál
- polovodičové nebo vakuové ( a elektromechanické relé)

---
# Elektromechanické relé
- elektromagnet (=cívka z drátu na kovovém jádře), který přitahuje tzv. kotvu a tím přepíná kontakty
![](images/14-elektromechanicke-rele.png)

---
# Polovodičové aktivní součástky
- využívají vlastností přechodů polovodičových materiálů **P** a **N**
- z **germánia** (už se moc nepoužívá, ale má nižší prahové napětí(citlivější)) nebo **křemíku**, (nebo **GaN** - výkonová elektronika)

## Dioda
- technicky není aktivní součástka, ale je polovodičová
- tzv. dvouvrstvá polovodičová součástka - `PN`
- propouští proud jen jedním směrem
- má anodu a katodu (proud teče z anody do katody)
- **Zenerova** - zapojuje se v závěrném směru (katoda na plus), při překročení určitého napětí začíná vodit, tudíž se používá jako regulátor
- **Shottkyho** - rychlá, nízký úbytek napětí
- **LED** - svítí, vyšší úbytek napětí (potřebuje energii na svícení)
- **Fotodioda** - mění vodivost v závislosti na osvětlení
- **Varikap** - mění svojí kapacitu v závislosti na napětí - využívá se v ladicích obvodech (LC obvod)
- atd.
![](images/14-dioda.png)

## Diak
- třívrstvý - dva druhy - `PNP`/`NPN`
- jako Zenerova dioda ale pro střídavý proud
![](images/14-diak.png)

## Transistor
- třívrstvá polovodičová součástka
- více druhů - výkonové, vysokofrekvenční, spínací atd.
- **Bipolární** - ( BJT - bipolar junction transistor ) - dva druhy - `PNP`/`NPN`
	- má **bázi**, **kolektor** a **emitor**
	- malý proud na bázi ovládá velký proud procházející z kolektoru na emitor (`NPN`) / z emitoru na kolektor (`PNP`)
	- proudový zesilovací činitel - určuje zesílení - poměr proudu báze a emitoru
	- Darlingtonovo zapojení - zapojení dvou tranzistorů → velké zesílení
- **Unipolární** - (FET - field effect transistor) - dva druhy - `N-channel`/`P-channel` (podobné rozdíly jako u NPN/PNP (negativní vs pozitivní signál na řídící elektrodě))
	- má **Gate** (řídící elektroda), **Drain** a **Source**
	- Gate má velkou vstupní impedanci
	- řízen elektrickým polem (napětím) místo proudu
	- více druhů - `JFET`, `MOSFET` atd. -liší se technologií výroby a některými vlastnostmi
![](images/14-tranzistor-bi-a-uni-polarni.png)
![](images/14-tranzistor-unipolarni.png)

## Tyristor
- čtyřvrstvá polovodičová součástka - `PNPN`
- spínání, převážně větších výkonů (mašinky UwU)
- má **Gate** (řídící elektroda), **anodu** a **katodu**
- signálem na řídící elektrodě sepne (proud prochází z anody do katody)
- dokud prochází anodový proud, je tyristor sepnut (i bez napětí na Gate)
- funguje binárně (sepnuto/rozepnuto), na rozdíl od tranzistoru (zesiluje analogový signál)
![](images/14-tyristor.png)






