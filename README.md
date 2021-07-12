Photoboth
=========

### Achtung dieser Artikel ist nicht immer aktuell. Bitte beachte sattesten den Artikel auf MacAndMore: https://macandmore.ddnss.de/projekte/photoboth

Was ist das?
------------

Ein Fotobox Python Programm für den Raspberry Pi, welches mit einer Pi Cam einen voll funktionsfähigen Fotoautomaten bereitstellt.
 Das Skript basiert auf "Python-PiCamera" und erweitert dieses in Formen der Automationen, sowie dem Nutzererlebnis. Jeder kann sehr gerne dieses Skript erweitern und dazu beitragen.

Was geschieht mit meinem Pi?
----------------------------

Der Pi startet nach der Installation automatisch in die CLI und meldet sich an. Danach wird das Photoboth Skript gestartet und es kann mit dem Druck der Taste ein Foto ausgelöst werden. Dieses wird nach der Ausgabe „Vielen Dank - gespeichert" in dem Ordner \$HOME/photoboth/data verschoben und kann mit sftp:22 heruntergeladen werden.
 Alternativ kann beim Start auch ein USB-Stick eingesteckt werden, nun wird dieser automatisch in /home/pi/photoboth/data eingebunden. Daraufhin steht dieser dem System als primäres Speichermedium für die Bilder zur Verfügung und kann einfach am PC ausgelesen werden.

Das Fotoboxprojekt
------------------

Ich habe bereits, aufgrund von großem Interesse, das Fotoboxprojekt in Schulen umgesetzt. Hier hatten Schülerinnen und Schüler die Möglichkeit, sich mit Mikroelektronik und Python Programmierung zu beschäftigen. Wer Anregung sucht, findet [hier eine PDF](../../media/photoboth/Photobox%20Projekt%20–%20Ablauf%20und%20Planung.pdf)mit allen Projektinformationen und erhält einen Vorschlag für den Zusammenbau.

Was wird Benötigt?
------------------

<table>
<col width="33%" />
<col width="33%" />
<col width="33%" />
<thead>
<tr class="header">
<th align="left">Artikel</th>
<th align="left">Preis</th>
<th align="left">Amazon Link</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left">Druckschalter</td>
<td align="left">07,99€</td>
<td align="left"><a href="https://www.amazon.de/gp/product/B0825RCZJS/ref=ppx_yo_dt_b_asin_title_o00_s00?ie=UTF8&amp;psc=1"></a>
<p>Zum Artikel</p></td>
</tr>
<tr class="even">
<td align="left">Sperrholzplatten</td>
<td align="left">16,95€</td>
<td align="left"><a href="https://www.amazon.de/dp/B005QM4V5C/ref=cm_sw_em_r_mt_dp_jN2SFbR2R8M3M"></a>
<p>Zum Artikel</p></td>
</tr>
<tr class="odd">
<td align="left">Pi Cam</td>
<td align="left">07,59€</td>
<td align="left"><a href="https://www.amazon.de/gp/product/B07CMXJLXR/ref=ppx_yo_dt_b_asin_title_o01_s00?ie=UTF8&amp;psc=1"></a>
<p>Zum Artikel</p></td>
</tr>
<tr class="even">
<td align="left">Raspberry Pi 3b</td>
<td align="left">33,60€</td>
<td align="left"><a href="https://www.amazon.de/dp/B01CD5VC92/ref=cm_sw_em_r_mt_dp_wi.SFbYWETK0P"></a>
<p>Zum Artikel</p></td>
</tr>
<tr class="odd">
<td align="left">Netzteil (2x)</td>
<td align="left">10,99€</td>
<td align="left"><a href="https://www.amazon.de/dp/B01566WOAG/ref=cm_sw_em_r_mt_dp_el.SFb8HM8T75?_encoding=UTF8&amp;psc=1"></a>
<p>Zum Artikel</p></td>
</tr>
<tr class="even">
<td align="left">SD Karte 128GB</td>
<td align="left">17,04€</td>
<td align="left"><a href="https://www.amazon.de/dp/B073JYC4XM/ref=cm_sw_em_r_mt_dp_mm.SFb9HCWJFZ"></a>
<p>Zum Artikel</p></td>
</tr>
<tr class="odd">
<td align="left">Steckerleiste 3</td>
<td align="left">03,89€</td>
<td align="left"><a href="https://www.amazon.de/dp/B00006J9XX/ref=cm_sw_em_r_mt_dp_Sn.SFbC4GTRD7"></a>
<p>Zum Artikel</p></td>
</tr>
<tr class="even">
<td align="left">F2F Kabel</td>
<td align="left">04,33€</td>
<td align="left"><a href="https://www.amazon.de/dp/B07KYHBVR7/ref=cm_sw_em_r_mt_dp_egaTFbHWN9CGD"></a>
<p>Zum Artikel</p></td>
</tr>
<tr class="odd">
<td align="left">Display</td>
<td align="left">89,99€</td>
<td align="left"><a href="https://www.amazon.de/gp/product/B06XWVLNMT/ref=ppx_yo_dt_b_asin_title_o00_s00?ie=UTF8&amp;psc=1"></a>
<p>Zum Artikel</p></td>
</tr>
<tr class="even">
<td align="left">Lüfter 120mm (1-2x)</td>
<td align="left">04,99€</td>
<td align="left"><a href="https://www.amazon.de/F12-120-Standard-Geh%C3%A4usel%C3%BCfter-Standardgeh%C3%A4use-Konfiguration/dp/B002KTVFTE/ref=sr_1_3?__mk_de_DE=%C3%85M%C3%85%C5%BD%C3%95%C3%91&amp;dchild=1&amp;keywords=l%C3%BCfter&amp;qid=1616863699&amp;sr=8-3"></a>
<p>Zum Artikel</p></td>
</tr>
<tr class="odd">
<td align="left">HDMI Kabel 0,25</td>
<td align="left">04,89€</td>
<td align="left"><a href="https://www.amazon.de/dp/B013ICNQLQ/ref=cm_sw_em_r_mt_dp_dlC_WynTFbMCMF2GY"></a>
<p>Zum Artikel</p></td>
</tr>
<tr class="even">
<td align="left">Gesamt:</td>
<td align="left">202,61€</td>
<td align="left">*Nach eigenem ermessen</td>
</tr>
</tbody>
</table>

