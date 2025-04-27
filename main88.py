# Bibliotheken laden
from machine import Pin, UART, ADC
import utime

# Initialisierung der Onboard-LED
led_onboard = Pin(25, Pin.OUT)

# Initialisierung von GPIO10, GPIO11 und GPIO12 als Ampel (Ausgang)
LED_red = Pin(10, Pin.OUT, value=0)
LED_yellow = Pin(11, Pin.OUT, value=0)
LED_green = Pin(12, Pin.OUT, value=0)

# Initialisierung des ADC0 (GPIO26)
adc0 = ADC(0)

# Initialisierung von GPIO18 als Ausgang
DONE = Pin(22, Pin.OUT) # setting this pin High will remove power, and wait for the next interval

# Initialisierung: UART
uart0 = UART(0, 115200, rxbuf=2048) # Sender

def blink_LED(i):
    while i > 0:
        LED_yellow.value(0); utime.sleep(0.2)
        LED_yellow.value(1); utime.sleep(0.8)
        LED_yellow.value(0)
        i = i-1

# Funktion: AT-Kommando senden und Rückmeldung empfangen
def sendCmdAT (uart, at_cmd, wait=1):
    char = ''
    dataString = ''
    uart.write(at_cmd + '\r\n')
    utime.sleep(wait) # Warten nach dem Senden des AT-Kommandos
    while char is not None:
        char = uart.read(1)
        try: dataString += char.decode()
        except: pass
    if dataString == '': return 'Keine Rückmeldung. Bitte TX und RX prüfen.'
    return dataString

def RAK_init():
    
    ###
    ### Konfiguration: LoRa-P2P-Mode für RAK3272S (Senden)
    ###
    print("Module Reset")
    print('Konfiguration: Sender (Transmitter)')
    print('LoRa-P2P-Mode')
    print(sendCmdAT(uart0, 'AT+NWM=0', 2))
    print(sendCmdAT(uart0, 'ATE'))
    print('LoRa-P2P-Parameter')
    print(sendCmdAT(uart0, 'AT+P2P=868000000:7:125:0:10:14'))
    print('Konfiguration für Senden abgeschlossen')
    return

# Main program
blink_LED(3)
RAK_init()

print('Senden per LoRa-P2P-Mode')
msg = "***************************"
read0 = adc0.read_u16()
y = "%04x" % read0
####y = "%04x" % x # always send 2 bytes (= 4 hex numbers)
##print("read0 = ", read0, "y = ", y)

LED_red.value(1)
LED_yellow.value(0)
utime.sleep(2)
print("\n\n|||||||||||||||")

print("read0 = ", read0)
print("y[hex] = ", y)
led_onboard.on()
msg = sendCmdAT(uart0, 'AT+PSEND=' + y)
print("Message = ", msg)
LED_red.value(0)
led_onboard.off()

print("****************")
utime.sleep(2)

# Now switch Pico off
print("Power OFF Pico")
DONE.on() 	# Power down Pico
utime.sleep(1)
LED_yellow.value(1)



