from machine import Pin, ADC, PWM,SPI
from ssd1306 import SSD1306_SPI
import framebuf
import time
buz = Pin(11, Pin.OUT) #This is the buzzer
servoE = PWM(Pin(14)) #This is the servo motor at the entrance gate
servoE.freq(50)
servoX = PWM(Pin(15)) #This is the servo motor at the exit gate
servoX.freq(50)
led1 = Pin(1, Pin.OUT) #This pin was connected to both the laser module at the entrance and at the exit
sensE = Pin(13, Pin.IN, Pin.PULL_DOWN) #This is the photoresistor at the entrance gate
sensX = Pin(12, Pin.IN, Pin.PULL_DOWN) #This is the photoresistor at the exit gate
spi = SPI(0, 100000, mosi=Pin(19), sck=Pin(18))
oled = SSD1306_SPI(128, 64, spi, Pin(17),Pin(20), Pin(16))


oled.fill(0)
oled.show()
oled.text("PARKING SYSTEM",0,0)
oled.show()
time.sleep(1.3)
oled.text("Designed by Aura",0,20)
oled.show()
time.sleep(2)
count = 10 #Total number of parking spaces available

while True:
        buz.value(1)
        value = 4500
        led1.value(1)
        if sensE.value()==0 and sensX.value()==0:
                servoE.duty_u16(7500)
                servoX.duty_u16(value)
                time.sleep(0.5)
                oled.fill(0)
                oled.show()
                oled.text("PARKING LOT",0,0)
                oled.text("EMPTY SPACES:",0,20)
                oled.text(str(count), 105,20)
                oled.show()
                
        elif sensE.value() == 1 and sensX.value() == 1:
            servoE.duty_u16(value)
            servoX.duty_u16(7500)
            oled.fill(0)
            oled.show()
            oled.text("PARKING LOT",0,0)
            oled.text("EMPTY SPACES:",0,20)
            oled.text(str(count), 105,20)
            oled.show()
            buz.value(0)
            time.sleep(3.5)
            buz.value(1)
        elif sensE.value()==0 and sensX.value()==1:
            count = count + 1
            if count <=10 and count>0:
                servoX.duty_u16(7500)
                servoE.duty_u16(7500)
                oled.fill(0)
                oled.show()
                oled.text("PARKING LOT",0,0)
                oled.text("EMPTY SPACES:",0,20)
                oled.text(str(count), 105,20)
                oled.show()
                buz.value(0)
                time.sleep(3.5)
                buz.value(1)
            else:
                oled.fill(0)
                servoE.duty_u16(7500)
                servoX.duty_u16(value)
                oled.show()
                oled.text("PARKING LOT",0,0)
                oled.text("FULL!!:",0,20)
                oled.show()
                buz.value(0)
                time.sleep(0.5)
                buz.value(1)
                time.sleep(0.5)
                buz.value(0)
                time.sleep(0.5)
                buz.value(1)
                time.sleep(1)
        elif sensE.value()==1 and sensX.value()==0:
            if count <=10 and count>0:
                count = count - 1
                servoE.duty_u16(value)
                servoX.duty_u16(value)
                oled.fill(0)
                oled.show()
                oled.text("PARKING LOT",0,0)
                oled.text("EMPTY SPACES:",0,20)
                oled.text(str(count), 105,20)
                oled.show()
                buz.value(0)
                time.sleep(3.5)
                buz.value(1)
            else:
                oled.fill(0)
                servoE.duty_u16(7500)
                servoX.duty_u16(value)
                oled.show()
                buz.value(1)
                time.sleep(0.5)
                buz.value(0)
                oled.text("PARKING LOT",0,0)
                oled.text("FULL!!:",0,20)
                oled.show()
                buz.value(0)
                time.sleep(0.5)
                buz.value(1)
                time.sleep(0.5)
                buz.value(0)
                time.sleep(0.5)
                buz.value(1)
                time.sleep(1)
        else:       
            continue
    
        
    
