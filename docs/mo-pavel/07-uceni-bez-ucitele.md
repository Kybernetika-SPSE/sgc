# Otázka 07

## Učení bez učitele

- správce: Pavel
- stav: převedeno z archivu do nové stránky
- původní zdroje:
  - [Strojové učení](../archiv/skripta-kyb/kybernetika/chapters/strojove_uceni.md)
  - [K-means teorie](../archiv/skripta-kyb/kybernetika/codes/shlukovani/kmeans_teorie.md)
  - [PCA teorie](../archiv/skripta-kyb/kybernetika/codes/pca/pca_teorie.md)

---

# Učení bez učitele
## Učení bez učitele (Unsupervised learning)

Učení bez učitele je metoda strojového učení, při které model pracuje pouze se vstupními daty bez známých výstupních hodnot (labelů).  
Cílem není predikovat konkrétní výstup, ale objevit skrytou strukturu, vzory nebo vztahy v datech.

### Data:

Každá položka vstupu je opět vektor:

$$
x = [x_1, x_2, \ldots , x_n], \qquad x_i \in \mathcal{R}
$$

Dataset tedy obsahuje pouze vstupy:

$$
\mathcal{D} = \{ x^{(i)} \}_{i=1}^{m}
$$

Na rozdíl od učení s učitelem zde neexistují odpovídající hodnoty $y^{(i)}$.

---

### Cíl učení bez učitele

Model se snaží:

- seskupovat podobná data dohromady,
- odhalovat strukturu dat,
- snižovat dimenzionalitu,
- identifikovat anomálie.

Nejde tedy o aproximaci známé funkce $f(x) \approx y$, ale o hledání vnitřní struktury dat.

---

## Úlohy učení bez učitele

### Shlukování (Clustering)

Cílem je rozdělit data do skupin (shluků) tak, aby si body v rámci jednoho shluku byly co nejvíce podobné a mezi shluky co nejméně podobné.

Příklady:
- segmentace zákazníků
- rozdělení dokumentů podle tématu
- seskupování obrázků

Typický algoritmus:
- K-means

---

### Redukce dimenzionality

Cílem je snížit počet příznaků při zachování co největšího množství informace.

Použití:
- vizualizace vícerozměrných dat
- zjednodušení modelu
- odstranění šumu

Typický algoritmus:
- PCA (Principal Component Analysis)

---

### Detekce anomálií

Cílem je najít data, která se výrazně liší od ostatních.

Příklady:
- detekce podvodů
- odhalení chyb v systému
- monitorování bezpečnosti

---

# K-means (metoda k-průměrů)

## Co je K-means
K-means je **neřízená** metoda strojového učení používaná pro **shlukování dat (clustering)**.  
Jejím cílem je **rozdělit data do K skupin (shluků)** tak, aby si body ve stejném shluku byly co nejpodobnější a body v různých shlucích co nejvíce odlišné.

---

## Hlavní myšlenka
K-means hledá **středy (centroidy)** K shluků a přiřazuje každý bod k nejbližšímu středu.  
Poté středy přepočítá jako průměry všech bodů, které do daného shluku patří.  
Proces se opakuje, dokud se středy „neustálí“.

---

## Postup algoritmu

| Krok | Popis                                                                 |
|------|------------------------------------------------------------------------|
| 1    | Zvol počet shluků **K**.                                               |
| 2    | Náhodně inicializuj **K počátečních středů (centroidů)**.              |
| 3    | Každý bod přiřaď ke **nejbližšímu středu** (např. podle Eukleidovské vzdálenosti). |
| 4    | **Přepočítej středy** jako průměr všech bodů, které do shluku patří.   |
| 5    | Opakuj kroky 3–4, dokud se středy nezmění nebo se změny stanou malé.   |

---

## Matematicky (zjednodušeně)

Hledáme rozdělení dat $ X = \{x_1, x_2, ..., x_n\} $ do K shluků $ C_1, ..., C_K $, které minimalizuje tzv. **chybu (SSE – Sum of Squared Errors):**

$$
J = \sum_{k=1}^{K} \sum_{x_i \in C_k} ||x_i - \mu_k||^2
$$

kde:
- $ \mu_k $ je centroid (střed) shluku $ C_k $,
- $ ||x_i - \mu_k|| $ je vzdálenost bodu od středu shluku.

---

## Intuice
- Každý shluk má svůj **střed (centroid)**.
- Body se **přiřazují** ke středu, který je nejblíže.
- Poté se středy **posunou** do nových pozic – do průměru svých bodů.
- Tento proces se **opakuje**, dokud se středy ustálí.

