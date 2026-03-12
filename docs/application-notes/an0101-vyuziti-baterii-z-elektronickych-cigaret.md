# AN0101 - Využití baterií z elektronických cigaret

> Vytvořeno pomocí AI (GPT-5.4)

> Aplikační list popisuje možnosti opětovného využití Li-ion článků získaných z elektronických cigaret, jejich omezení a zásady bezpečného návrhu.

## Cíl dokumentu

Cílem tohoto aplikačního listu je shrnout, kdy dává smysl použít článek z elektronické cigarety v dalším projektu a kdy je naopak bezpečnější jej vůbec nenasazovat. Dokument je určen hlavně pro školní projekty, jednoduché přenosné přístroje a laboratorní prototypy s malým až středním odběrem proudu.

## Co jsou to za články

V jednorázových i opakovaně použitelných elektronických cigaretách se nejčastěji nachází jeden Li-ion nebo Li-pol článek s jmenovitým napětím `3,7 V`.

Typické vlastnosti:

- plně nabitý článek má přibližně `4,2 V`
- za bezpečné minimum se obvykle považuje přibližně `3,0 V`
- kapacita bývá řádově `300 až 1000 mAh`, podle velikosti zařízení
- některé články mají vestavěnou ochranu, jiné jsou zcela bez ní
- často chybí přesný datasheet i spolehlivé značení výrobce

Z praktického hlediska je největší problém v tom, že parametry bývají neznámé nebo neověřené. Proto je potřeba ke každému získanému článku přistupovat konzervativně.

## Kdy má článek smysl znovu použít

Použití je rozumné jen tehdy, pokud jsou splněny všechny následující podmínky:

- článek není mechanicky poškozený, nafouklý ani zkorodovaný
- napětí na svorkách není extrémně nízké
- při nabíjení se článek nepřehřívá
- je možné doplnit ochranný a nabíjecí obvod
- cílová aplikace nemá vysoké proudové špičky

Vhodné aplikace:

- jednoduché měřicí přístroje
- přenosné senzory s mikrokontrolerem
- dataloggery
- malé IoT uzly
- LED osvětlení s omezeným proudem
- laboratorní demonstrátory napájení

Nevhodné aplikace:

- zařízení bez ochrany proti přebití a podvybití
- modelářské pohony a jiné aplikace s vysokým proudem
- zařízení ponechaná bez dozoru během nabíjení
- produkty pro dlouhodobý provoz v teple nebo na slunci
- cokoliv, kde by porucha mohla ohrozit zdraví nebo majetek

## Identifikace a prvotní kontrola

Před použitím článku je vhodné provést základní kontrolu.

1. Změřit napětí naprázdno.
2. Zkontrolovat stav obalu, vývodů a případné známky nafouknutí.
3. Ověřit, zda článek není po pádu, propíchnutí nebo přehřátí.
4. Zjistit, zda je přítomna ochranná elektronika.

Orientační vyhodnocení napětí:

- `4,0 až 4,2 V`: článek je pravděpodobně čerstvě nabitý
- `3,4 až 3,9 V`: běžný skladovací nebo provozní stav
- `3,0 až 3,3 V`: opatrně, článek je téměř vybitý
- pod `3,0 V`: pro školní použití raději nevyužívat

Pokud není známá historie článku, je vhodnější jej použít jen pro nenáročné testovací účely, případně jej ekologicky zlikvidovat.

## Doporučené zapojení

Samotný článek se nikdy nemá připojovat přímo k zátěži bez dalších obvodů. Minimální doporučená struktura je:

`Li-ion článek -> ochrana -> nabíjecí obvod -> měnič nebo zátěž`

Prakticky to znamená:

- ochrana proti přebití
- ochrana proti hlubokému vybití
- omezení nabíjecího proudu
- ochrana proti zkratu
- podle potřeby step-up nebo step-down měnič

Ve školních projektech se často používá kombinace modulů s obvodem `TP4056` a ochranným čipem. I v tomto případě je ale nutné ověřit maximální proud a zahřívání.

## Nabíjení

Li-ion článek se nabíjí metodou `CC/CV`, tedy nejprve konstantním proudem a potom konstantním napětím.

Zásady:

- koncové napětí je typicky `4,2 V`
- nabíjecí proud musí odpovídat kapacitě a stavu článku
- při neznámé kapacitě je vhodné volit spíše menší proud
- článek nesmí být během nabíjení bez dozoru v rizikovém prostředí

Pro laboratorní a školní nasazení je rozumné držet se nižších proudů, protože tím klesá tepelné namáhání i riziko poruchy.

## Napájení cílových obvodů

Napětí článku se během vybíjení mění přibližně od `4,2 V` do `3,0 V`, což je potřeba zahrnout do návrhu.

Příklady:

- pro `3,3 V` mikrokontroler je vhodný stabilizátor s malým úbytkem nebo buck-boost měnič
- pro `5 V` zařízení je nutný step-up měnič
- pro LED aplikace je vhodné použít proudový driver nebo alespoň proudové omezení

Při návrhu je potřeba počítat s tím, že skutečná využitelná kapacita staršího článku bude nižší než nominální hodnota.

## Odhad výdrže

Přibližná doba provozu se dá odhadnout vztahem:

```text
t = C / I
```

kde:

- `t` je doba provozu v hodinách
- `C` je kapacita článku v `Ah`
- `I` je průměrný odběr proudu v `A`

Příklad:

Má-li článek kapacitu `0,65 Ah` a zařízení odebírá průměrně `0,13 A`, pak:

```text
t = 0,65 / 0,13 = 5 h
```

V praxi bude výdrž menší kvůli ztrátám v měniči, stárnutí článku a rezervě proti hlubokému vybití.

## Příklad vhodné aplikace

Jednoduchý bezdrátový senzor může být napájen takto:

1. Li-ion článek z elektronické cigarety.
2. Nabíjecí modul s ochranou.
3. Stabilizace na `3,3 V`.
4. Mikrokontroler s režimem spánku.
5. Senzor teploty nebo vlhkosti.

Takové řešení je vhodné jen tehdy, pokud zařízení odebírá malý proud a pokud lze bezpečně zajistit nabíjení mimo hořlavé prostředí.

## Hlavní rizika

Při nesprávném použití může dojít k:

- přehřátí článku
- úniku elektrolytu
- nafouknutí obalu
- požáru při zkratu nebo přebití
- poškození připojené elektroniky nestabilním napětím

Zvláštní pozornost je potřeba věnovat článkům bez známého původu. U levných jednorázových zařízení bývá kvalita i reálná kapacita velmi proměnlivá.

## Doporučení pro školní praxi

- používat článek jen v prototypu, ne ve finálním výrobku
- doplnit ochranný obvod a vhodnou pojistku
- mechanicky zajistit článek proti promáčknutí a vibracím
- pravidelně kontrolovat zahřívání při provozu i nabíjení
- neukládat plně nabité články dlouhodobě bez kontroly
- podezřelé nebo poškozené články okamžitě vyřadit

## Závěr

Baterie z elektronických cigaret lze v některých případech využít jako levný zdroj energie pro malé přenosné projekty. Jejich opětovné použití však dává smysl pouze tehdy, pokud je článek v dobrém stavu, aplikace má nízké nároky na proud a návrh obsahuje kompletní ochranu i správné nabíjení. Pokud není znám původ článku nebo nelze zajistit bezpečný provoz, je vhodnější zvolit nový článek s datasheetem.