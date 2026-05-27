# H-můstek

## Úvod

Zatímco v předchozích tématech jsme se zabývali pasivními prvky a základními polovodiči, v této otázce se podíváme na jedno z nejdůležitějších zapojení výkonové elektroniky – **H-můstek**. Pokud potřebujeme stejnosměrný motor (DC motor) nejen zapnout a vypnout, ale také měnit směr jeho otáčení nebo jej aktivně brzdit, pouhý jeden spínací tranzistor nám stačit nebude. 

H-můstek dostal svůj název podle specifického tvaru schématu, které připomíná písmeno **H**. Skládá se ze čtyř spínačů (zpravidla tranzistorů) a zátěže (motoru) umístěné uprostřed jako „příčka“ tohoto písmene. Je základním stavebním kamenem robotiky, pohonů CNC strojů, elektrických vozidel i spínaných měničů.

---

## Princip fungování a stavy můstku

Můstek tvoří čtyři spínače označené jako $S_1, S_2, S_3, S_4$. Podle toho, které spínače sepneme, dovolíme proudu téci zátěží v jednom nebo druhém směru.

```
       + Vcc (Napájení)
        |         |
     +--+--+   +--+--+
     |  S1 |   |  S3 |  <-- Horní spínače (High-Side)
     +--+--+   +--+--+
        |         |
        +--[ M ]--+     <-- Motor (Zátěž)
        |         |
     +--+--+   +--+--+
     |  S2 |   |  S4 |  <-- Dolní spínače (Low-Side)
     +--+--+   +--+--+
        |         |
       --- GND (Zem)
```
| Sepnuté spínače | Stav motoru | Popis funkce |
| :--- | :--- | :--- |
| **$S_1$ a $S_4$** | **Otáčení vpravo** | Proud teče z $+V_{cc}$ přes $S_1$, motorem zleva doprava a přes $S_4$ do GND. |
| **$S_3$ a $S_2$** | **Otáčení vlevo** | Proud teče z $+V_{cc}$ přes $S_3$, motorem zprava doleva a přes $S_2$ do GND. |
| **Všechny rozepnuté** | **STOP (Volnoběh)** | Motorem neteče žádný proud, hřídel volně dobíhá. |
| **$S_1$ a $S_3$** nebo **$S_2$ a $S_4$** | **Brzda** | Motor je zkratován do napájení (nebo země), generuje protisílu a rychle zastaví. |
| **$S_1$ a $S_2$** nebo **$S_3$ a $S_4$** | **ZAKÁZANÝ STAV** | **Zkrat zdroje (Shoot-through)!** Proud teče přímo z $+V_{cc}$ do GND a hrozí zničení prvků. |

### Základní pracovní stavy

1. **Směr vpřed (Dopředu):** Sepneme spínače **$S_1$ a $S_4$** (ostatní jsou rozpojené). Proud teče z $V_{cc}$ přes $S_1$, motorem zleva doprava a přes $S_4$ do země ($GND$). Motor se točí jedním směrem.
2. **Směr vzad (Dozadu):** Sepneme spínače **$S_3$ a $S_2$** (ostatní jsou rozpojené). Proud teče z $V_{cc}$ přes $S_3$, motorem zprava doleva a přes $S_2$ do země ($GND$). Polarita na motoru se obrátila a motor se točí naopak.
3. **Zastavení setrvačností (Freewheel):** Všechny spínače jsou **rozpojené**. Motor není napájen a pomalu se zastaví vlastní setrvačností.
4. **Aktivní brzdění (Short/Brake):** Sepneme buď oba dolní spínače (**$S_2$ a $S_4$**), nebo oba horní spínače (**$S_1$ a $S_3$**). Motor se v tomto stavu chová jako generátor. Tím, že jeho vývody zkratujeme, vznikne velký protiproud (brzdný moment), který motor téměř okamžitě zastaví.

> **Mnemotechnická pomůcka:** Pro rotaci spínej vždy tranzistory v **úhlopříčce**. Nikdy nespínej tranzistory nad sebou!

### Zakázaný stav (Zkrat / Shoot-Through)
Pokud by došlo k současnému sepnutí spínačů nad sebou (např. $S_1$ a $S_2$), proud poteče přímo z napájecího zdroje do země tou nejjednodušší cestou. Vznikne **tvrdý zkrat**. V lepším případě zasáhne proudová pojistka, v horším případě tranzistory okamžitě shoří.

---

## Realizace pomocí tranzistorů

V reálné praxi se místo mechanických spínačů používají tranzistory. U menších výkonů bipolární (BJT), u moderních a výkonnějších zapojení výhradně polí řízené tranzistory (**MOSFET**), případně **IGBT** tranzistory pro velmi vysoká napětí.

