# Otázka 08

## Základní principy neuronových sítí

- správce: Pavel
- stav: částečně převedeno z archivu do nové stránky
- původní zdroje:
  - [Perceptron - teorie](../archiv/skripta-kyb/kybernetika/codes/klasifikace/perceptron_teorie.md)
  - [Strojové učení](../archiv/skripta-kyb/kybernetika/chapters/strojove_uceni.md)

---

Tato otázka má ve starých materiálech zatím nejsilnější pokrytí přes perceptron, tedy základní model umělého neuronu. Vícevrstvé sítě, aktivační funkce a backpropagation bude vhodné doplnit samostatně.
# Jak funguje perceptron

Perceptron je jednoduchý model umělého neuronu, který se používá pro binární klasifikaci. Jeho úkolem je rozdělit data do dvou tříd, například $+1$ a $-1$.

---

## Základní princip

Perceptron dostává několik vstupů $x_{1}, x_{2}, \dots, x_{n}$. Každý vstup má přiřazenou váhu $w_{1}, w_{2}, \dots, w_{n}$, která určuje, jak je daný vstup důležitý.

Model spočítá lineární kombinaci vstupů a vah:

$z = w_{1} \cdot x_{1} + w_{2} \cdot x_{2} + \dots + w_{n} \cdot x_{n} + b$

kde $b$ je bias (konstanta, která posouvá rozhodovací hranici).

---

## Rozhodnutí

Výsledek z se pošle do jednoduché aktivační funkce sign:

$$y = \mathrm{sign}(z)$$

Pokud je $z > 0$, perceptron vrátí $+1$.  
Pokud je $z \leq 0$, vrátí $-1$.

Tak perceptron určí, do které třídy vstup patří.

---

## Učení perceptronu

Perceptron se učí z trénovacích dat. Postupně prochází všechny příklady a upravuje váhy podle toho, jestli klasifikoval správně nebo ne.

1. Pro daný vstup $x_{i}$ spočítá výstup $\hat{y}_{i} = \mathrm{sign}(w \cdot x_{i} + b)$.
2. Pokud se spletl ($\hat{y}_{i} \neq y_{i}$), upraví váhy podle pravidla:

$$
\begin{align}
  w &:= w + \eta \cdot (y_{i} - \hat{y}_{i}) \cdot x_{i} \\
  b &:= b + \eta \cdot (y_{i} - \hat{y}_{i})
\end{align}
$$

kde $\eta$ je koeficient učení (*learning rate*), $y_{i}$ je skutečná hodnota (label) a $\hat{y}_{i}$ je predikce.

3. Proces se opakuje v tzv. epochách, dokud nejsou všechny příklady správně klasifikovány nebo dokud se chyba dále nezmenšuje.

---

## Výsledek

Po natrénování perceptron najde takové váhy a bias, které určují rozhodovací hranici:

$$w_{1} \cdot x_{1} + w_{2} \cdot x_{2} + b = 0$$

Tato přímka (v $2D$) nebo rovina (v $nD$) rozděluje prostor na dvě oblasti odpovídající dvěma třídám.

---

## Omezení

Perceptron dokáže správně fungovat pouze tehdy, když jsou data lineárně oddělitelná.  
Pokud se třídy překrývají, nebo jsou nelineárně rozloženy (například problém XOR), perceptron správné řešení nenajde.


## Co ještě doplnit

- vícevrstvé neuronové sítě
- aktivační funkce
- zpětné šíření chyby (backpropagation)
- rozdíl mezi perceptronem a moderní neuronovou sítí