---

## Vlastnosti
- Algoritmus **vždy konverguje**, i když může uvíznout v **lokálním minimu**.
- Pořadí inicializace může ovlivnit výsledky – často se používá **K-means++** pro lepší výběr počátečních středů.

---

## Výhody
- Jednoduchý a rychlý.
- Dobře škáluje na velké množství dat.
- Snadno interpretovatelný výsledek (centroidy).

---

## Nevýhody
- Musí se **předem zvolit K** (počet shluků).
- Je citlivý na **počáteční pozici centroidů**.
- Funguje dobře pouze pro **sférické (kulovité) shluky**.
- Špatně pracuje s odlehlými body (outliery).

---

## Shrnutí
K-means je jednoduchý, ale účinný algoritmus pro **rozdělení dat na K shluků** na základě jejich podobnosti.  
Pracuje iterativně – střídavě **přiřazuje body ke středům** a **přepočítává středy**, dokud nedojde ke stabilizaci.


---

# PCA – Analýza hlavních komponent (Principal Component Analysis)

## Co je PCA
PCA je **statistická metoda** používaná pro **snížení rozměrnosti dat**.  
Jejím cílem je převést původní data do nového souřadného systému tak, aby:

- co nejvíce zachovala **variabilitu dat (informaci)**,  
- a zároveň používala **co nejméně dimenzí**.

---

## Intuice
PCA hledá **nové osy (hlavní komponenty)**, které:

1. jsou **kolmé (nezávislé)**,  
2. zachycují **maximální rozptyl** dat.

Tím umožňuje:
- zjednodušit data,
- odstranit šum,
- a zlepšit vizualizaci i výkon následných algoritmů (např. klasifikátorů).

---

## Kdy použít PCA
- Máš **hodně vstupních znaků (features)**.
- Některé jsou **silně korelované**.
- Chceš **zmenšit rozměrnost** dat bez ztráty většiny informace.

---

## Hlavní myšlenka
Místo původních os (x₁, x₂, …, xₙ) se najdou **nové osy (PC₁, PC₂, …)**, které:

- směřují tam, kde mají data největší rozptyl,  
- postupně zachycují co nejvíce informace.

První osa (PC₁) vysvětluje největší část rozptylu, druhá menší atd.

---

## Postup algoritmu

| Krok | Popis |
|------|--------|
| 1 | **Normalizuj data** – odečti průměr každého sloupce (centrace). |
| 2 | **Spočítej kovarianční matici** dat. |
| 3 | **Najdi vlastní čísla a vlastní vektory** kovarianční matice. |
| 4 | **Seřaď vlastní vektory** podle velikosti vlastních čísel (rozptyl). |
| 5 | **Vyber prvních k komponent** – ty zachytí největší část variability. |
| 6 | **Projektuj data** na tyto komponenty → získáš data v menší dimenzi. |

---

## Matematicky (zjednodušeně)

Máme matici dat $ X \in \mathbb{R}^{n \times d} $:

1. Centrovaná data:  
   $ X' = X - \bar{X} $

2. Kovarianční matice:  
   $ C = \frac{1}{n-1} (X')^T X' $

3. Vlastní čísla λ a vlastní vektory v:
   $$
   C v = \lambda v
   $$

4. Seřadíme vektory podle λ (od největšího).

5. Projekce na k komponent:
   $$
   Z = X' W_k
   $$
   kde $ W_k $ obsahuje první k vlastních vektorů.

---

## Vizuální intuice
Představ si body rozložené podél šikmé přímky v rovině.  
PCA najde **směr této přímky** (největší rozptyl) a **projekcí bodů** na ni vytvoří 1D reprezentaci.

---

## Výhody
- Zjednodušuje data (menší počet dimenzí).  
- Odstraňuje šum a korelované znaky.  
- Zrychluje učení modelů.  
- Umožňuje vizualizovat i vysokodimenzionální data (např. v 2D).

---

## Nevýhody
- **Ztrácí interpretaci** – nové osy jsou lineární kombinace původních znaků.  
- Funguje pouze na **lineární** závislosti.  
- **Citlivá na měřítko** – je nutná standardizace.

---

## Shrnutí

| Vlastnost | Popis |
|------------|--------|
| Typ | Neřízená metoda (unsupervised) |
| Účel | Snížení rozměrnosti |
| Hlavní princip | Najde směry s největším rozptylem |
| Matematika | Vlastní vektory kovarianční matice |
| Výsledek | Data v novém souřadném systému s menším počtem dimenzí |
