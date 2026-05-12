﻿# Otázka 15

## Kombinační a sekvenční logika

- správce: Jirka
- stav: převedeno z archivu do nové stránky
- původní zdroj: [15. Kombinační a sekvenční logika](../archiv/skripta-kyb/kybernetika/chapters/15.%20Kombinační%20a%20sekvenční%20logika.md)

---

Logické obvody, kde výstupní stavy závisí na současných i předchozích vstupních stavech. Jde tedy o obvod s pamětí.

Obsahují zpětnou vazbu, tedy tzv. *vnitřní výstupy* jsou zapojeny na tzv. *vnitřní vstupy*. Jejich stav pak určuje vnitřní stav sekvenčního obvodu.

Dělí se na:
- **Asynchronní** = jejich stav se mění při jakékoli změně vstupních hodnot
- **Synchronní** = stav se může měnit jen v okamžicích určených *hodinovým vstupem* (`clock`), obvykle jeho náběžnou hranou

# Klopný obvod RS (Flip-flop)
- asynchronní
- má dva vstupy: $S$ = `set`, $R$ = `reset`
- má dva výstupy (ostatní druhy taky): $Q$ = `výstup`, $\overline{Q}$ = `negace výstupu`
- $1$ na vstupu $S$ nastaví výstup na 1
- $1$ na vstupu $R$ nastaví výstup na 0
- $1$ na vstupu $S$ a $R$ zároveň je **nepovolený stav**

$$
\begin{array}{cc|c}
S & R & Q \\
\hline 0 & 0 & Q \\
0 & 1 & 0 \\
1 & 0 & 1 \\
1 & 1 & -
\end{array}
$$

![](images/15-sr-flip-flop-async-circuit.png ":class=pre-inverted")
![](images/15-sr-flip-flop-async-symbol.png ":class=pre-inverted")

# Synchronní klopný obvod RS
- synchronní
- viz výše
- má hodinový vstup $C$ ($EN$)
- když chci změnit stav změnou vstupů, musím dát zároveň $1$ i na vstup $C$, jinak nereaguje na vstupy

$$
\begin{array}{ccc|c}
S & R & C & Q \\
\hline 0 & 0 & \uparrow & Q \\
0 & 1 & \uparrow & 0 \\
1 & 0 & \uparrow & 1 \\
1 & 1 & \uparrow & -
\end{array}
$$

![](images/15-sr-flip-flop-sync.png ":class=pre-inverted")

# Klopný obvod JK
- synchronní
- vstupy $J$, $K$
- hodinový vstup $C$ ($CLK$)
- když chci změnit stav změnou vstupů, musím dát zároveň $1$ i na vstup $C$, jinak nereaguje na vstupy
- když $J=K=0$, výstup zůstává stejný
- když $J=K=1$, výstup se neguje
- $K=1$ a $J=0$, výstup se nastaví na $0$
- $K=0$ a $J=1$, výstup se nastaví na $1$

$$
\begin{array}{ccc|c}
J & K & C & Q \\
\hline 0 & 0 & \uparrow & Q \\
0 & 1 & \uparrow & 0 \\
1 & 0 & \uparrow & 1 \\
1 & 1 & \uparrow & \overline{Q}
\end{array}
$$

![](images/15-jk-flip-flop.png ":class=pre-inverted")

# Klopný obvod D
- synchronní
- vstup $D$
- hodinový vstup $C$
- když chci změnit stav změnou vstupů, musím dát zároveň $1$ i na vstup $C$, jinak nereaguje na vstup
- když $D=0$, výstup se nastaví na $0$
- když $D=1$, výstup se nastaví na $1$
- v podstatě jeden bit RAM

$$
\begin{array}{cc|c}
D & C & Q \\
\hline 0 & \uparrow & 0 \\
1 & \uparrow & 1
\end{array}
$$

![](images/15-d-flip-flop.png ":class=pre-inverted")

# Klopný obvod T
- asynchronní
- jen vstup $T$
- jednička na vstupu $T$ překlopí výstup na negaci předchozího stavu (`0 -> 1`, `1 -> 0`)

$$
\begin{array}{c|c}
T & Q \\
\hline 0  & Q \\
1  & \overline{Q}
\end{array}
$$

![](images/15-t-flip-flop.png ":class=pre-inverted")

# Použití klopných obvodů:
## Čítače
viz. [Čítače, časovače a přerušení](18-citace-casovace-a-preruseni.md)

## Posuvné registry (PR)
- kaskádně (za sebou) zapojené klopné obvody, počet klopných obvodů určuje počet bitů (stupňů)
- např. do 8bitového PR se vejde 8 bitů, čili např. může převést 8 bitů sériových dat na paralelní data o šířce 8 bitů
- využití především jako převodníky ze sériových na paralelní data nebo z paralelních na sériová data
- prakticky se dají použít i pro rozšíření počtu vstupů a výstupů mikrokontroleru (`PISO` pro vstupy, `SIPO` pro výstupy). Mikrokontroler komunikuje s registrem sériově pomocí několika pinů, zatímco registr může nabídnout více vstupů a výstupů.

## Sériová data
Data přenášená typicky dvěma vodiči: na jednom jsou hodinové impulsy (`CLK`), na druhém samotná data (jednička nebo nula), která se čtou ve správný okamžik podle hodin.
![](images/15-serial-data.png)

## Paralelní data
Například 8 vodičů vedle sebe, na každém je samostatně jednička nebo nula. Data jsou tedy dostupná současně, bez nutnosti sériového hodinového přenosu.

## Základní druhy:
(kromě popsaných paralelních/sériových vstupů mají ještě řídící vstupy Reset, Enable atd. atd.)

### SISO (Serial In Serial Out)
- má sériový vstup i výstup
- slouží například ke zpoždění sériových dat; data na výstupu jsou zpožděná o $n$ impulsů `CLK`, kde $n$ je počet stupňů registru

### SIPO (Serial In Parallel Out)
- má sériový vstup a paralelní výstup
- přijatá data se naposouvají do paralelních výstupů (jako když nabíjím dva druhy střel (jedničky a nuly) do zásobníku)
- pokud do registru pošlu víc bitů sériových dat, než kolik pojme, nové bity vytlačí ty nejstarší. Když tedy do 8bitového registru pošlu 10 bitů, na paralelních výstupech zůstanou jen poslední 8 bitů.

### PISO (Parallel In Serial Out)
- má paralelní vstup a sériový výstup
- má hodinový vstup $C$ (CLK)
- na paralelní vstup se nahrají paralelní data
- pomocí impulsů CLK se jednotlivé bity vyposouvají na sériový výstup
