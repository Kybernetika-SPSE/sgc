# Otázka 06

## Učení s učitelem

- správce: Pavel
- stav: převedeno z archivu do nové stránky
- původní zdroj: [Strojové učení](../archiv/skripta-kyb/kybernetika/chapters/strojove_uceni.md)

---

# Strojové učení

Strojové učení je podmnožina umělé inteligence, která umožňuje modelům učit se z dat a zlepšovat svůj výkon bez explicitního naprogramování každého pravidla.
## Učení s učitelem (Supervised learning)

Učení s učitelem je metoda strojového učení, při které model trénuje na označených datech, kde každý vstup (vektor vlastností / feature vector) má odpovídající výstup (label). Cílem je naučit model predikovat výstup pro nové, neznámé vstupy.

### Data:

Každá položka vstupu je tedy vektor:

$$ x = [x_1, x_2, \ldots , x_n], \qquad x_i \in \mathcal{R}, $$

kde x_i jsou jednotlivé vlastnosti jednoho vstupu.

A každá položka má k ní odpovídající *label*, což je odpovídající výstup (od učitele). Celkem jde tedy o soubor dvojic dat 

$$\mathcal{D} = \{(x^{(i)}, y^{(i)})\}_{i=1}^{m}$$

kde každá taková dvojice odpovídá jednomu datu (objeku, záznamu, ...)


> Například, pokud budou jako vstupy různá auta, bude vektor $$x$$ popisovat sadu jejich vlastností. x = [barva, objem motoru, počet kol, počet sedadel, ...], celá trénovací sada pak bude více takových položek a k nim odpovídající labely.

### Rozdělení na trénovací a testovací sadu:

Cílem strojového učení není jen zapamatovat si trénovací data, ale naučit se zobecňovat – tedy správně reagovat i na nová, dosud neviděná data.

Pokud bychom model hodnotili na stejných datech, na kterých se učil, dostaneme zkresleně dobrý výsledek. Model si totiž může data „zapamatovat“ (přeučení / overfitting).

Proto dataset rozdělíme na dvě části:

- trénovací sada (train set) – slouží k učení modelu

- testovací sada (test set) – slouží k nezávislému ověření jeho kvality

Testovací data simulují reálné nasazení modelu v praxi.

#### Jak se train–test split provádí?

- Celý dataset se náhodně promíchá.

- Rozdělí se na dvě disjunktní části. Typicky: 70–80 % trénovací data a 20–30 % → testovací data

Důležité je, že:

- testovací data se nesmí používat při trénování

- testovací data se použijí až po dokončení učení

### Úlohy učení s učitelem:

## Regrese

Výstup je spojitá hodnota.

$$ y \in \mathcal{R} $$

Příklady:

- predikce ceny domu

- předpověď teploty

- odhad spotřeby energie

Model se snaží minimalizovat chybu mezi skutečnou a predikovanou hodnotou (např. střední kvadratickou chybu - MSE).

Regrese je úloha učení s učitelem, při které se snažíme najít funkci, která mapuje vstupní data na spojitou výstupní hodnotu.
Cílem je nalézt takovou funkci, která minimalizuje chybu mezi skutečnými hodnotami a predikcí modelu.
Speciálním případem je lineární regrese, kde model předpokládá lineární závislost mezi vstupy a výstupem a hledá přímku (resp. rovinu či nadrovinu), která data nejlépe aproximuje.

## Klasifikace

Výstup je diskrétní třída.


$$ y \in {1, 2, \ldots, K} $$

Typy klasifikace a příkaldy:

- Binární (např. spam / nespam)

- Multitřídní (např. rozpoznání číslice 0–9, rozpoznávání pes, kočka, pták, letadlo, ...)

Model rozhoduje, do které třídy vstup patří.

Klasifikace je úloha učení s učitelem, při které se snažíme najít funkci, která mapuje vstupní data na diskrétní výstupní třídu.
Cílem je nalézt takovou funkci, která co nejlépe rozlišuje jednotlivé třídy a minimalizuje počet chybných klasifikací.

## Lineární separabilita v klasifikaci

U klasifikace se snažíme najít rozhodovací hranici, která odděluje jednotlivé třídy v prostoru příznaků.

### Lineárně separabilní problém

Problém je lineárně separabilní, pokud existuje lineární rozhodovací hranice, která dokonale oddělí všechny třídy bez chyby.

V 2D prostoru je tato hranice přímka, ve 3D prostoru rovina, ve vyššícch dimenzích se nazývá obecně nadrovina.

Rozhodovací hranici lze zapsat jako:

$$
w^T x + b = 0
$$

kde:
- $w$ je vektor vah  
- $b$ je bias (posun)

Pokud lze najít takové $w$ a $b$, že všechny body jedné třídy splňují

$$
w^T x + b > 0
$$

a body druhé třídy

$$
w^T x + b < 0,
$$

pak je problém lineárně separabilní.

---

### Lineárně neseparabilní problém

Problém je lineárně neseparabilní, pokud neexistuje žádná lineární hranice, která by data dokonale oddělila.

V takovém případě je nutné zvolit jiný přístup:

- **Použít nelineární model**  
  Například neuronovou síť nebo rozhodovací strom, které dokáží vytvářet nelineární rozhodovací hranice (křivky místo přímek).

- **Transformovat data do vyšší dimenze**  
  Pomocí vhodné transformace příznaků lze původně neseparabilní data učinit separabilními v jiném prostoru.  
  Příkladem je přidání nových příznaků (např. $x_1^2$, $x_1 x_2$) nebo použití jádrové funkce (kernel trick) u metod jako SVM.

- **Připustit určitou klasifikační chybu (soft margin)**  
  V reálných datech často existuje šum nebo překryv tříd.  
  Model proto hledá rozhodovací hranici, která minimalizuje chybu, ale nemusí data oddělit dokonale.  
  Cílem je dobrá generalizace, nikoli perfektní oddělení trénovacích dat.

