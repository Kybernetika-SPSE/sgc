# Studentův průvodce kybernetikou

> Zdroj všeho vědění pro aktuálně vyučovanou kybernetiku na VOŠ a SPŠE.


## Co tu najdete

- [Info](/informace/) - termíny, organizace, jak na Markdown, atd.
- [Seznam maturitních otázek](/seznam-maturitnich-otazek/) - z toho vás budeme zkoušet ať chcete nebo ne :)
- [MO Pavel](/mo-pavel/) - materiály pro KYB orientovanou část otázek
- [MO Jirka](/mo-jirka/) - materiály pro ELE orientovanou část otázek
- [Nová skripta](/nova-skripta/) pro budoucí studijní texty a rozsáhlejší materiály.
- [Archiv starých materiálů](/archiv/) s importovanými podklady ze starého repozitáře `skripta-kyb`.

## Jak web používat

1. Vlevo si vyber sekci, která tě zajímá.
2. Postupně procházej jednotlivé stránky a studuj materiály.
3. Pro rychlé hledání použij vyhledávání v horní části sidebaru.
4. Pro noční studium můžeš přepnout na tmavý režim v nastavení (ikona vpravo dole).

## Jak přispět
- Pokud máš nějaké materiály, které bys chtěl přidat, nebo chceš pomoci s úpravami, vytvoř si fork repozitáře a pošli pull request.

## Odkazy v Markdown

- Docsify používá standardní Markdown odkazy `[text](cesta)`.
- **Relativní cesta** (`file.md`, `assets/note.pdf`) - relativní k aktuálnímu souboru
- **Absolutní cesta** (`/mo-jirka/file.md`, `/assets/note.pdf`) - relativní ke kořenu `docs/`
- Příklady:
  - Uvnitř `mo-jirka/README.md` lze psát `[Otázka 13](13-pasivni-elektronicke-prvky.md)`
  - Z jiné sekce odkazovat `[Git](mo-pavel/01-verzovaci-system-git.md)`
  - Pro PDF soubor `[Návod](assets/soubor.pdf)` nebo absolutně `[Návod](/mo-jirka/assets/soubor.pdf)`

## Stav projektu

- Základní struktura je připravena.
- Staré materiály byly importovány do `docs/archiv/skripta-kyb/`.
- Obsah jednotlivých sekcí se bude doplňovat postupně.
- Obrázky jsou nyní uložené v `mo-*/images/` a ostatní soubory patří do `mo-*/assets/`.
- Repo je nastavené tak, aby šlo publikovat z `docs/` na GitHub Pages.

