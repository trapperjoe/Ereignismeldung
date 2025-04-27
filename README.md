# Ereignismeldung
Meldung eines Ereignisses von einem externen Standort. 
Hier wird eine Lösung dokumentiert, wie man Ereignisse, von einem entfernten Standort melden und darstellen kann. 
Am externen Standort muss weder ein Stromanschluss vorhanden sein noch ein WLAN Verbindung.  
Die Stromversorgung wird durch Batterien (oder Akkus) gewährleistet. Das impliziert natürlich, dass man extrem sparsam mit 
dem Stromverbrauch umgehen muss, damit die Lösung über einen längeren Zeitraum ohne manuellen Eingriff funktionieren kann. 
So ist z.B. mit einer Batteriespeisung durch drei Battereien (Typ AA) ein Betrieb über mehrere Monate möglich, 
wenn man nur einmal pro Stunde misst. Für manche Anwendungsfälle ist das gut ausreichend. 

Für die hier gezeigte Lösung benötigt man folgende Hardware: 
- 1 x RaspberryPi Pico 
- 1 x RaspberryPi Pico W
- 2 x LoraWAN Transceiver vom Typ RAK3272S ( https://www.elektronik-kompendium.de/sites/praxis/bauteil_rak3272s-breakout-board.htm ) 
- 1 x Nano Power Timer HAT ( https://core-electronics.com.au/makerverse-nano-power-timer-hat-for-raspberry-pi-pico.html )
- 1 x Magnetschalter mit passendem Magnet
- 3 x Batterien (Typ: AA) mit passendem Halter

Viele Anwenndungsmöglichkeiten sind denkbar, z.B.:
- Überwachung ob ein Fenster oder eine Türe in einer abgelegenen Hütte noch geschlossen ist.
- Messen und Darstellen der Bodenfeuchte in einem Feld für Gemüse oder Früchte.
- Überprüfen ob ein Parkplatz noch frei ist oder nicht.
- Messen der Temperatur in einem entlegenen Keller.
- Meldung, wenn eine Tierfalle zugeschnappt hat.
- Nachricht, wenn das Garagentor nicht geschlossen ist.
- usw.

Folgende Dateien sind hier hochgeladen: 
1. Stoermelder.JPG        Eine kurze Beschreibung für welche Fälle diese Lösung geeignet ist.
2. Blockschaltbild.JPG    Eine grafische Darstellung welche funktionalen Blöcke dieses Projekt erfordert.
3. Funktionsablauf.JPG    Eine kurze Beschreibung was in den einzelnen Funktionsblöcken passiert und wie Meldungen weitergereicht werden.
4. Schaltung.JPG          Eine detaillierte Zeichnung für eine bestimmte Anwendung mit allen beteiligten Komponenten. 
5. Darstellung.JPG        Ein Beispiel, wie eine grafische Anzeige und eine Meldung (per  E-Mail) aussehen kann.
   
Die Kosten für ein solches Projekt sind minimal und in wenigen Stunden ist das Projekt fertiggestellt. 

