# Otázka 20 - Pulzně šířková modulace (PWM)

Pulzně šířková modulace (PWM) je technika používaná k imitaci analogového signálu pomocí digitálního výstupu. Signál rychle přepíná mezi vysokou a nízkou úrovní a poměr $T_{ON}/T_{OFF}$ (střída) určuje efektivní hodnotu výstupního signálu. Pak už spoléháme na vyhlazení výstupu buď vlastním zařízením (např. setrvačností motoru), filtrací nebo že výsledné "blikání" nebude pro danou aplikaci vadit (např. u LED diod blikáme mnohokrát rychleji než lidské oko postřehne).

Nyní ale přejděme rovnou k příkladu, na kterém si princip vysvětlíme:

<iframe
	src="https://www.falstad.com/circuit/circuitjs.html?ctz=DwYwlgTgBAZgvAIgIwKgFwM6IAwDpsEECsqYIiAzABy4BsAnLQCzNFNIBMT9SSTqIAEaIi2VAAdhCJhVQA3CCNQBbTCICmAWl4IAfACgoUYAHcoAD0TbaUTlVs27qeAjEB6A0dMWrSR7WwHBzFYHAQPQ2MzSwRrKEYgxmcwiK9o3xtmIOZk13DPKJ9kJiYoLKQAdkz+ULzU42UAV3MivzLSpnsc2pCMdUQOfMjQNGgY7U52qE0s7pcQwTBEGrAAO0QYAEMAGz6VAHswqDkOJWOKJXrgABkijgqOKAoOQI4uJ5fc9wKbu4eoDhUexvUqAqhfIZeW4xe6PDhEGwggEIiFXaEDf5IrFcVE-ABKRU0FGwpTamhkjz8uSpUBMLkGsEUyACIWUm3McgGuBIUEWmywCA43MhhRiTAIUCogRK9iluOG6WkEr4HU6thK8rSf0ez0CxNK+s1ooxcKBTxJAIeRu8MMxCPNoPF1sVsIB731AOw4J6IptJuCDtsVWd2tsgMDKpDtseCQ9vAZ819Lv+WQ9cp9VxA22UUFWymWmkWaCgIH2ynEmwgmzQ+wgEKga0QAEEKAAaKBNjjtptIbvYdsAITbUAHXZHvZHIUOCCbADJNuWANzbNCLgfduDrjuzgDmq4HpBcTELYGLpfLlertb0TYHAGEACId+9PuBQbBIbD6JAAfj-77-H8oDfAgkH0Ht-ybbB-xAj9wIHX9n2g4D3zg287yQZ870CWCwMAoD8JQz9sGANws2UH4syKNM9VoWUQkTKBlGnY8ixLMsKyrGs60zUZWiqKYkTmI5FmWUh1gQLZdnUA4jhOM45AuBASCuRUJkeLJ1PiWgoysD01SJCgbE6XTYgoIyoAM8zHHoBMUh+NS41s6Z9JpRNVMJVzHAE9gdIzH50WQASKCIOF3VC0z4zdUlJhCuy6gc1pYtCoMbDi0ypWiyU9SoGp3IC-i0tyrLqDy+yFSKTLStSp5cutQLKmMtokV8+txEQFA0VDGUspla0AElPItJBnKJYbOHrDBthwYUoAACyWZSkyG0lRus2xbPqlbsumClstMnqot82wJv8iqxTaI7mpRM6vEGsU1XhYy1UaybptcWaFsuRLo0stVjr627jWkNoeuOp6Duu57gRu-LzsQZhAjsKAKgspxakGK4m1WAATbbnmmEadXi75hmxvHxg9BJtGcpIgeAcmih6hIEUCOm4a8RmHvsPxAlZ4J62nFSft8WLHi04SEvhhBEe09okcBUzZeR5WAmtCnfGcgmtOeetmMQHH1C2RoV19DXYiJuWtPZo59YQQ3jdNq5zf5hJZZtvImOnB3NhNtAzaKfneflgWfS9g2jd9p2fgAZVLcR1CZzKkSqewKQhAovH2KB1AklhUAwdqZbKhBzFkKAi+0PRIiMLxxGOI4MHIJb6lr4x685BBy6bmbCGwegqgReERS8Nx9h+Nw4-2BOfkEO4vU9YFxUs2gSd9OfKbowmbG0KhEU-a0N98cMkfYN1vQ54wj6CtKdXoegniMw+mYXohMP5jgGGtFpKaYCppneJoDgn4AEoDDhgRaOJ0D9AQAANX2NsQQmxjgYDQI0cQjRfQ-ysLQf+EwUaBE0BfRukCahoBgbA1B6DVgAFuoA40ANiA2wwCAFhALBrRiocAoE8HgAI-KMQgQMMhMDAAwgDQtAmwWFQAANQV1rPsOQqwACHchJHsIuo8FgUAiD2m4JNUhqByGIHgYg5B4gEGVlPAAT3UR1HRll6CvF4dwcuAiDHQMQIADUAaE4xoSAOhEB1A7jAKgniBhSLgAgAYIAA"
	width="100%"
    height="380"
    title="4-bit PWM generátor - Falstad"
    loading="lazy"
    style="border: 1px solid #ddd; border-radius: 8px;">
