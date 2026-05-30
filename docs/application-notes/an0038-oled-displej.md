# AN0038 - OLED displej úvod

> Částečně vytvořeno pomocí AI (Gemini 3.5)

> Aplikační list popisuje možnosti využití malých OLED displejů ve školních elektronických projektech, jejich technická omezení a zásady bezpečného návrhu z hlediska napájení i paměti mikrokontroléru.

## Cíl dokumentu

Cílem tohoto aplikačního listu je shrnout, kdy dává smysl použít malý OLED displej v projektu a na co si dát při jeho nasazení pozor. Dokument je určen hlavně pro školní projekty, jednoduché přenosné přístroje, IoT uzly a laboratorní prototypy řízené mikrokontrolery, jako jsou Arduino, ESP32 nebo STM32.

## Co jsou to za displeje

V současné praxi se nejčastěji setkáte s miniaturními monochromatickými displeji technologie OLED (Organic Light-Emitting Diode), kde každý pixel tvoří samostatná svítivá dioda. Nepotřebují tedy podsvícení.

> Typické vlastnosti:

- Běžné úhlopříčky jsou 0,91", 0,96" nebo 1,3"

- Typické rozlišení bývá 128x64 nebo 128x32 pixelů

- Barva svitu je nejčastěji bílá, modrá nebo rozdělená (horní čtvrtina žlutá, zbytek modrý)

- Komunikace probíhá po sběrnici I2C (4 piny) nebo SPI (6-7 pinů)

- Nejčastější řídicí čipy uvnitř displeje jsou SSD1306 nebo SH1106

Z praktického hlediska je největší výhodou vysoký kontrast a výborné pozorovací úhly, nevýhodou naopak mechanická křehkost a riziko vypalování pixelů při dlouhodobém statickém zobrazení.

## Kdy má displej smysl použít

Použití je rozumné tam, kde potřebujete zobrazovat text nebo jednoduchou grafiku, a zároveň máte omezený prostor či rozpočet na napájení.

> Vhodné aplikace:

- Přenosné senzory teploty, tlaku a vlhkosti

- Menu a uživatelské rozhraní malých přístrojů

- Nositelná elektronika (wearables) a chytré hodinky

- Stavy a diagnostika u IoT uzlů (IP adresa, síla Wi-Fi)

- Zobrazení hodnot v laboratorních demonstrátorech

## Prvotní kontrola

Před zapojením zakoupeného nebo získaného OLED modulu je nutné prověřit několik klíčových vlastností.

- Zjistit z potisku DPS typ komunikačního rozhraní (I2C vs. SPI).

- Identifikovat rozložení napájecích pinů (pozor, některé moduly mají na kraji GND a hned vedle VCC, jiné to mají naopak).

- Ověřit, zda je na zadní straně desky osazen malý stabilizátor napětí, což určuje toleranci k napájení.

- U I2C displejů zjistit hardwarovou adresu (typicky 0x3C nebo 0x3D).

- Ověření logických úrovní (většina čipů v displejích je interně na 3,3 V)

## Doporučené zapojení

Standardní zapojení displeje s I2C sběrnicí vyžaduje připojení čtyř vodičů. Sběrnice vyžaduje pull-up rezistory, které však bývají na modulech displejů často již osazeny z výroby.

Mikrokontroler -> Sběrnice (I2C/SPI) -> OLED Modul

Prakticky to znamená připojit:

- GND na společnou zem

- VCC na napájecí napětí (3,3 V nebo 5 V dle modulu)

- SDA na datový pin I2C

- SCL na hodinový pin I2C

V případě SPI displejů přibývají piny pro MOSI, CLK, CS (Chip Select), DC (Data/Command) a RES (Reset). Zapojení je složitější, ale překreslování obrazovky je podstatně rychlejší.

## Komunikace a řízení

Pro řízení displeje se ve školní praxi nepíše ovladač od nuly, ale využívají se hotové knihovny, které řeší inicializační sekvence a posílání grafických dat.

> Zásady:

- Knihovny jako Adafruit_SSD1306 nebo U8g2 jsou průmyslovým standardem v prostředí Arduino

- Displej nemá vlastní znakovou sadu v ROM, překreslování písmen i grafiky řídí výhradně mikrokontroler

