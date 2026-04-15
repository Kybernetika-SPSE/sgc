# Otázka 10

## Computer vision

- správce: Pavel
- stav: vlastni upravy autor.

---

## Související materiály

- [Základy umělé inteligence](../archiv/skripta-kyb/kybernetika/chapters/ZakladyUI.md)
- [Témata učení watafa](../archiv/skripta-kyb/Temata_uceni_watafa.md)
- [Neuronové sítě](../docs/mo-pavel/09-typy-neuronovych-siti.md)

# Computer Vision

Computer vision je oblast umělé inteligence zabývající se zpracováním a interpretací obrazu počítačem. Cílem je převést obraz na numerickou reprezentaci a následně z něj extrahovat informace – hrany, objekty, textury, nebo význam.

---

# Vznik digitálního obrazu

Digitální obraz vzniká převodem spojitého světelného signálu na diskrétní matici hodnot.

Proces má dvě hlavní fáze:

## Diskretizace (sampling)

Diskretizace znamená rozdělení spojitého obrazu do mřížky pixelů.

- obraz se rozdělí na body (pixely)

- každý pixel reprezentuje oblast scény

- rozlišení určuje počet pixelů (např. 1920×1080)

Vyšší rozlišení → více detailů  
Nižší rozlišení → ztráta detailů (aliasing)

Digitální obraz lze reprezentovat jako matici:

\[
\mathbf{I}(x,y)  
\]

kde:

- $x$, $y$ — souřadnice pixelu

- $\mathbf{I}$ — intenzita jasu nebo barvy

---

## Kvantizace (quantization)

Kvantizace převádí spojité hodnoty jasu na konečný počet diskrétních úrovní.

Například:

- 8 bitů → 256 úrovní jasu

- 10 bitů → 1024 úrovní

- 12 bitů → 4096 úrovní

Při malé kvantizaci vzniká:

- banding

- ztráta jemných přechodů

Digitální obraz je tedy:

- diskretizovaný v prostoru

- kvantizovaný v intenzitě

---

# Barevné modely

## RGB – additivní model

RGB je aditivní barevný model používaný displeji.

Barva je dána kombinací:

- R – red

- G – green

- B – blue

Každý kanál má typicky rozsah:

0–255

Například:

- (255,0,0) → červená

- (0,255,0) → zelená

- (0,0,255) → modrá

- (255,255,255) → bílá

- (0,0,0) → černá

Aditivní míchání:

- R + G = žlutá

- R + B = magenta

- G + B = cyan

- R + G + B = bílá

---

## Subtraktivní model (CMY / CMYK)

Používá se v tisku.

Základní barvy:

- C – cyan

- M – magenta

- Y – yellow

- K – black

Subtraktivní míchání:

- cyan absorbuje červenou

- magenta absorbuje zelenou

- yellow absorbuje modrou

CMY + K zlepšuje kontrast a snižuje spotřebu inkoustu.

---

## HSV model

HSV odděluje barvu od jasu.

- H – hue (odstín)

- S – saturation (sytost)

- V – value (jas)

Rozsahy:

- H: 0–360°

- S: 0–1

- V: 0–1

Výhody HSV:

- intuitivní práce s barvou

- jednoduchá segmentace

- oddělení jasu od barvy

Použití:

- detekce barev

- thresholding

- segmentace objektů

---

## Gamut a barevný trojúhelník

Gamut je množina barev, které zařízení dokáže zobrazit.

Barevný prostor RGB lze zobrazit jako trojúhelník:

- vrcholy = primární barvy

- uvnitř = kombinace

- mimo = nezobrazitelné barvy

Různé gamut:

- sRGB

- Adobe RGB

- DCI‑P3

Větší gamut → více barev

---

# Histogram obrazu

Histogram popisuje rozdělení jasů v obraze.

- osa X → jas (0–255)

- osa Y → počet pixelů

Histogram umožňuje:

- analyzovat kontrast

- detekovat přeexpozici

- normalizaci obrazu

---

## Histogram jasu

Histogram jasu používá grayscale obraz:

\[  
Y = 0.299R + 0.587G + 0.114B  
\]

Používá se pro:

- auto contrast

- equalizaci histogramu

- thresholding

---

## Oversaturation

Oversaturation znamená přesycení barev.

Projevy:

- ztráta detailů v barvě

- clipping kanálů

- nepřirozené barvy

Histogram:

- hodnoty u maxima

---

## Undersaturation

Undersaturation znamená nízkou sytost.

Projevy:

- vybledlé barvy

- blízkost grayscale

Histogram:

- úzké rozdělení barev

---

# Diskrétní konvoluce

Konvoluce je základní operace zpracování obrazu.

Výstupní pixel:

\[  
\mathbf{I}'(x,y) = \sum_{i=-k}^{k} \sum_{j=-k}^{k} \mathbf{K}(i,j) \mathbf{I}(x-i, y-j)  
\]

kde:

- $\mathbf{I}$ — vstupní obraz

