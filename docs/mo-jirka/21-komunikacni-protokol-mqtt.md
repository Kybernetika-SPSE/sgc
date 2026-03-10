# Otázka 21

## Komunikační protokol MQTT a jeho využití

- správce: Jirka
- stav: převedeno z archivu do nové stránky
- původní zdroj: [21. Komunikační protokol MQTT a jeho využití](../archiv/skripta-kyb/kybernetika/chapters/21.%20Komunikační%20protokol%20MQTT%20a%20jeho%20využití.md)

---

# MQTT
- Návrhový vzor **publisher/subscriber**
- Broker (centrální bod) třídí zprávy podle tématu (topic) a zařízení buď:
	- **Publikuje** v daném tématu (publisher) a odesílá zprávu brokeru, který ji ukládá a přeposílá zařízením, která mají **odběr** (subscription) na dané téma
	- Je **přihlášeno k odběru** na dané téma a broker zasílá tomuto zařízení všechny zprávy daného tématu
- V protokolu se posílají **zprávy** (**message** nebo také **payload**) a s nimi téma (**topic**)
- Klient může publikovat i v topicu, který zároveň odebírá. Zpráva se samozřejmě odešle **všem subscriberům**, tedy i klientovi, který ji publikoval. V praxi se to ale takto obvykle nedělá. Typicky klient vystupuje buď jako subscriber, nebo jako publisher podle konkrétní role.
- Témata
	- místo, kam „putuje“ zpráva
	- Jedno zařízení může mít **odběr nebo publisher** u **více témat najednou**. Zpráva může patřit **právě do jednoho tématu**
	- **Publisher nemusí zakládat nové téma**. Pokud broker přijme zprávu s novým tématem, automaticky je založí
	- Témata jsou řetězce **UTF-8** (diakritika není problém)
- **Wildcards**:
	- **Single level** = “+ˮ
		- odběr celé **jedné úrovně** témat
		- pokud odbíráme téma: `myhome/groundfloor/+/temperature`
![](images/21-single-level-wild-card.png)

- **Multi level** = “#ˮ
	- odběr **všech úrovní** témat
	- pokud odbíráme téma: `myhome/groundfloor/#`
![](images/21-multilevel-wild-card.png)

- Normálně broker **nevidí strukturu** topicu; topic je prostě řetězec a broker nevidí lomítka jako oddělovače úrovní.
- Když broker **detekuje wildcard**, rozdělí si zprávu podle lomítek a vytvoří routovací tabulku, podle které zasílá nové zprávy subscriberům.
- Protokol je „payload agnostic“, tedy **formát** dat nebo zpráv je z jeho pohledu **irelevantní**. Nejčastěji jde o JSON nebo BSON. Obsah zprávy je omezen na **256 MB**.

## QoS
Tři úrovně **QoS** (Quality of Service). Klient **nemusí všechny podporovat**
**= Potvrzení o dodání** zprávy / packetu
1. Zpráva je odeslána bez potvrzení a **není zaručeno doručení**
2. Zpráva je doručena **alespoň jednou**
3. Každá zpráva je doručena **právě jednou**

## Struktura MQTT
![](images/21-striktura-mqtt.png)

Ukázka programu MQTT v Micropythonu:
```python
import network
import time
from machine import Pin
from umqtt.simple import MQTTClient

wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect("ssid","pass")
time.sleep(5)
print(wlan.isconnected())

sensor = Pin(16, Pin.IN)

mqtt_server = 'broker.hivemq.com'
client_id = 'sauron'
topic_pub = b'middle_earth/sauron'
topic_sub = b'middle_earth/sauron'
topic_msg = b'Ach nach utunbagul'
```

```python
def callback(topic, msg):
	print("Message received: ", msg)
	print("Topic: ", topic)
```

```python
def mqtt_connect():
	client = MQTTClient(client_id, mqtt_server, keepalive=3600) # keepalive v sekundách
	client.connect()
	print('Connected to %s MQTT Broker'%(mqtt_server))
	return client
```
Parametr **keepalive** označuje interval v sekundách, během kterého musí odesílatel poslat packet `PINGREQ`, aby nebylo připojení ukončeno. Broker po přijetí odpovídá packetem `PINGRESP`, který potvrzuje, že je připojení pořád aktivní.

```python
def reconnect():
	print('Failed to connect to the MQTT Broker. Reconnecting...')
	time.sleep(5)
	machine.reset()

try:
	client = mqtt_connect()
	client.set_callback(callback)
	client.subscribe(topic_sub) #zaregistruje schránku, kterou poslouchá a
except OSError as e:
	reconnect()
while True:
	client.publish(topic_pub, topic_msg) #topic_pub = jméno schránky
	#topic_msg = odesílané data
	time.sleep(3)
```