<iframe
    src="https://www.falstad.com/circuit/circuitjs.html?ctz=DwYwlgTgBAZgvAIgIwKgFwM6IAwDpsEECsqYIiSuAHACwDsAnEVQGzYtIENVEuogAjRL1QAHIQiLZUANwjDUAW0zCApgFokKAHwAoKFGBooADwp0WUKtihIGAJivTYOMQDsKqAaooElAe0QAE1UYAEMAVwAbNFlvHHx7GgYUqnsGJCJuDKQ6KjjyBDxsJJTuHh4AZhYaGipKhAB6PQMjU0QaJEtrKBoCJ1R4IvdPKHjkPyhFQIQQ8OjYqBlx4tLU9Mzs3PsChJLk1IqiappjmiaWw2MzZAtbNlsHe+ch51EPZC8fCedp4NDIjE4t9VgdysxjjV6PY6LsiokwWVrPUaFCLvoru0EJ1LF0bH0bHjBq4oO9RuNOL8ZnNAYtliCEUijidOkQSEsBIVQWUkdgUVl0a1oDc8c8oDVnsThlB5D9pM0McBhR06mKiLVJS5pbLKfLLkqsUlCUhHPYqFRbCapc4dXrFVFDebLY5KkRHFodlrnFE9uyyCSwB1cCwqNw6HR7EQTa77Bp7CgFa0AO6GpLOx7uq1ewWGFMip4MXFPD3WnPAPOIGPpgnO0uJ3NYmse3r9Qt1-UAcyxdlNfIzUHsSXbiq7Nxr9j746H2frwCCWOqFp7UEXtjNpam1IBCzLMkdFpsZot6kqnqGXVQSdeSjCJhkClnFYQR-uA6dL1cj8b-S6b6XfBnfUnxfX9lwvQDFSfWoLR6HEBgg5NG1VUU4KJBDDGVbFVR6dUaHg68ZV8PwvxFB5RVyXE2GHRDSJsHoKPwz99Uw0UeglawN1tYigMbGD8QtU8P2GEiOgEicoFwlcJ2ohsbkkwSJI1NDrxEyQHkjSwJQ0mTyyxLTeHFPDlKYxVRGuRA2DEiTiwA88byIt4ZmKbB2QwH0EAAEX8KJVBkMIywAJT0vsbEsqATzPCgAKvElFFve9JDLUcLL7U9xUnfJ0OAZKiikqB+J0oKbhsErwtPKVwJi6U4rvB99TMrFSpscqtRQKYwgcsQnNwFIpEIfr+ratzEC80QIDCPyyygvjDMY4SeLk9SDN4OihLtGjhAeHCNQ4rLpqcXp-x0-bQMo46sRWg7LpalSFs25rHEu8Dbsgi6yMsLJ3VskyNoQVcTQtJt1z2hcQ37JsHHOscfxNFtCWBl7fqBwGf1qKGOh-O4Ici+bXuhwknnHPkdPnG5V0LFcwZu2Kt3mIFVNXNKa2p3HfvJywazbEH8dfZmcfW2SMYeuHDJJ1M8Ipwc8JZql-jp2JVKl9MjVrbnECVinly5xHBefNM0uXGWpu7J4DZs9HkFN90nhqMWbiV5cHYRmm5dpY37bTAH+wBi2wLNb2sx13T83df2wLRtW9aM4sY-592KFj72LF9xPHeJiDgEacAID0IA"
    width="100%"
    height="380"
    title="Více komparátorů s kodérem - Falstad"
    loading="lazy"
    style="border: 1px solid #ddd; border-radius: 8px;">
</iframe>

Můstek můžeme postavit dvěma způsoby:

### 1. Kombinovaný můstek (P-MOS + N-MOS)
V horní větvi ($S_1, S_3$) jsou použity tranzistory s kanálem **P**, v dolní větvi ($S_2, S_4$) s kanálem **N**.
- **Výhoda:** Velmi snadné řízení. N-MOS se otevírá kladným napětím proti zemi na hradle ($G$), P-MOS se otevírá naopak tehdy, když hradlo uzemníme.
- **Nevýhoda:** P-MOS tranzistory mají kvůli fyzikální podstatě (nižší pohyblivost děr oproti elektronům) přibližně 2x až 3x větší odpor v sepnutém stavu ($R_{DS(on)}$) než N-MOS. Pro velké proudy jsou proto nevhodné a drahé.

### 2. Čistě N-MOS můstek (4x N-MOS)
Všechny čtyři spínače jsou realizovány pomocí tranzistorů s kanálem **N**.
- **Výhoda:** N-MOS tranzistory jsou levné, efektivní a mají extrémně nízké ztráty.
- **Konstrukční oříšek (High-Side Bootstrapping):** Aby se N-MOS tranzistor v horní větvi ($S_1$ nebo $S_3$) zcela otevřel, musí být napětí na jeho hradle ($G$) o cca 10 V **vyšší než napětí na jeho emitoru/source ($S$)**. Jenže v sepnutém stavu je na source tranzistoru plné napájení $V_{cc}$! Potřebujeme tedy na hradlo přivést napětí vyšší než je samotné napájecí napětí obvodu (např. $V_{cc} + 10\,V$). K tomu se používají speciální budiče (Gate Drivers) s tzv. **nábojovou pumpou** (bootstrap kondenzátorem).

---

## Podrobnější pohled: Ochrana a parazitní jevy