- $\mathbf{K}$ — konvoluční jádro

- $\mathbf{I}'$ — výstupní obraz

Jádro se posouvá přes obraz.

---

# Konvoluční jádra

## Rozmazání (blur)

\[  
\frac{1}{9}  
\begin{bmatrix}  
1 & 1 & 1 \\  
1 & 1 & 1 \\ 
1 & 1 & 1  
\end{bmatrix}  
\]

---

## Gaussian blur

\[  
\frac{1}{16}  
\begin{bmatrix}  
1 & 2 & 1 \\  
2 & 4 & 2 \\ 
1 & 2 & 1  
\end{bmatrix}  
\]

---

# Detekce hran

## Sobel X

\[
\begin{bmatrix}  
-1 & 0 & 1 \\
-2 & 0 & 2 \\ 
-1 & 0 & 1  
\end{bmatrix}  
\]

## Sobel Y

\[  
\begin{bmatrix}  
-1 & -2 & -1 \\
0 & 0 & 0 \\
1 & 2 & 1  
\end{bmatrix}  
\]

Gradient:

\[  
G = \sqrt{G_x^2 + G_y^2}  
\]

---

## Laplace

\[  
\begin{bmatrix}  
0 & -1 & 0 \\
-1 & 4 & -1 \\  
0 & -1 & 0  
\end{bmatrix}  
\]

Detekuje změny intenzity.

---

# Medianový filtr

Medianový filtr je nelineární filtr.

Postup:

1. vezmi okolí pixelu

2. seřaď hodnoty

3. vyber medián

Použití:

- odstranění salt‑and‑pepper šumu

- zachování hran

---

# Pooling

Pooling zmenšuje rozlišení obrazu.

## Max pooling

Vybere maximum z oblasti.

Výhody:

- zachová hrany

- robustní na posun

---

## Average pooling

Počítá průměr.

Výsledek:

- hladší obraz

- ztráta detailů

---

# Segmentace obrazu

Segmentace je proces rozdělení obrazu na oblasti (segmenty), které odpovídají objektům nebo jejich částem.

Cílem segmentace je:

- oddělit objekt od pozadí

- rozdělit obraz na významné části

- připravit data pro klasifikaci

Výstupem segmentace je maska:

- 1 → objekt

- 0 → pozadí

---

## Prahování (thresholding)

Nejjednodušší segmentace používá práh $T$:

$$
\begin{gathered}
\mathbf{S}(x,y) = 1 \text{ pro } \mathbf{I}(x,y) > T  \\
\mathbf{S}(x,y) = 0 \text{ pro } \mathbf{I}(x,y) \leq T
\end{gathered}
$$

Typy thresholdingu:

- globální threshold

- adaptivní threshold

- Otsu metoda

---

## Segmentace podle barvy

Segmentace v HSV prostoru:

- threshold na Hue

- threshold na Saturation

- threshold na Value

Použití:

- detekce barevných objektů

- sledování objektu

---

## Segmentace pomocí hran

Postup:

1. detekce hran

2. spojení hran

3. vyplnění oblasti

Používá se pro:

- segmentaci tvarů

- detekci objektů

---

# Popis segmentu (feature extraction)

Po segmentaci lze každý segment popsat pomocí příznaků.

Tyto příznaky se používají pro klasifikaci objektů.

---

## Bounding box

Každý segment lze ohraničit obdélníkem:

- width

- height

- area

Poměr stran:

ratio = width / height

Například:

- mince → ratio $\approx$ 1

- tužka → ratio >> 1

---

## Plocha segmentu

Počet pixelů objektu:

A = počet pixelů segmentu

---

## Cirkularita

$$C = \frac{4πA}{P^{2}} $$

kde:

- $A$ — plocha

- $P$ — obvod

kruh → $C \approx 1$  
nepravidelný tvar → $C < 1$

---

## Těžiště segmentu

Střed objektu:
$$
\begin{gathered}
x_c = \frac1A \sum x \\
y_c = \frac1A \sum y
\end{gathered}
$$
---

## Další příznaky segmentu

- excentricita

- orientace objektu

- momenty

- convex hull

- solidity

---

# Klasifikace podle segmentu

Postup:

1. segmentace obrazu

2. výpočet příznaků

3. klasifikace

Příklad:

| Objekt | ratio       | cirkularita |
| ------ | ----------- | ----------- |
| mince  | $\approx1$  | $\approx 1$ |
| šroub  | $>2$        | malá        |
| matice | $\approx 1$ | nižší       |

Klasifikace může být:

- pravidla

- KNN

- SVM

- neuronová síť

---

# Shrnutí

Computer vision pracuje s obrazem jako maticí hodnot. Základní kroky:

1. digitalizace obrazu (diskretizace + kvantizace)

2. barevné modely (RGB, HSV)

3. histogram a kontrast

4. konvoluce a filtrace

5. detekce hran

6. median filtry

7. pooling

Tyto operace tvoří základ klasického zpracování obrazu i neuronových sítí (CNN).
