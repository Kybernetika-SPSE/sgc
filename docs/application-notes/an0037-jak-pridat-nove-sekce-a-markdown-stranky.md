# AN0037 - Jak správně přidat nové sekce a Markdown stránky

> Částečně vytvořeno pomocí AI (GPT-5.4 + Claude Sonnet 4.5)

> Praktický návod pro přidávání nových sekcí, rozcestníků a jednotlivých Markdown stránek do tohoto průvodce postaveného na Docsify.

## Účel dokumentu

Tento aplikační list popisuje doporučený postup, jak rozšířit tento studijní web o novou sekci nebo o novou stránku v existující sekci. Cílem je, aby nové materiály měly konzistentní strukturu, správně fungovaly v sidebaru a neobsahovaly rozbité odkazy.

## Jak je tento průvodce organizovaný

Web je publikovaný z adresáře `docs/` a používá Docsify. To znamená, že hlavní obsah tvoří Markdown soubory a navigace je řízená hlavně těmito soubory:

- `docs/README.md` jako hlavní úvodní stránka
- `docs/_sidebar.md` jako levé navigační menu
- `docs/<sekce>/README.md` jako rozcestník konkrétní sekce

Typická sekce vypadá například takto:

```text
docs/
  moje-sekce/
    README.md
    tema-01.md
    tema-02.md
    images/
    assets/
```

## Kdy přidat novou sekci a kdy jen novou stránku

Novou sekci přidávej tehdy, když:

- vzniká nový tematický celek
- bude obsahovat více samostatných stránek
- dává smysl mít vlastní rozcestník a vlastní podnavigaci

Jen novou stránku v existující sekci přidávej tehdy, když:

- téma logicky patří do již existující sekce
- nepotřebuje vlastní složku
- jde o jeden konkrétní materiál nebo doplnění

## Postup pro přidání nové sekce

### 1. Vytvoř složku sekce

Nová sekce se zakládá v `docs/`.

Příklad:

```text
docs/moje-sekce/
```

Název složky by měl být:

- krátký
- bez diakritiky
- psaný malými písmeny
- oddělený pomlčkami

Vhodné příklady:

- `application-notes`
- `prakticka-mereni`
- `microcontroller-labs`

## 2. Přidej rozcestník `README.md`

Každá sekce by měla mít vlastní `README.md`, který slouží jako hlavní stránka sekce.

Základní šablona může vypadat takto:

```md
# Název sekce

> Krátký popis, co v této sekci je.

## Co tu najdeš

- [První stránka](prvni-stranka.md)
- [Druhá stránka](druha-stranka.md)
```

Tento rozcestník pomáhá čtenáři i vyhledávání a zároveň poskytuje jedno stabilní místo pro vstup do sekce.

## 3. Přidej sekci do sidebaru

Bez úpravy `docs/_sidebar.md` bude sekce existovat, ale nepůjde pohodlně otevřít z levého menu.

Do `docs/_sidebar.md` přidej řádek například takto:

```md
- [Moje sekce](moje-sekce/)
```

Pokud chceš přidat i přímé odkazy na konkrétní stránky, můžeš pod sekci doplnit další položky:

```md
- [Moje sekce](moje-sekce/)
  - [První stránka](moje-sekce/prvni-stranka.md)
  - [Druhá stránka](moje-sekce/druha-stranka.md)
```

## 4. Zvaž doplnění hlavní stránky webu

Pokud jde o důležitou sekci, je vhodné ji uvést i na `docs/README.md`, aby byla vidět hned na titulní stránce webu.

To není povinné pro každý drobný doplněk, ale pro větší nové části ano.

## Postup pro přidání nové Markdown stránky do existující sekce

### 1. Vytvoř nový `.md` soubor

Soubor přidej přímo do cílové sekce.

Příklad:

```text
docs/application-notes/an0037-jak-pridat-nove-sekce-a-markdown-stranky.md
```

Doporučení pro název souboru:

- používej malá písmena
- nepoužívej diakritiku
- slova odděluj pomlčkami
- pokud jde o číslovaný dokument, nech číslo i v názvu souboru

## 2. Vlož základní strukturu stránky

Pro běžnou stránku stačí například tato osnova:

```md
# Název stránky

> Krátké shrnutí obsahu

## Úvod

## Hlavní obsah

## Závěr
```

Pokud vytváříš aplikační list generovaný AI, musí být na třetím řádku uvedeno využití a modely (pokud možno):

```md
> Částečně vytvořeno pomocí AI (GPT-5.3 + Claude Sonnet 4.5)
```

