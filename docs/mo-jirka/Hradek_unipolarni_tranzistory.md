# Hrádek – Unipolární tranzistory (FET)

---

## 1. Úvod a základní charakteristika

**FET** (*Field Effect Transistors* – tranzistory řízené elektrickým polem) jsou třísvorkové polovodičové součástky. Na rozdíl od bipolárních tranzistorů (BJT), kde výstupní proud řídí **proud** do báze, u FET výstupní proud řídí **elektrické pole** (napětí) na řídicí elektrodě.

| Vlastnost | FET | BJT |
|---|---|---|
| Způsob řízení | Napětím $U_{GS}$ | Proudem $I_{B}$ |
| Vstupní odpor | 10⁹ – 10¹⁴ Ω | 10² – 10⁵ Ω |
| Nosiče náboje | Pouze jeden typ (unipolární) | Oba typy (bipolární) |
| Řídicí proud | Minimální (pikoampéry) | Nenulový |
| Teplotní stabilita | Výborná | Horší (hrozí tepelný útěk) |
| Šumové vlastnosti | Nízký šum (zejm. JFET) | Vyšší šum |
| Zástavba v integrovaných obvodech | Velmi malá plocha | Větší plocha |

## Jednotky a fyzikální veličiny (FET)

| Symbol | Veličina | Jednotka | 
|---|---|---|
| $U_{GS}$ | napětí Gate–Source | V | 
| $U_{DS}$ | napětí Drain–Source | V | 
| $U_{TH}$ | prahové napětí MOSFET | V | 
| $U_{P}$ | pinch-off napětí JFET | V | 
| $I_{D}$ | proud drainem | A | 
| $I_{B}$ | proud báze | A | 
| $R_{DS(on)}$ | odpor kanálu v sepnutém stavu | Ω |
| $C_{ox}$ | kapacita oxidové vrstvy | F/m² | 
| $μ_{n}$| pohyblivost elektronů | m²·V⁻¹·s⁻¹ | 
| $W$ | šířka kanálu | m | 
| $L$ | délka kanálu | m |
| λ | modulace délky kanálu | V⁻¹ |
| K | technologický koeficient | A·V⁻² | 
| $I_{G}$ | proud hradlem | A | 

### Hlavní vlastnosti

- **Unipolární vedení:** Na vedení proudu se podílí **pouze jeden typ** nosičů náboje — buď majoritní elektrony (kanál N), nebo majoritní díry (kanál P).
- **Vysoký vstupní odpor:** U JFET dosahuje 10⁹ Ω, u MOSFET až 10¹⁴ Ω. Řídicí elektroda je od kanálu oddělena buď PN přechodem v závěrném směru, nebo vrstvou dielektrika.
- **Bezztrátové řízení:** V ustáleném stavu je řídicí proud prakticky nulový — součástka se ovládá napětím, nikoli proudem.
+
---

## 2. Fyzikální princip

Podstata funkce FET spočívá v **elektrostatické modulaci vodivosti polovodičového kanálu**.

Po přivedení napětí na hradlo (Gate, G) vůči zdroji (Source, S) vznikne elektrické pole, které působí na volné nosiče náboje v kanálu. Probíhá to dvěma způsoby:

**Ochuzení — JFET a depletionový MOSFET**
> Elektrické pole vytlačuje majoritní nosiče z kanálu. Rozrůstá se ochuzená vrstva (oblast bez volných nosičů), efektivní průřez kanálu se zužuje, jeho odpor roste a proud $I_{D}$ klesá.

**Inverze — enhancementový MOSFET**
> Kladné $U_{GS}$ na substrátu typu P nejprve odtlačí díry od povrchu a poté přitáhne minoritní elektrony. Jakmile jejich koncentrace u povrchu převýší koncentraci děr, nastane **silná inverze** a vznikne tenký indukovaný kanál N spojující Source s Drainem.

---

## 3. Rozdělení unipolárních tranzistorů

![](images/Hrádek_rozpis.jpg)

---

## 4. JFET – tranzistor s hradlovým PN přechodem

### Stavba

JFET tvoří tyčinka polovodiče (např. typu N), na jejích koncích jsou kontakty **Source (S)** a **Drain (D)**. Po obou stranách tyčinky jsou oblasti opačné vodivosti (P), navzájem propojené a vyvedené jako elektroda **Gate (G)**.

![](images/Hrádek_jfet.jpg)

---
### Jak JFET funguje (kanál N)

| Krok | Co se děje |
|:----:|------------|
| 1 | Přivedeme $U_{DS}$ > 0 → kanálem N začne téct proud $I_{D}$ |
| 2 | Přivedeme $U_{GS}$ < 0 → PN přechod se polarizuje v závěrném směru |
| 3 | Ochuzená vrstva se rozrůstá do kanálu → průřez kanálu se zmenšuje |
| 4 | Odpor kanálu roste → proud $I_{D}$ klesá |
| 5 | Při $U_{GS}$ = $U_{P}$ (závěrné napětí, pinch-off) → ochuzené vrstvy se spojí → kanál se uzavře → $I_{D}$ ≈ 0 |

