# Ereignismeldung
Meldung eines Ereignisses von einem externen Standort 
Hier wird eine Lösung dokumentiert, wie man Ereignisse, von einem externen Standort melden und darstellen kann. 
Am externen Standort soll weder ein Stromanschluss vorhanden noch ein WLAN Verbindung möglich sein. 
Die Stromversorgung wird durch Batteriebetrieb sichergestellt. Das impliziert natürlich, dass man extrem sparsam mit 
dem Stromverbrauch umgehen muss, damit die Lösung über einen längeren Zeitraum funktionieren kann. 
So ist z.B. mit einer Batteriespeisung mit drei Battereien (Typ AA) ein Betrieb über mehrere Monate möglich, 
wenn man nur einmal pro Stunde misst.

Für die hier gezeigte Lösung benötigt man folgende Hardware: 
- 1 x RaspberryPi Pico 
- 1 x RaspberryPi Pico W
- 2 x LoraWAN Transceiver vom Typ RAK 3272S
- 1 x Nano Power Timer HAT ( Link: https://core-electronics.com.au/makerverse-nano-power-timer-hat-for-raspberry-pi-pico.html )
- 1 x Magnetschalter mit passendem Magnet
- 3 x Batterien (Typ: AA) mit passendem Halter