Příklad začátku AI generovaného aplikačního listu:

```md
# AN0037 - Jak správně přidat nové sekce a Markdown stránky

> Částečně vytvořeno pomocí AI (GPT-5.4)

> Praktický návod pro přispěvatele.
```

## 3. Přidej odkaz do `README.md` dané sekce

Nová stránka by se měla objevit v rozcestníku příslušné sekce. Například v `docs/application-notes/README.md`:

```md
- [AN0037 - Jak správně přidat nové sekce a Markdown stránky](an0037-jak-pridat-nove-sekce-a-markdown-stranky.md)
```

Bez této úpravy sice stránka technicky existuje, ale čtenář ji hůře objeví.

## 4. Volitelně přidej odkaz i do sidebaru

Pokud je stránka důležitá nebo má sloužit jako často používaný návod, můžeš přidat přímý odkaz i do `docs/_sidebar.md`.

To se hodí zejména pro:

- rozcestníky sekcí
- často používané návody
- klíčové studijní materiály

## Odkazy, obrázky a soubory

Při psaní nových stránek dodržuj tyto zásady:

- obrázky ukládej typicky do `images/`
- ostatní soubory ukládej typicky do `assets/`
- pokud sekce funguje jako rozcestník, používej v ní `README.md`

### Jak fungují cesty v Docsify

Díky nastavení `relativePath: true` v konfiguraci Docsify platí:

- **Relativní cesta** (bez úvodního lomítka): `file.md`, `../dir/file.md`, `images/pic.png`
  - Cesta je relativní k aktuálnímu souboru
  - Funguje jako běžné relativní cesty v souborovém systému
  - Použij `../` pro přechod o úroveň výš

- **Absolutní cesta** (s úvodním lomítkem): `/mo-jirka/file.md`, `/assets/file.pdf`
  - Cesta je relativní ke kořenu `docs/`
  - Nezávislá na poloze aktuálního souboru
  - Vhodná pro důležité odkazy, které se mohou použít odkudkoliv

### Příklady odkazů

Z `application-notes/an0037-jak-pridat-nove-sekce-a-markdown-stranky.md`:

```md
[Zpět na rozcestník](README.md)                    ← relativní (v téže složce)
[Jiná sekce](../mo-pavel/README.md)                ← relativní (o složku výš, pak do mo-pavel)
[Otázka 13](/mo-jirka/13-pasivni-elektronicke-prvky.md)  ← absolutní (od docs/)
![Schema](images/schema.png)                       ← relativní obrázek
[Zadání PDF](assets/zadani.pdf)                    ← relativní soubor
[Archiv](/archiv/README.md)                        ← absolutní odkaz
```

## Doporučený pracovní postup

Prakticky se osvědčuje tento sled kroků:

1. Rozhodnout, zda jde o novou sekci nebo jen o novou stránku.
2. Vytvořit složku nebo Markdown soubor.
3. Přidat nebo upravit `README.md` v dané sekci.
4. Upravit `docs/_sidebar.md`, pokud má být obsah snadno dostupný z menu.
5. Zkontrolovat relativní odkazy, obrázky a názvy souborů.
6. Ověřit, že AI generovaný aplikační list má na třetím řádku správný tag.

## Nejčastější chyby

- soubor je vytvořený, ale není nikde odkazovaný
- sekce nemá vlastní `README.md`
- v názvu souboru je diakritika nebo mezery
- záměna relativní a absolutní cesty (relativní bez `/`, absolutní s `/` na začátku)
- obrázek je uložený jinde, než kam vede odkaz
- AI generovaný aplikační list nemá na třetím řádku požadovaný text

## Rychlý checklist před uložením změn

- existuje správná složka v `docs/`
- nová stránka má smysluplný název souboru
- sekční `README.md` obsahuje odkaz na novou stránku
- `docs/_sidebar.md` je upravený, pokud je to potřeba
- odkazy používají správný formát (relativní bez `/`, absolutní s `/`)
- obrázky a soubory jsou na správných místech
- AI generovaný aplikační list má na třetím řádku `> Generated by AI (GPT-5.4)`

## Závěr

Správné přidání nové sekce nebo Markdown stránky v tomto průvodci není složité, pokud se dodrží několik jednoduchých pravidel: rozumné názvy složek a souborů, rozcestníky přes `README.md`, aktualizovaný sidebar a správné použití relativních (bez `/`) a absolutních (s `/`) odkazů. Díky tomu zůstane web přehledný a nové materiály budou snadno dohledatelné.