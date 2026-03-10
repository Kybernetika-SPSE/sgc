# Otázka 04

## Karnaughovy mapy

- správce: Pavel
- stav: převedeno z archivu do nové stránky
- původní zdroj: [Booleovská algebra](../archiv/skripta-kyb/kybernetika/chapters/booleovska_algebra.md)

---

Karnaughovy mapy jsou ve zdrojových materiálech součástí společné kapitoly s Booleovou algebrou.
## Karnaughova mapa (K-map) 
je grafická metoda používaná k minimalizaci logických výrazů v Booleově algebře. Pomáhá jednoduchým a přehledným způsobem redukovat složité logické funkce na jejich nejjednodušší podobu. Tato metoda je zvláště užitečná při návrhu logických obvodů.

### Struktura Karnaughovy mapy
Karnaughova mapa je tabulka, kde každé pole odpovídá určité kombinaci hodnot vstupních proměnných. Pole jsou uspořádána tak, aby se sousední pole lišila vždy pouze v jedné proměnné (Grayův kód). Pro $n$ proměnných má mapa $2^n$ polí.

### Postup minimalizace pomocí Karnaughovy mapy

- Nakreslení Karnaughovy mapy odpovídající počtu proměnných.
- Zapsání hodnot logické funkce (0 nebo 1) do příslušných polí mapy podle hodnot vstupních proměnných.
- Seskupení jedniček (1) do co největších obdélníkových nebo čtvercových bloků.
  - Bloky musí mít velikost mocniny čísla 2 (1, 2, 4, 8 atd.).
  - Bloky mohou být vodorovné nebo svislé (nikoliv diagonální).
  - Karnaughova mapa je nekonečná, což znamená, že levý a pravý okraj, stejně jako horní a dolní okraj, jsou spojeny.
  - Bloky se mohou (částčně) překrývat. 
  - Každá jednička (1) musí být v nějakém bloku
  - Počet bloků musí být co nejmenší. (Bloky musí být co největší)
- Zapsání minimalizovaného výrazu na základě seskupených bloků.

> Poznámka:
> pokud seskupujem do bloků jedničky (1), vzniká zápisem disjuktní normální forma (součet součinů). Můžeme rovněž seskupovat nuly (0), pak vzniká konjuktní normální forma (součin součtů).

### Příklad:

![](../assets/mo-pavel/karnaugh.png)




