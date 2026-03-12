# Markdown cheat sheet

Stručný přehled nejběžnějších Markdown zápisů pro tvorbu materiálů v tomto repozitáři.

## Nadpisy

```md
# Nadpis 1
## Nadpis 2
### Nadpis 3
```

## Odstavce a zalomení

- Prázdný řádek oddělí odstavce.
- Pro nový řádek uvnitř odstavce nech na konci řádku dvě mezery.

```md
První odstavec.

Druhý odstavec.
```

## Zvýraznění textu

```md
**tučně**
*kurzíva*
`kód nebo příkaz`
```

Výsledek: **tučně**, *kurzíva*, `kód nebo příkaz`

## Seznamy

### Odrážkový seznam

```md
- první položka
- druhá položka
- třetí položka
```

### Číslovaný seznam

```md
1. první krok
2. druhý krok
3. třetí krok
```

## Odkazy a obrázky

```md
[Odkaz na Google](https://www.google.com)
![Popis obrázku](../mo-jirka/images/priklad.png)
```

## Citace

```md
> Toto je důležitá poznámka.
```

> Toto je důležitá poznámka.

## Blok kódu

Použij tři zpětné apostrofy. Za otevírací můžeš napsat jazyk kvůli zvýraznění syntaxe.

````md
```py
for i in range(3):
	print(i)
```
````

## Tabulky

```md
| Sloupec | Hodnota |
| --- | --- |
| Napětí | 5 V |
| Proud | 2 A |
```

| Sloupec | Hodnota |
| --- | --- |
| Napětí | 5 V |
| Proud | 2 A |

## Vodorovná čára

```md
---
```

---

# Na co si dát pozor v tomto systému (Docsify)

Tento web nepoužívá klasické generování statických HTML stránek. Markdown soubory načítá až prohlížeč přes Docsify, takže některé věci je dobré psát trochu jinak.

## 1. Odkazy piš relativně nebo absolutně

- **Relativní odkaz** - relativní k aktuálnímu souboru:
  - V rámci jedné složky: `[Další téma](dalsi-soubor.md)`
  - Při přechodu o úroveň výš: `[Zpět](../README.md)`
  - Odkazy na jiné sekce: `[MO Pavel](../mo-pavel/README.md)`
  
- **Absolutní odkaz** - relativní ke kořenu `docs/`:
  - Začíná lomítkem: `[MO Pavel](/mo-pavel/README.md)`
  - Pro PDF: `[Soubor](/mo-jirka/assets/soubor.pdf)`

Příklady z `informace/`:
```md
[Otázka 13](../mo-jirka/13-pasivni-elektronicke-prvky.md)
[Git](../mo-pavel/01-verzovaci-system-git.md)
[Soubor PDF](../mo-jirka/assets/soubor.pdf)
```

## 2. Cesty k obrázkům a souborům musí sedět na umístění souboru

- Obrázky vkládej relativně ke konkrétní stránce.
- Pro materiály v `mo-jirka/` a `mo-pavel/` patří obrázky obvykle do `images/` a ostatní soubory do `assets/`.
- Když se obrázek nezobrazí, bývá nejčastěji špatně relativní cesta.

Příklad:

```md
![Schema](images/schema-zapojeni.png)
[Zadani v PDF](assets/zadani.pdf)
```

## 3. Používej běžný Markdown, ne HTML, pokud to není nutné

- Docsify Markdown umí dobře.
- Jednodušší zápis se líp upravuje a méně se kazí při přesunech stránek.
- HTML použij jen když Markdown nestačí.

## 4. Matematika jde psát v LaTeXu

Web má načtený MathJax, takže lze použít třeba:

```md
Inline: $U = R \cdot I$

Blok:
$$
P = U \cdot I
$$
```

## 5. Vyhledávání bere obsah Markdown souborů

- Vyplatí se psát jasné nadpisy a smysluplné názvy stránek.
- Důležitá klíčová slova dej i přímo do textu, ne jen do obrázku.

## 7. Drž strukturu sekcí konzistentní

- Každá sekce by měla mít své `README.md`, pokud funguje jako rozcestník.
- Nové stránky přidej tak, aby dávaly smysl i v sidebaru a v navazných odkazech.
- Když přesunuješ soubor, zkontroluj staré odkazy a obrázky.

## Doporučení na závěr

- Piš krátké odstavce a výstižné nadpisy.
- Po úpravě zkontroluj, že odkazy, obrázky a rovnice opravdu fungují.
- Když si nejsi jistý, podívej se na existující stránky v `docs/mo-jirka/` nebo `docs/mo-pavel/` a drž se stejného stylu.