>**Pozor:** JFET pracuje **výhradně v ochuzovacím režimu**. Kladné $U_{GS}$ u kanálu N použít nelze — otevřelo by PN přechod v propustném směru a zničilo unipolární charakter součástky.

---

## 5. MOSFET – tranzistor s izolovaným hradlem

Hradlo (Gate) je od polovodičového substrátu odděleno extrémně tenkou vrstvou oxidu křemičitého SiO₂ (tloušťka pouze několik nanometrů). Díky tomu vstupní odpor dosahuje až 10¹⁴ Ω.

### 5.1 Enhancementový MOSFET (s indukovaným kanálem)

**Normálně zavřený** — bez řídicího napětí proud nevede.

- Substrát je typu P, elektrody Drain a Source tvoří silně dotované oblasti N⁺.
- Při $U_{GS}$ = 0 brání průchodu proudu dva protilehlé PN přechody.
- Přivedením kladného $U_{GS}$ > 0 začne hradlo fungovat jako deska kondenzátoru: odtlačí díry od povrchu a přitáhne elektrony.
- Po překročení **prahového napětí U_TH** se pod oxidem vytvoří tenká vrstvička elektronů — **indukovaný kanál N** — a tranzistor začne vést.
- Podmínka vedení:   $U_{GS}$ > $U_{TH}$

![](images/Hrádek_nmos_indukovany.webp)

---

### 5.2 Depletionový MOSFET (se zabudovaným kanálem)

**Normálně otevřený** — kanál je fyzicky vytvořen již při výrobě, proud teče i při $U_{GS}$ = 0.

Může pracovat ve dvou režimech:

| Režim | Napětí $U_{GS}$ (NMOS) | Výsledek |
|-------|-------------------|----------|
| Ochuzení (depletion) | $U_{GS}$ < 0 | Nosiče se vytlačují → $I_{D}$ klesá |
| Obohacení (enhancement) | $U_{GS}$ > 0 | Nosiče se přitahují → $I_{D}$ roste |

![](images/Hrádek_nmos_zabudovany.jpg)

---

## 6. Pracovní oblasti a matematický popis

Chování NMOS s indukovaným kanálem popisují tři pracovní oblasti podle hodnot $U_{GS}$ a $U_{DS}$:

### Oblast odříznutí (Cut-off)

**Podmínka:** $U_{GS}$ < $U_{TH}$

Kanál neexistuje, tranzistor je uzavřen.

$$I_D \approx 0$$

---

### Lineární (triodová) oblast

**Podmínka:** $U_{GS}$ ≥ $U_{TH}$ a zároveň $U_{DS}$ < ($U_{GS}$ − $U_{TH}$)

Kanál je nepřerušený po celé délce od Source po Drain. Tranzistor se chová jako **napětím řízený odpor**.

$$I_{D} = K \cdot \left[ 2(U_{GS} - U_{TH}) \cdot U_{DS} - U_{DS}^2 \right]$$

kde parametr K závisí na technologii výroby:

$$K = \frac{1}{2} \mu_n C_{ox} \frac{W}{L}$$

---

### Saturační oblast (aktivní režim)

**Podmínka:** $U_{GS}$ ≥ $U_{TH}$ a zároveň $U_{DS}$ ≥ ($U_{GS}$ − $U_{TH}$)

Vlivem velkého napětí $U_{DS}$ dojde u elektrody Drain k **zaškrcení kanálu** (*pinch-off*). Od tohoto okamžiku proud $I_{D}$ prakticky nezávisí na $U_{DS}$ — řídí ho pouze napětí $U_{GS}$, a to kvadraticky.

$$I_D = K \cdot (U_{GS} - U_{TH})^2$$

---

## 7. Voltampérové charakteristiky

### Výstupní charakteristika — $I_{D}$ = f($U_{DS}$) při $U_{GS}$ = konst.

Zobrazuje přechod z lineární do saturační oblasti. Každá křivka odpovídá jinému napětí $U_{GS}$. V saturaci jsou křivky přibližně vodorovné.

![obr.5](images/Hrádek_vystupni_char.jpg)

### Převodní (přenosová) charakteristika — $I_{D}$ = f($U_{GS}$) při $U_{DS}$ = konst.

Ukazuje **kvadratickou závislost** proudu na řídicím napětí v saturaci:

- Enhancementový MOSFET: proud začíná téct až po překročení $U_{TH}$.
- JFET a depletionový MOSFET: křivka protíná osu proudu (při $U_{GS}$ = 0 teče nenulový proud), klesá k nule při $U_{GS}$ = $U_{P}$.

![obr.6](images/Hrádek_transfer2.png)

---

## 8. Parazitní jev

### Modulace délky kanálu

