# Otázka 19 - A/D a D/A převodníky

## Slovo úvodem

A/D a D/A převodníky, jak již název napovídá, převádí analogové hodnoty signálů na digitální a naopak. Toho dosáhnou dvěmi základními funkce - **diskretizací** a **kvantováním**.
- **Diskretizace** znamená převod signálu ze spojitého do diskrétního, tj. "rozsekaného" na časové vzorky (např. každou 1ms). Je to stejný rozdíl jako mezi vektorovou a rastrovou grafikou - křivky jsou spojité, bitmapa ne. 
- **Kvantování** znamená převod spojitého rozsahu hodnot na diskrétní množinu, tj. "zaokrouhlení" na nejbližší hodnotu z měřícího rozsahu převodníku (např. 10-bit ADC v Arduinu UNO má rozsah 0-1023, takže krokujeme cca po 5mV).

Když tahle pravidla aplikujeme $(A\rightarrow D)$, můžeme nějakou dobu signál zaznamenávat a následně ho v PC dále zpracovat - pokusit se dokreslit chybějící části mezi body, odhadnout původní tvar signálu, nebo použít algorytmy pro zpracování signálu (filtry, Fourierova transformace, atd.).

Pokud na to jdeme opačně $(D\rightarrow A)$, můžeme z digitálních dat vytvořit analogový signál, který se nám převede do spojitého (ne, diskrétní v přírodě nenajdeme). O spojení těchto bodů se starají různé filtry a to už chtěné či nechtěné (RC/RL filtry, ale i parazitní vlastnosti vedení atp.). Proč myslíte, že zvuk z telefonů zněl tak špatně? A proč vytáčené připojení bylo tak pomalé? To už ale moc odbočuji.

> Pro jednoduchost zde budu dodržovat nap. úrovně "klasické" TTL logiky, tj:
> - log. 0: 0V (validní 0-0,4V)
> - log. 1: 5V (validní 2,1-5V)
> - Provozní napětí: 5V
> - Zakázané pásmo: 0,4-2,1V (kdy může dojít k nejednoznačnému chování)
>
> Samozřejmě existují i jiné úrovně, např. 3,3V logika, 1,8V, pro CMOS se používalo i 12V, atd. Ovšem čím nižší napětí, tím menší spotřeba, rychlejší přepínání apod. 

## A/D převodníky

První částí základu kažého převodníku je komparátor, který dělá jedinou věc - porovnává. Porovnává vstupní napětí s nějakou referencí a říká nám, jestli je vyšší (log. 0) nebo nižší (log. 1). 

![Komparátor](images/19-komparator.png)

### Flash ADC (paralelní komparátory)

Teď dokážeme zjistit, zda-li je vstupní signál větší než 1V. Tak jich přidáme více. A trochu interaktivněji.

<iframe
	src="https://www.falstad.com/circuit/circuitjs.html?ctz=CQAgjCAMB0l3BWEAWB0DsZnMwZgEwBsAHAJySkgKRUq5UCmAtGGAFACG4Y+46hIfJGJ8BlJDTDx44aCOThpkNgCVuvMIRrFJWqPuQ0FNE9ARsA5uAH58CzYMP7lAeUHDRghALD9w4NjchEXxvLxswiHY1Vl47bRp45xQaehMoM051cPcQsPF9KSVZEXoi+CzYlAdg6rFaSSVJOX9yuFVswwSU9KNJZJhzII9kGrDRnwDh0twIgVxZ1o6qgm7V5KdeXsyuFcXahfqJRWKwFo0lNgB3FBEwUg0ecAeoa9vn3mQQ9C23r8Eftl8IDlDd-sDPqUEL8wVDHrxcNDXrCQIjIXQYe9kAROjjlL50fcth99OgSg1nGYQAA1AD2ABsAC4cCwMNiGei4SD2bAgH5GPHuAD6hGQQsgQp4+HIQrQ8FwxGQpFI6CVyuV4tgcDAQpYIqFQiFuCN4qFYolUlNpHFbCAA"
	width="100%"
	height="380"
	title="Více komparátorů - Falstad"
	loading="lazy"
	style="border: 1px solid #ddd; border-radius: 8px;"