Support für Blitzlicht
----------------------

Seit der Photoboth Version 1 wird auch das ansteuern eines Blitzlichtes überstürzt. Dieses kann eine ganz normale Lampe oder auch eine professionelle Fotoleuchte sein. Angesteuert wird diese dann über ein PI kompatibles Relais welches auch automatisch durch die Software initialisiert wird.

<table>
<col width="33%" />
<col width="33%" />
<col width="33%" />
<thead>
<tr class="header">
<th align="left">Artikel</th>
<th align="left">Preis</th>
<th align="left">Amazon Link</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left">Sehr Helle E27 LED</td>
<td align="left">6,76€</td>
<td align="left"><a href="https://www.amazon.de/gp/product/B08V8ND1VY/ref=ppx_yo_dt_b_asin_title_o05_s00?ie=UTF8&amp;psc=1"></a>
<p>Zum Artikel</p></td>
</tr>
<tr class="even">
<td align="left">Pi Relais</td>
<td align="left">6,99€</td>
<td align="left"><a href="https://www.amazon.de/gp/product/B07BVXT1ZK/ref=ppx_yo_dt_b_asin_title_o03_s00?ie=UTF8&amp;psc=1"></a>
<p>Zum Artikel</p></td>
</tr>
<tr class="odd">
<td align="left">Gesamt:</td>
<td align="left">13,75€</td>
<td align="left">*Nach eigenem ermessen</td>
</tr>
</tbody>
</table>

Tools die Benötigt werden:
-------------------

- Raspberry PI OS (Frische Installation)

- Heißkleber

- Kleine, Dünne Schrauben

- Lötkolben mit Lötzinn

- Zeit und Nerven :-)


Das Pinout
-------------------

![](https://git.ts13.de/Nick/photoboth/-/raw/master/info/pinout.png)

Die Software
-------------------

Die Software Die Software wurde von mir selbst erstellt. Es handelt sich um ein Python Skript, welches in Form eines DEB Paketes ausgeliefert wird. Dabei wird im Zuge der Installation ein Systemd-Service erstellt, welcher das Programm automatisch startet. Jeglicher code ist auf GitHub frei verfügbar und kann abgeändert sowie verbessert werden (GP3).

Die Installation
================

1. Startart Password ändern

`passwd pi`

2. System aktualisieren

`sudo apt update && sudo apt upgrade -y && sudo apt dist-upgrade -y`

3. Sprache, Uhrzeit und Tastaturlayout setzen

`sudo dpkg-reconfigure locales keyboard-configuration tzdata`

4. PiCam und SSH Aktivieren

`sudo raspi-config`

5. Paket herunterladen

`wget https://github.com/MacAndMoreYT/Photoboth/raw/master/deb/photoboth_1_all.deb`

6. Installieren

`sudo apt install ./photoboth_1_all.deb`

7. Reboot

`sudo reboot`

8. Einstellungen anpassen

`sudo nano /opt/photoboth/config.json`

Mögliche Einstellungen:
-------------------

- Bildschirmauflösung

- Fotoauflösung

- Fotoformat

- Speicherort

- Anzuzeigende texte

- Text Größe

- Schriftart

- Vorschau FPS

- Speicherung auf USB

Speichern auf USB
-------------------

1. FSTAB Eintrag erstellen

`sudo nano /etc/fstab`

    /dev/sda1 /media/stick vfat auto,nofail,sync,users,rw,umask=000,uid=pi,gid=users   0   0

2. USB in der Config.json Aktivieren

`sudo nano /opt/config.json`

	"usb":"OFF",
	"usb-path":"/media/stick/"

3. Reboot

`sudo reboot`

### Wichtig: Solange in der fstab und config.json USB aktiviert muss beim Start der USB-Stick vorhanden sein.