V saturační oblasti se s rostoucím $U_{DS}$ bod zaškrcení posouvá blíže k Source → efektivní délka kanálu $L$ se zkracuje → $I_D$ mírně roste i v saturaci (namísto ideálně konstantní hodnoty).

Korigovaný výpočet:

$$I_D = K \cdot (U_{GS} - U_{TH})^2 \cdot (1 + \lambda \cdot U_{DS})$$

kde $\lambda$ je parametr modulace délky kanálu (jednotky V⁻¹).

### Subprahová vodivost

I při $U_{GS}$ < $U_{TH}$ protéká tranzistorem malý proud s exponenciální závislostí na $U_{GS}$. V moderních procesorech je tento proud hlavní příčinou **klidové spotřeby** celého čipu.

---

## 9. Výhody a nevýhody FET

### Výhody

- **Téměř nekonečný vstupní odpor** — v ustáleném stavu neodebírá řídicí elektroda žádný výkon.
- **Vynikající teplotní stabilita** — s rostoucí teplotou klesá pohyblivost nosičů, proud se tedy sám od sebe omezuje. U BJT hrozí naopak tepelný útěk.
- **Nízký šum** — proud neteče přes PN přechod v propustném směru, takže nevzniká rekombinační šum. JFET se proto používá na vstupních stupních citlivých zesilovačů.
- **Malé rozměry** — v integrovaných obvodech zabírají FET tranzistory mnohonásobně méně plochy než BJT.

### Nevýhody

- **Citlivost na elektrostatický výboj (ESD)** — tenká vrstvička SiO₂ se prorazí již při napětí desítek voltů. Součástky proto vyžadují ochranné diody a opatrnou manipulaci.
- **Kapacita hradla C_iss** — při vysokých spínacích frekvencích je nutné tuto kapacitu rychle nabíjet a vybíjet, což způsobuje dynamické ztráty a proudové špičky v řídicím obvodu.

---

## 10. Nejdůležitější aplikace

### CMOS logika

> Základ všech moderních procesorů, pamětí a mikrokontrolérů.

Komplementární dvojice NMOS a PMOS zapojená jako invertující člen. V každém logickém stavu je vždy jeden z tranzistorů zcela uzavřen → **statický příkon celého čipu je prakticky nulový**.

<iframe
	src="https://www.falstad.com/circuit/circuitjs.html?ctz=DwYwlgTgBAZgvAIgAwKgFwM6KQOif-AVlTBEQEZcAmfKgdjoGYkAOKgNgE5O7UQAjRIRRQADoITDUANwhDUAW0xCApgFpy5BAD4AUFCjAYUAB6IaLKOTrso9KlZup4CLVGloKOYlH4rseFQIAPR6Bkam5qx2dA72MUGw2DKert6ofgFIQaH6hgDukQjx5JxxsXZUACzOybnhhWbFFVTVCXaE7LXIIWEFRRaOtoOtNUk99f1NI20jsd0ok8AAMgPRo1bsSJVjLot9wACyAy1tjIzD1Qu9ecAASicO5Fvtmol7qPkfUAoAhibSeRLADmjzsLEs8UYNGuuWAwXAED0QA"
	width="100%"
    height="400"
    title="CMOS inventer - Falstad"
    loading="lazy"
    style="border: 1px solid #ddd; border-radius: 8px;">
</iframe>

### Výkonové spínání

> Spínané zdroje, střídače, pohony, elektromobily.

Výkonové MOSFETy zvládají spínat stovky ampér při napětích v řádu kilovoltů. Odpor v sepnutém stavu R_DS(on) dosahuje hodnot jednotek až desítek miliohmů → minimální ztráty.

### Vysokofrekvenční a mikrovlnná technika

> Satelitní přijímače, radary, mobilní sítě.

Součástky GaAs FET a HEMT (*High Electron Mobility Transistor*) umožňují zesílení signálů v pásmech desítek gigahertzů s velmi nízkým vlastním šumem.

### Nízkošumové zesilovače

> Kondenzátorové mikrofony, měřicí přístroje, přístrojová technika.

JFET na vstupním stupni zajistí vysoký vstupní odpor a nízký šum — klíčové vlastnosti pro zesílení slabých signálů ze snímačů.

---

## Přehled vzorců

| Pracovní oblast | Podmínka | Výpočet I_D |
|----------------|----------|-------------|
| Odříznutí (cut-off) | $U_{GS}$ < $U_{TH}$ | $I_{D}$ ≈ 0 |
| Lineární (triodová) | $U_{GS}$ ≥ $U_{TH}$, $U_{DS}$ < $U_{GS}$ − $U_{TH}$ | $I_{D}$ = K · [2($U_{GS}$−$U_{TH}$)·$U_{DS}$ − $U²_{DS}$] |
| Saturace | $U_{GS}$ ≥ $U_{TH}$, $U_{DS}$ ≥ $U_{GS}$ − $U_{TH}$ | $I_{D}$= K · ($U_{GS}$ − $U_{TH}$)² |
