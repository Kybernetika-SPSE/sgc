# Studentův průvodce kybernetikou

> Centrální rozcestník pro materiály, maturitní přípravu a aktuální informace k předmětu.

Tento web běží na Docsify a je připravený pro publikaci přes GitHub Pages.

## Co tu najdete

- [Aktuální informace o předmětu](aktualni-informace/) pro oznámení, organizaci a důležité termíny.
- [Seznam maturitních otázek](seznam-maturitnich-otazek/) jako přehled témat k doplnění.
- [MO Jirka](mo-jirka/) pro Jirkovy zpracované maturitní otázky a poznámky.
- [MO Pavel](mo-pavel/) pro Pavlovy materiály a vlastní zpracování.
- [Nová skripta](nova-skripta/) pro budoucí studijní texty a rozsáhlejší materiály.
- [Archiv starých materiálů](archiv/) s importovanými podklady ze starého repozitáře `skripta-kyb`.

## Rozdělení otázek

- Otázky 1 až 12 patří Pavlovi.
- Otázky 13 až 24 patří Jirkovi.
- Každá otázka má vlastní rozcestníkovou stránku s odkazy na převzaté zdroje.

## Jak web používat

1. Vlevo si vyber sekci, která tě zajímá.
2. Postupně doplňuj jednotlivé stránky a odkazy podle potřeby.
3. Pro rychlé hledání použij vyhledávání v horní části sidebaru.

## Wikilinky

- Docsify nemá wikilinky nativně, ale web je teď umí přes vlastní preprocesor v `docs/index.html`.
- Uvnitř `mo-jirka/README.md` lze psát například `[[13-pasivni-elektronicke-prvky|Otázka 13]]`.
- Z jiné sekce lze odkazovat například `[[mo-pavel/01-verzovaci-system-git|Git]]`.
- Pro PDF, ZIP nebo jiné soubory lze používat třeba `[[mo-jirka/assets/soubor.pdf|Soubor PDF]]`.
- Wikilinky se automaticky převádějí na Docsify hash odkazy pro markdown stránky a na běžné odkazy pro ostatní soubory.

## Stav projektu

- Základní struktura je připravena.
- Staré materiály byly importovány do `docs/archiv/skripta-kyb/`.
- Obsah jednotlivých sekcí se bude doplňovat postupně.
- Obrázky jsou nyní uložené v `mo-*/images/` a ostatní soubory patří do `mo-*/assets/`.
- Repo je nastavené tak, aby šlo publikovat z `docs/` na GitHub Pages.