- Po zapnutí napájení je displej plný náhodného "zrnění", je nutné jej softwarově vymazat funkcí clearDisplay()

- Obraz se typicky nejprve připraví v paměti RAM (buffer) a poté se celistvě odešle na displej příkazem (např. display() )

## Napájení a spotřeba

OLED technologie se vyznačuje tím, že neexistuje žádné globální podsvícení. Spotřeba proudu je tedy přímo úměrná počtu rozsvícených pixelů a nastavenému jasu.

> Příklady spotřeby (0,96", napájení 3,3 V):

- Zhasnutý displej (režim spánku): jednotky uA

- Displej svítí černě (všechny pixely off, ale displej je aktivní): cca 1 až 2 mA

- Běžný text a sem tam ikona: cca 10 až 15 mA

- Plně rozsvícený displej (všechny pixely on na max. jas): může přesáhnout 30 až 40 mA

Při návrhu bateriového napájení je nutné počítat s průměrnou spotřebou kolem 20 mA a ideálně displej softwarově vypínat, pokud uživatel se zařízením zrovna nepracuje.

## Odhad paměťové náročnosti

Aby bylo možné obraz snadno překreslovat, vyhrazuje si grafická knihovna v paměti RAM mikrokontroléru tzv. frame buffer. Paměťovou náročnost lze odhadnout vztahem:

    RAM = (Š * V) / 8

kde:

- RAM je potřebná paměť v bajtech

- Š je šířka displeje v pixelech

- V je výška displeje v pixelech

- Dělí se 8, protože jeden pixel zabírá v monochromatickém režimu přesně 1 bit (8 bitů = 1 bajt).

Příklad:
Máme-li běžný displej s rozlišením 128x64 pixelů, pak:
    
    RAM = (128 * 64) / 8 = 1024 B = 1 kB

V praxi to znamená, že např. Arduino Uno, které má pouze 2 kB RAM, spotřebuje polovinu veškeré dostupné paměti jen pro udržení obrazu. U složitějších programů může dojít k pádu softwaru.


## Příklad vhodné aplikace

Jednoduchá interaktivní jmenovka nebo meteostanice:

1. Mikrokontroler ESP8266 připojený k Wi-Fi.
2. Stažení přesného času z NTP serveru a dat z lokálního senzoru teploty.
3. OLED displej na I2C sběrnici zobrazující čas a teplotu.
4. Kód odesílá data na displej pouze tehdy, dojde-li ke změně minuty.
5. Každou hodinu se barvy obrazu na displeji prohodí, aby se předešlo vypálení čísel do matrice.

## Hlavní rizika

Při nesprávném použití může dojít k:

- Nevratnému zničení řídicího čipu v důsledku přepólování (OLED moduly většinou nemají ochranu)

- Poškození modulu při aplikaci 5 V logiky na čistě 3,3 V piny

- Mechanickému prasknutí skleněného panelu displeje při nešetrné manipulaci nebo špatném návrhu 3D tisknuté krabičky

- Může dojít k effektu "burn-in"
## Doporučení pro školní praxi
- Ověřte rozložení napájecích pinů těsně před zapojením nepájivého pole, mezi výrobci neexistuje jeden standard
- Při potížích s nedostatkem RAM zvažte nasazení textových knihoven (nepoužívají frame buffer) nebo použijte displej 128x32 (vyžaduje poloviční RAM)
- Omezujte jas na nejnižší čitelnou úroveň (šetří to proud i samotný displej)
- Zaveďte funkci automatického vypnutí obrazu po několika sekundách od datovýho vstupu uživatele.
- Pamatujte, že I2C adresa může kolidovat s jinými moduly na stejné sběrnici (např. s některými senzory tlaku)
- doplnit ochranný obvod a vhodnou pojistku
- mechanicky zajistit článek proti promáčknutí a vibracím

## Závěr
OLED displeje patří k nejoblíbenějším výstupním periferiím pro začínající kybernetiky díky svému vynikajícímu kontrastu a nízké ceně. Jejich nasazení je velmi snadné za předpokladu, že mikrokontroler disponuje dostatkem paměti RAM a vývojář respektuje nutnost předejít statickému "vypálení" obrazu.