Motor je ve své podstatě obrovská **cívka** (indukčnost). Jak už víme z minulé otázky, cívka nesnáší prudké změny proudu.

### Zhášecí (freewheeling) diody
Když tranzistory v H-můstku prudce rozepneme, indukčnost motoru se pokusí udržet proud a vygeneruje obrovskou napěťovou špičku opačné polarity. Pokud by v obvodu nebyly ochranné diody, toto napětí by prorazilo přechody tranzistorů.

Každý tranzistor v můstku proto musí mít paralelně k sobě připojenou rychlou diodu v závěrném směru (u MOSFETů bývá tato dioda již integrovaná přímo ve struktuře čipu – tzv. *Body Diode*, avšak pro vyšší frekvence se k nim často přidávají externí, extrémně rychlé **Schottkyho diody**). Tyto diody umožní bezpečné odvedení nahromaděné energie zpět do napájecího zdroje nebo filtračních kondenzátorů.

### Dead Time (Mrtvý čas)
Tranzistory se neotevírají ani nezavírají okamžitě, proces trvá několik desítek až stovek nanosekund. Pokud měníme směr otáčení motoru a bleskově zavřeme $S_1+S_4$ a otevřeme $S_3+S_2$, mohlo by se stát, že se na malý okamžik potkají stav, kdy se $S_1$ ještě nestihl zcela zavřít a $S_2$ se už začíná otevírat.

Abychom zabránili destrukčnímu zkratu (*shoot-through*), mikrokontrolér (nebo budič) musí mezi vypnutím jedné větve a zapnutím druhé vložit kratičkou pauzu, kdy jsou **všechny tranzistory prokazatelně vypnuté**. Tato pauza se nazývá **Dead Time**.

---

## Regulace rychlosti pomocí PWM

H-můstek sám o sobě umí měnit jen směr. Jak ale zajistíme, aby motor běžel např. na polovinu výkonu? Využijeme **pulsně šířkovou modulaci (PWM)**.

Místo toho, abychom tranzistory nechali sepnuté trvale, budeme je velmi rychle (např. s frekvencí 20 kHz) zapínat a vypínat. Motor má velkou mechanickou i elektrickou setrvačnost, takže tyto pulsy vyhladí a reaguje na **střední hodnotu napětí**.

- Výkon určujeme pomocí **střídy (Duty Cycle)** v rozmezí 0 % (vypnuto) až 100 % (plný výkon).

> **Pro zvídavé:** Proč používáme pro regulaci otáček PWM a nesnižujeme napětí lineárně (třeba reostatem nebo výkonovým tranzistorem v lineárním režimu)? Odpovědí je **účinnost**. Když je tranzistor plně sepnutý, má téměř nulový odpor, a tedy nulový úbytek napětí ($P = I^2 \cdot R \approx 0$). Když je plně vypnutý, protéká jím nulový proud ($P = 0 \cdot U = 0$). Tranzistor v režimu spínání téměř netopí. Pokud bychom napětí snižovali lineárně, tranzistor by fungoval jako topné těleso a spálil by obrovské množství energie na teplo.

---

## Integrovaná řešení (Monolitické budiče)

Stavět H-můstek z diskrétních (samostatných) tranzistorů pro menší výkony je neekonomické a složité. Proto se často sahá po hotových integrovaných obvodech:

- **L293D / L298N:** Absolutní klasika v učebnicích robotiky. Obsahují bipolární tranzistory. Jejich obrovskou nevýhodou je velký úbytek napětí (klidně i 1,5 až 2 V), který se promění v teplo, proto vyžadují masivní chladiče.
- **TB6612FNG / DRV8833:** Moderní budiče na bázi MOSFETŮ. Mají minimální vnitřní odpor, hřejí zanedbatelně a nepotřebují chladič, i když jsou rozměrově mnohem menší.

| Vlastnost | Bipolární můstek (např. L298N) | MOSFET můstek (např. TB6612FNG) |
| :--- | :--- | :--- |
| **Ztráty (úbytek napětí)** | Vysoké ($ pprox 1.5 - 2\,V$) | Velmi nízké ($R_{DS(on)} \approx \text{miliOhmy}$) |
| **Zahřívání** | Vyžaduje velký hliníkový chladič | Téměř netopí při nominálním proudu |
| **Maximální frekvence PWM**| Nižší (jednotky kHz) | Vysoká (desítky až stovky kHz) |

---

## Závěrečné shrnutí aplikací
H-můstek najdeme všude tam, kde je vyžadován obousměrný pohyb:
- **Pohony robotů** (řízení kol a pásů).
- **Krokové motory** (každá cívka krokového motoru vyžaduje pro plnohodnotné řízení svůj vlastní H-můstek).
- **Měniče napětí (Invertory):** Zde zátěží není motor, ale transformátor. H-můstek střídavým spínáním vytváří ze stejnosměrného napětí (např. z 12V autobaterie) střídavé, které se následně transformuje na sinusových 230 V.

---

## Zdroje

Malina, Václav: Poznáváme elektroniku

Vondra, Martin: Elektronika – Součástky a obvody

Sedra, Adel S. & Smith, Kenneth C.: Microelectronic Circuits.