></iframe>

Nyní máme funkční převod z analogového signálu na 4-bitový digitální výstup, který ofšem není binární. Máme 4 převody, 4 výstupy, 4 úrovně. Pokud bychom taková data četli nějakým počítačem, dokážeme je již na bin. hodnotu převést, ale to za nás může udělat i hardware. V další ukázce jsem přida převoník 1z7 na 3-bit binární výstup (nejedná se o multiplexer, ale o převodník. Multiplexer podle bin vstupu vybírá 1zN vstupů a pouští jej na výstup, např. [CD4052](https://www.ti.com/lit/ds/symlink/cd4052b.pdf)). Také jsem v následující ukázce zapojení obrátil (koukněte na operační zesilovače), což efektivně udělalo negaci jejich výstupu

<iframe
    src="https://www.falstad.com/circuit/circuitjs.html?ctz=DwYwlgTgBAZgvAIgIwKgFwM6IAwDpsEECsqYIiALEbgOxIUV0DMATAGwAcAnNl6iACNERbKgAOQhBSaoAbhGGoAtpmEBTALRIUAPgBQUKMABKUAB6JtLKEjbYoHe7dGwcqAO7wELpQEMzspQIAPT6hsAA5uaWbFAsLBQ2sQkuXqKhBkYA8tFSrDY0sRSOBWyoXihQGOTIIWHZudLWLNgcUMX2LRzllqjVvRnhphbISM0U9iUpPd4eacr+gQgyg0bDlmPtBA72E6luUJ4HfgED9cA5I01xE+1TEzOV-bWrJrlWUKyT9l8zLkezKAnJYsOqZYDuRptJBcawfGGg1yzV6Qq7Q2F3OI0RHzFFQrFwzYsbF-MHhVGUNrE6zFT5EHFuPFoumE6xMemkpmUlmYpqc84UqRta4fPlI9LnABqvggxl8YAANviEVAnLDSYcvDRygoECxcDIgYtFFU0IhJQB7BVoXwRNRkowAZRAFrEalyRE2zigsOFxVJ9XCFqgagAdpYSFUxIg2BQZmYWthEdGEFoEIHDEYxFAli5niRVpmsznEIbnnhCChC5ngNm1IhEbm+jUCxnwnXS3IDvmHUXayGY13AT3q8BghbzsFna61OcQAqlFBQ0pEAATNQwXwAV2tGrA4YQABEaAAaQ9sM9EM8UM9MM8sM+VC2IACKD5fSBPL5cYAqFpgNDoMGABCACSABy6ZIAA-LBcFwNoSB6NBMFwdBCFINgyEoWhCHYEhcGoehmFYWhqFwPhBFkeh+GkWhKEUfheiECxjHYGO85KHOSojEwTCxEghSfBwiSCWU4rKM+CDrpuO5oA6wC+O8XpCV0pQzN0RomkoYAHBEviWCxErgoKaliQS6kSVyeqtHERDJLcLD2fyJm5CkdkOT82BxlZApubcTDeZ8-GfN5Lnkm52IWXxyQkr5rkjNSFlJWJ4VGKZtkxcFsQxWlEJubZFC2KFiRFeJuJ+bxQVlSVnycHlgqBYk-FtFlLV5UpIwfE5yS2T1GkLNpumAvphksQpnUbGyIVqblSKaX4Q16QZyBGRNyk0sVallQNWkIJGOnLWNhBghxkD6EAA"
    width="100%"
    height="380"
    title="Více komparátorů s kodérem - Falstad"
    loading="lazy"
    style="border: 1px solid #ddd; border-radius: 8px;">
</iframe>

> Pokud chcete, můžete si převodník dostavět Jakou binární hodnotu mají výstupy Qn?

Jako poslední už potřebujeme pouze 2 úpravy:

1. 4 napěťové reference znamenají 4 přesné stabilizátory s odrušením pro každou úroveň. Lepší použít jeden stabilizátor a druhou základní část každého A/D či D/A převodníku - **dělič napětí**. Ten můžeme zapojit buď na referenční úrovně, nebo na vstupní signál. V obou případech nám zajistí přesné úrovně pro porovnávání.

> Jak se liší vstupní parametry A/D převodníku s děličem napětí na vstupu aa na referenčních úrovních? A k čemu by mohl být dělič napětí na ref. úrovních náchylný?

2. Kvantizaci na 4 úrovně jsme již provedli, ale stále nám chybí diskretizace. Co kdybychom postavili 16-bit převodník, ale mohli číst jen 8-bit hodnoty? Museli bychom číst po polovinách, což ale znamená časovou prodlevu mezi daty, kde může v signálu dojít ke změně. A nebo potřebujeme číst v přesný časový okamžik, zatímco CPU dělá něco jiného. 

    V takovém případě nám pomůže nějaký vzorkovací obvod, který si celou hodnotu v jeden okamžik uloží a my ji pak můžeme číst klidně i později. Zde nám stačí i obyčejný registr.

<iframe
    src="https://www.falstad.com/circuit/circuitjs.html?ctz=CQAgjCAMB0l3BWEAWB0DsZnMwZgEwBsAHAJySkgKRUq5UCmAtGGAFADmIxNyP3vUoShQ2AdxTFwpfODCywM0RL7TZq-OlmRxkkJoXz9W5XoN7cCbbtWXDsu6dtW9yAk6lv7da2BOrFbTURdH1oKSQaKOgkADUAewAbABcAQw4GNgBCEAATBgAzVIBXFJEAEXQAGnLCGoQa5BrcGvwaiABFNo6wKo6aMHiC9AAdAGdk+PGAIQBJADlwAH4V1ZGAR1YwEYA7JbBVlY3WSF2Vg7XNyG2988uwODPVi43rm8P9pdeHp8Pt9bgN3gwNejx2bHwkCkuFwwj8wlwxGQ4HQwho+SKpWSIkibFScgUqP0UJRwgiIgewN4YSklPgukhtKJ5nhpkZ+gQwnwyBo+E5bJ5HK5gtwkGROgk5nMMK5JglxOhsJAMuVSvlLOZJnM6pFYtVCL16pJyDAsvUprZ-gt0pIloctpVsKkOnxrFkfK5JI93FoAypvOgpCDwZDoZp4CpeIJ+oVMfJfqp4EDoZTwfo+HCEeBUbdKGtxot8azwKgydTKdCGdpkdNEWw4HrhG5DeR6l9InlXlJVHrrM77nZCHr7P77sFQ9bgp0AHkQIRBaySEy4eA2LP57ySUvYxB2OvBdyaNvD+BV2NJLyTBPjG2IEVEmMGCAAMoAQViAFE2AAlC83lDzv+UQoDQkQdjEbAAE4COAhA0PwJ4Jjo0EIYK-AEMBdJQTBGEwTymH0ihvBwHh-BIdh-CmvB1EUvSEiUXB0ZUaYqEDEYiG6OhkLRrh8r8Ph0YCTov78KJR7iiI44dqWCBsEAA"
    width="100%"
    height="380"
    title="Celý A/D převodník - Falstad"
    loading="lazy"
    style="border: 1px solid #ddd; border-radius: 8px;">
</iframe>

### Integrační ADC (s RC obvodem)

ADC v minulém příkladu je sice jednoduchý, ale velmi špatně se škáluje. Pro N bitů potřebujeme $2^N-1$ komparátorů (**to je hodně**).

Ne vždy potřebujeme okamžitou odezvu, kterou nám minulý ADC dovoluje. Za cenu času můžeme postupně nap. referenci měnit a postupně tak projít všecny možnosti. To nám umožní použít pouze jeden komparátor a nějakou formu **integračního obvodu** (např. RC článek). Abychom se vyhnuli problémům s linearitou, budeme uvažovat, že náš integrátor napájíme v režimu CC (konstantním proudem), viz [otázka 13 - dodatek k přechodovým dějům](13-pasivni-elektronicke-prvky.md#dodatek-k-přechodovým-dějům).

V simulaci níže je nastíněn základní princip (integrátor nahrazen generátorem pilového sig. 100Hz, ampl. 2,5V, referenční napětí 2,5V). Komparátor jej porovná se vstupním napětím a výstupem je log. 1/0, pokud je vstup větší/menší než integrátor. No a jelikož výstup integrátoru je periodický se známou frekvencí, Můžeme jednoduchým poměrem $T_{ON}/T_{OFF}$ odhadnout celkem přesně vstupní napětí (samozřejmě záleží na linearitě integrátoru nebo jeho mat. modelu pro přesné odhadnutí).

<iframe 
    src="https://www.falstad.com/circuit/circuitjs.html?ctz=DwYwlgTgBAZgvAIgIwKgFwM6IAwDpsEECsqYIiAnPtkgOxIDMjxATEgBwpQgBGiR2VAAc+CACwNUANwj9UAW0z8ApgFokKAHwAoKFGABDKAA9EDBgDYoLFmKgSW126ngJ2Cg3KjywOVAHNPZEICBAB6HT1gACUTM0trbHZrdmSWJJdEJAtUAHdXMRdZYMFvA2MpRBZcEigeMAMsBGqSCN19ADUDCGiDMAAbOIRzK1tsazFxsczkHKh8xFois1wkWvlyyoRajDREDoB7frQDf2VwyP1coYcnOzF2KedYPzaogGUQA6FlG4orJBiOy0dJQBjYQovBCCS5RA5QZQAOyyqAwQiyc1cxnS2EkUHRCHUCFhen0QigW1KGHI22ouMBtDEtAEBCYF3apLJFLMqJpeEIKDenK5yh53OhvP4dKYTKZLPp7OFIrFWzx1JwdMFJKi5NFzWkfig6tphBljOZpq1HNJwF1VQNw0l0M1iptYQOl2AYU+32UOi94AgOiAA"
    width="100%"
    height="380"
    title="Princip integračního ADC - Falstad"
    loading="lazy"
    style="border: 1px solid #ddd; border-radius: 8px;">
</iframe>

Měření $T_{ON}/T_{OFF}$ můžeme provést čítačem synchronizovaným s integrátorem. A aby celé zařízení počkalo, než se uráčíme vyčíst hodnoty, přidáme S-R klopný obvod, který čítání až do resetu zastaví.

<iframe 
    src="https://www.falstad.com/circuit/circuitjs.html?ctz=DwYwlgTgBAZgvAIgIwKgFwM6IAwDpsEECsqYIOuALABwDsSSAbEQJxsBMlRltAzLahAAjREWyoADiISVeqAG4RRqALaZRAUwC0DBAD4AUFCjAASlAAeiXr0ZR22avepOH1VPGSNUAd0+UPJWQCVQBDC3lEdlwSKCEwUKwEaJIAekNjYAA1UIhTULAAG0trW3tKbHLKznFYRCZfTwFYIN5cJFiVcMiEWIw0RCyAe0K0UIBzDQR0oxMfEpledntOKBpqzg8caYyTAGUQIYkNBZr7WmXKGjWGuoRxXcyhqA0AO22oDAl67zuLB2wcig3wQOn0s2MmQkUB6tQw5F6+AISGolDYtDSj0hwGhPSB8IohBQM0h2OhGiiCg+BMRRNR6MxELJL0pMOsqBpeCJOyZUJZyCp9w5CKISOwKLRLAxPNJfIpArZCHxCK5yJl2NSQ12wFSByOGm1IDQ0CsCAulSQtDstFRUEtv08tXiiACUDA7wQMFChQwUygKiG2xJJnMppsdiY1RcdsYtU8tz8rJgQUjtS6ESiMVQ8USmcZmQAgq8ACYLWNOe1Qc12q1bIXB0CFFRQV4qRCmLR7KCFUJoEAACzrtXdiD2ABooKZUIGEABFCevWekTwdrs9vuDvQAfi3UAIcHFBiQlR3cGPBnFUFPh4YV63B+wF8qBYAQnBXzqQE3DcVTesVpQUBEOwribHcaYzqu3a9gO6rAPMprlnaLDLEh7BEA6QbaghohWvYGFQGhGFDnBOEIEhkZQOGMZxlhszwQs1bsBcVYOFR2Cuo6pGMWxvAcWsjCAXxnF0ZkZGUIJ7GARJgHoZh9bYQs-5yQJsnEeB3F-pJKkyXaVwkQ2ZFEHh7CrMZEb6RpDYADJKZJSBXKpdpIOwBnagAsgs5l6YB3kMK5VnaqECzUaZ0lLABdYsGEyj+mAHzjKE9SECEDZ7Bo8hvOl4wACIaIcxYaCaiDUEwNZ2ChFa1hpcTxTIHLjAMCn0RgGClqaLCOZWx6rPaJG1YgzRCElZqoBopq1MWdXiIZCydUJ-HHo4UlufRZHzVRZTHhUm3yTNimmttlTUUdK2BWtc2ObYFbYCx12rWJCzHndjA3XdHEPSYFhKewFW+dgFXNFxnx1WBaDyqYACieyQwAKnB32mtwTgsLwhGWlALB7RyoOuuDiA5QA8gAcpDPKfpAhhAA"
    width="100%"
    height="380"
    title="Integrační ADC s čítačem - Falstad"
    loading="lazy"
    style="border: 1px solid #ddd; border-radius: 8px;">
</iframe>

Toto zapojení je již principiálně složitější. Jako převodník času na digitální hodnotu se používá 4-bit čítač, který se synchronizuje s integrátorem. Frekvence čítání by měla být $2^N$ krát vyšší než frekvence integrátoru, aby se využil celý rozsah čítače. V našem případě je $2^4=16$ x vyšší. Výsledné napětí pak můžeme odhadnout jako $V_{in} = (T_{ON}/T_{OFF}) \cdot V_{ref}$, kde $V_{ref}$ je napěťová reference převodníku (aka maximum signálu z integrátoru).

> Při 3,2V vstupního napětí zobrazí ADC hodnotu 'b' (11 v desítkové soustavě), jelikož $T_{ON}/T_{OFF} \cdot 16 \approx 10,24$. Správně by tedy mělo být zobrazeno 'a' (10 DEC), ale model čítače v použité simulaci začíná od 1, ne od 0. Náš výstup je tedy vždy o 1 vyšší.
> Úrovně jsou rozděleny rovnoměrně po $1/N$ částech rozsahu.
> Díky linearitě si při výpočtech můžme pomoci a pro výpočet výsledného výstupu lze místo $T_{ON}/T_{OFF}$ použít jen poměr napětí $V_{in}/V_{ref}$.

## D/A převodník

D/A převodník dělá přesný opak a převádí binární hodnotu na analogový signál. Nejjednodušší způsob jak převést pevnou hodnotu napětí na nějakou jinou (nižší), je odporový dělič. Jednotlivé bity můžeme použít jako spínače, které "přizemní" jednotlivé rezistory. A hodnoty vypočteme úpravou základního vztahu pro nap. dělič:

<div style="width: 100%; display: flex; justify-content: center; align-items: center;">
    <div style="width: 50%; display: inline-block; text-align: center;">
        $$V_{out} = V_{in} \cdot \frac{R_2}{R_1 + R_2}$$
        $$\frac{V_{out}}{V_{in}} = \frac{R_2}{R_1 + R_2}$$
        $$\frac{V_{out}}{V_{in}} \cdot (R_1 + R_2) = R_2$$
        $$\frac{V_{out}}{V_{in}} \cdot R_1 + \frac{V_{out}}{V_{in}} \cdot R_2 = R_2$$
        $$\frac{V_{out}}{V_{in}} \cdot R_1 = R_2 - \frac{V_{out}}{V_{in}} \cdot R_2$$
        $$\frac{V_{out}}{V_{in}} \cdot R_1 = R_2 \cdot (1 - \frac{V_{out}}{V_{in}})$$
        $$R_2 = R_1 \cdot \frac{\frac{V_{out}}{V_{in}}}{1 - \frac{V_{out}}{V_{in}}}$$
    </div>
    <div style="width: 50%; display: inline-block; text-align: center;">
        <iframe
            src="https://www.falstad.com/circuit/circuitjs.html?ctz=DwYwlgTgBAZgvAIgIwKgFwM6IAwDpsEECsqYIiSeATAVQOx0DM2AHFQGwCcndqIARoiLZUAB0EIALI1QA3CENQBbTEICmAWiQoAfACgoUYBigAPCu2xRGLSVCSXrNVPAQiooiggD0+w8GhzZEcHK1CoKkl3V3cFZEIfPyNAiytIsMdGZ1gcVDiqYUSDZLNEGhYIqIjWJ2jcqDj2Jtx2Xl9igNKEAvZKtKJerLq3PIphEXb-FIRmO3TrbDshl3q4qIIi-xMg8utbaorlnJGPL0mjbbKBvbnro5ixM6TjLtmbhaXsh9PkTaMAdy64Xmu3SKxG52AgJ2NRB1zBxwmz2hV168zeCIekJRM0WfWs7AqmLKf2AACUgSEqWEqCxwQ5UP9vkoAIamWSKSEAc0pVhsdnC63BSI6PJhh32uyFiNJYtR7x6UGlWOectxS32b2VuXawG84Ag+iAA"
            width="100%"
            height="380"
            title="D/A převodník - Falstad"
            loading="lazy"
            style="border: 1px solid #ddd; border-radius: 8px;">
        </iframe>
    </div>
</div>

Takto můžeme jednoduše vytvořit 4-úrovňový ADC. Nevýhodou jsou potřebné různé hodnoty rezistorů a pouze 4 úrovně, zatímco 4-bitová hodnota může mít až 16 různých kombinací. Navíc zde výstupy pouze "přizemňujeme" a neaktivní bity musí být odpojeny aby neovlivňovaly výstup.

> U nap. děliče platí, že každý rezistor s odlišnou hodnotou ovlivňuje výstup jinou váhou (z definice) a hodnoty rezistorů lze sčítat pro jejich navýšení. U binárního čísla každý bit reprezentuje také nějakou váhu. Toho lze využít.

### R-2R síť

R-2R síť je elegantní způsob, jak vytvořit D/A převodník s pouze dvěma hodnotami rezistorů (R a 2R) a využívá principů popsaných výše. Každý bit je reprezentován dvěma rezistory, které jsou buď připojeny k zemi (log. 0) nebo k napájení (log. 1) a vzhledem k tomu, že jsou zapojeny za sebou, s přibývajícími rezistory se síla ovlivnění zmenšuje o polovinu, stejně jako v binárním systému.

> R-2R síť se většinou znázorˇuje s invertujícím operačním zesilovačem na výstupu, který odděluje zátěž od rezistorů aby nedocházelo k jejich vzájemnému ovlivňování. Ovšem, *KDO V HOBBY ZAPOJENÍCH POUŽÍVÁ SYMETRICKÉ NAPÁJENÍ ABY MOHL POUŽÍT INVERTUJÍCÍ OPERAČNÍ ZESILOVAČ*? Já rozhodně ne. Takže otočíme vstup a výstup a invertující OZ za napěťový sledovač (neinvertující OZ se zesílením 1).

<div style="width: 100%; display: flex; justify-content: center; align-items: center;">
    <div style="width: 50%; display: inline-block; text-align: center;">
        D/A převodník R-2R invertující
        <iframe
            src="https://www.falstad.com/circuit/circuitjs.html?ctz=DwYwlgTgBAZgvAIgIwKgFwM6IAwDpsEECsqYIiSeATAVQOx0DM2AHFQGwCcndqIARonYAWVAAdBCItlQA3CIhJQAtpkUBTALRIUAPgBQUKMACGGKlAAeFdtihJhw+7ahVhM2DlQQA9gDtEGm8fGHhkQgjCVDQAC0DcEgB6AyNTcytA93tHVyy3DzCPXwCEIKhfUIpIyOi40oSEZMNjMwtrBEYabKdOu3zUQuCSsoqwymqo9DqqBqbUgHMM5Bz87tcWFgGvOeNF9qo3XL7Dqg2thBkd4D3EZidVu-XNzwvGlOMAdyWkOnZ7TgsSAB-yo50u72AX3aPz+qxhriI7DBb2akO+vwRsMRmORVyhgWxVEJhPcuIh+NKxL+jEYWKRL3BqIpNLpUBZRzJTO+wKBgOBvU5qQpRL+vNcdD5oIZKKFS3okvFFgF0rxS3ZYsYRElgs+aq1ILZ+uVgyuABluUquhqtTrgOb9hK2V15YapSaIfbbkaupqlTaVRDoNCXA4nEgXCwCl5ylUIjLjEHMnZQ0coJHkTHwnGromOlacr001HXpnxlEc98I30sunpZnpOXA3Ka3ZC7XBvXs032m27O47O3owos43UTcEP2i1BJzo3dtyUthOHMdPlwdRAGue0tSxXIcd4rbQB5JYHl1EYHy84oKAYcjIeNonu0ldLum23NvvdOM9uDPD6Rxkfccv1OXcv2NedURMRc10dM8JQzZQTEUVBlDARBNCUeYUJHAhH1zcMB2Iot-0ULtUVzSMp2o0MyLwxlUlaJZaJyaj+jrYpAiKEIxgmSZYniJIF3aThRR5JBtU3WVoUkg1ZydYtGN2JYRFTNSwNtT1kDkwsFN9DMxAoR8ACUWJIzpSLrD4O2QyxZFQ1VRNhLIxJxaTdWcld4RFTlgEScAIAMIA"
            width="100%"
            height="380"
            title="D/A převodník R-2R invertující - Falstad"
            loading="lazy"
            style="border: 1px solid #ddd; border-radius: 8px;">
        </iframe>
    </div>
    <div style="width: 50%; display: inline-block; text-align: center;">
        D/A převodník R-2R neinvertující
        <iframe
            src="https://www.falstad.com/circuit/circuitjs.html?ctz=DwYwlgTgBAZgvAIgIwKgFwM6IAwDpsEECsqYIiSeATAVQOx0DM2AHFQGwCcndqIARonYAWVAAdBCItlQA3CIhJQAtpkUBTALRIUAPgBQUKMACGGKlAAeFdtihJhw+7ahVhM2DlQQA9gDtEGm8fGHhkQgjCVDQAC0DcEgB6AyNTcytA93tHVyy3DzCPXwCEIKhfUIpIyOi40oSEZMNjMwtrBEYabKdOu3zUQuCSsoqwymqo9DqqBqbUgHMM5Bz87tcWFgGvOeNF9qo3XL7Dqg2thBkd4D3EZidVu-XNzwvGlOMAdyWkOnZ7TgsSAB-yo50u72AX3aPz+qxhriI7DBb2akO+vwRsMRmORVyhgWxVEJhPcuIh+NKxL+jEYWKRL3BqIpNLpUBZRzJTO+wKBgOBvU5qQpRL+vNcdD5oIZKKFS3okvFFgF0rxS3ZYsYRElgs+aq1ILZ+uVgyuABluUquhqtTrgOb9hK2V15YapSaIfbbkaupqlTaVRDoNCXA4nEgXCwCl5ylUIjLjEHMnZQ0coJHkTHwnGromOlacr001HXpnxlEc98I30sunpZnpOXA3Ka3ZC7XBvXs032m27O47O3owos43UTcEP2i1BJzo3dsIQB5JaaYQsKAiKCaSPr0QvFBQDDkZDxtHtVdT7eD15XExLc8bldrkQZ5QmRSoZRgaPzN8jggn3NwwHYCiwzYcG3-Ct2kvEDQzA2NR1SVolm3FNt36OtikCIoQjGCZJlieIknJJZOFFHkkG1AMuWhSiDVnJ1i0ZBYlg3VY2LOajUk9ZA6MLBjfQzMQKBPAAlNVaUxacCBxOsPg7V9LFkd9VXaMjU3UkVbQpTTsXhLSuN1dpHx3Tdz3DbS7zXc9zPpd0aMQEzw2nNcLOo4BEnACADCAA"
            width="100%"
            height="380"
            title="D/A převodník R-2R neinvertující - Falstad"
            loading="lazy"
            style="border: 1px solid #ddd; border-radius: 8px;">
        </iframe>
    </div>
</div>
