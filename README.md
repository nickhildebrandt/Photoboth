<p align="center">
  <img src="https://git.ts13.de/Nick/photoboth/-/raw/master/data/Logo.png" width="300"/>
</p>

# Photoboth

Eine Fotobox Linux Bash Skript für den Raspberry Pi welches mit einer Pi Cam einen voll funktionsfähigen Automaten Bereitstellt.

## Inhalt

- Vorausetzungen
- Aufbau
- Installation
- Verwendung
- Entwicklung
- FAQ
- Credits
- Lizenz

## Vorausetzungen (Mein Einkauf vom 17.11.20)

| Artikel         | Preis              | Amazon Link                                                                                     |
|:---------------:|:------------------:|:-----------------------------------------------------------------------------------------------:|
| Druckschalter   | 07,99€             | https://www.amazon.de/gp/product/B0825RCZJS/ref=ppx_yo_dt_b_asin_title_o00_s00?ie=UTF8&psc=1    |
| Carbon Folie    | 16,99€             | https://www.amazon.de/gp/product/B07MJ2NBBV/ref=ppx_yo_dt_b_asin_title_o08_s00?ie=UTF8&psc=1    |
| Sperholzplatten | 16,95€             | https://www.amazon.de/dp/B005QM4V5C/ref=cm_sw_em_r_mt_dp_jN2SFbR2R8M3M                          |
| Pi Cam          | 07,59€             | https://www.amazon.de/gp/product/B07CMXJLXR/ref=ppx_yo_dt_b_asin_title_o01_s00?ie=UTF8&psc=1    |
| Rasberry Pi 3b  | 33,60€             | https://www.amazon.de/dp/B01CD5VC92/ref=cm_sw_em_r_mt_dp_wi.SFbYWETK0P                          |
| Netzteil        | 10,99€             | https://www.amazon.de/dp/B01566WOAG/ref=cm_sw_em_r_mt_dp_el.SFb8HM8T75?_encoding=UTF8&psc=1     |
| SD Karte 128GB  | 17,04€             | https://www.amazon.de/dp/B073JYC4XM/ref=cm_sw_em_r_mt_dp_mm.SFb9HCWJFZ                          |
| Steckerleiste 3 | 03,89€             | https://www.amazon.de/dp/B00006J9XX/ref=cm_sw_em_r_mt_dp_Sn.SFbC4GTRD7                          |
| USB Netzteil    | 13,99€             | https://www.amazon.de/dp/B00WLI5E3M/ref=cm_sw_em_r_mt_dp_lq.SFbHVP13ED                          |
| F2F Kabel       | 04,33€             | https://www.amazon.de/dp/B07KYHBVR7/ref=cm_sw_em_r_mt_dp_egaTFbHWN9CGD                          |
| LAN Verlängerung| 06,40€             | https://www.amazon.de/dp/B016ZBCSIO/ref=cm_sw_em_r_mt_dp_YdaTFbYDPQTTF                          |
| Display         | 89,99€             | https://www.amazon.de/gp/product/B06XWVLNMT/ref=ppx_yo_dt_b_asin_title_o00_s00?ie=UTF8&psc=1    |
| Lüfter          | 17,49€             | https://www.amazon.de/gp/product/B071CL82G9/ref=ppx_od_dt_b_asin_title_s02?ie=UTF8&psc=1        |
| HDMI Kabel 0,25 | 04,89€             | https://www.amazon.de/dp/B013ICNQLQ/ref=cm_sw_em_r_mt_dp_dlC_WynTFbMCMF2GY                      |
| **Insgesamt**   | **252,13€**       | *Speicher und Folie nach eigenem ermessen.                                                      |

### Was Ihr sonst noch Braucht

  - Heizkleber
  - Kleine, Dünne Schrauben
  - Lötkolben mit Lötzin
  - Zeit und Nerven :-)


## Aufbau

### Der Aufbau ist jedem selbst überlassen hier nur mein Beispiel.

<p align="center">
  <img src="https://git.ts13.de/Nick/photoboth/-/raw/master/info/Boden.png" width="600"/>
</p>


## Installation

### Bitte Denkt Daran in der "raspi-config" die Picam und SSH zu Aktiviren

### Clone

> Installiere Git

```shell
$ sudo apt-get install git
```

> Lade dir das Repo Herunter und entpacke es in dein Home Verzeichnis.

```shell
$ git clone http://git.ts13.myds.me/puplic/photoboth.git
```
### Setup


> Wechsle in den entpacken Ordner und mache die Datei ausführbar.

```shell
$ cd photoboth
```

```shell
$ sudo chmod +x install.sh
```

> Führe sie nun aus.

```shell
$ ./install.sh
```
> Nun bist du Fertig!


## Verwendung

Der Pi starten nun automatisch in die CLI und meldet sich an. Danach wird das Photoboth Skript gestartet und es kann mit dem druck einer beliebigen Taste ein Foto ausgelöst werden. Dieses wird nach der Ausgabe „Vielen Dank - Gespeichert" in dem Ordner $HOME/photoboth/data Verschoben und kann mit sftp:22 heruntergeladen werden.


## Entwicklung

Das Skript basiert auf dem im Raspberry Pi OS inbegriffenen "raspivid" und erweitert diese in formen der Automationen sowie dem Nutzererlebnis. Jeder kann sehr gerne dieses Skript erweitern und dazu beitragen.


## FAQ

### Frage und Antworten:

Hier auf GitLab

MacAndMore: Youtube Kanahl https://www.youtube.com/channel/UCITYl7HZpDdAfpelX5oixeg

Mail: macandmore100@gmail.com


## Credits

Ich betreibe auch einen YouTube Kanal rund ums Thema Linux. Wenn ihr mich unterstützen wollt schaut gerne mal Vorbei!

https://www.youtube.com/channel/UCITYl7HZpDdAfpelX5oixeg

Zudem habe ich eine Website mit mehr Informationen und Anleitungen zu diesem oder anderen Projekten.

https://macandmore.ddnss.de