</iframe>

Jak si lze všimnout, výstupní signál v pravidelných intervalech přepíná mezi log. 0 a log. 1. Veškeré nastavení je ovládáno řídícím registrem (umístěn uprostřed pod čítačem).

### Řídící registr

| Bit 7 | Bit 6 | Bit 5 | Bit 4 | Bit 3 | Bit 2 | Bit 1 | Bit 0 |
|------|------|------|------|------|------|------|------|
| Střída | Střída | Střída | Střída | Vstupní | dělič | Volba vstupu | Polarita výstupu |

- Střída (Duty Cycle) - 4 bity - nastavení $T_{ON}/T_{OFF}$
  > 
- Vstupní dělič - 2 bity - nastavení frekvence (dělící poměr vstupního signálu)
  > 00 - CLK/16, 01 - CLK/8, 10 - CLK/4, 11 - CLK/2
- Volba vstupu - 1 bit - výběr mezi hodinovým signálem či externím vstupem
  > 1 - CLK, 0 - EXT
- Polarita výstupu - 1 bit - hw prohození $T_{ON}/T_{OFF}$.
  > 0 - normální, 1 - invertovaný


---

Původní text dále

---


# Princip funkce
- funguje na principu rychlého spínání a vypínání signálu, přičemž se mění poměr mezi dobou zapnutí a vypnutí (střída)
- umožňuje regulaci systémů řízených analogovým vstupem (DC motory, LED), k plynulosti je však potřeba dostatečně vysoká frekvence (např. u LEDky by mohlo být viditelné jak bliká)
- (pro pochopení) pokud je střída 50 %, pak se námi spínaný systém chová jako kdyby byl spínán stejnosměrným napětím poloviční amplitudy (adekvátně pak pro střídu 33.3 % je DC napětí třetinové amplitudy, ...).
![20. 50 duty cycle](images/20-50-duty-cycle.png)
![20. 20 duty cycle](images/20-20-duty-cycle.png)

---

# Klíčové parametry
- **Frekvence** - počet cyklů za sekundu
- **Střída (Duty Cycle)** - poměr doby zapnutí k celkové periodě
- **Rozlišení** - počet kroků pro nastavení střídy

---

# Využití PWM
- Řízení rychlosti motorů
- Regulace jasu LED diod
- Řízení topných těles
- Audio zesilovače třídy D

---

# Příklad implementace pro Pico
```python
# Nastavení PWM na ESP32 s MicroPythonem
from machine import Pin, PWM
import time

# Vytvoření PWM objektu na pinu 2
pwm = PWM(Pin(2))

# Nastavení frekvence na 1000 Hz
pwm.freq(1000)

# Hlavní smyčka
while True:
	# PWM s 50% střídou (32767 je polovina z 65535)
	pwm.duty_u16(32767)
	time.sleep(1)
```
PWM signál na pinu 2 s 50% střídou a frekvencí 1000 Hz.

---

# Použití PWM
**Servo** má el. desku, které PWM signál přijme a změří jeho signál v čase.
- Pro polohovací serva (omezená šířka polohy většinou 180 °) tento signál znamená úhel natočení servomotoru
	- například pro ovládání robotických ramen

- U kontinuálního serva (servo co se točí dokola) signál PWM znamená rychlost a směr otáčení.
	- například jak rychle nebo pomalu se bude točit kolo u autíčka nebo ventilátor

**LED dioda** - u LED diody můžeme pomocí PWM řídit jas diody

> Ilustrační obrázek serva v původních podkladech chybí, proto je zde ponechaný jen textový popis.






