from machine import ADC, Pin, I2C, PWM, time_pulse_us
from pico_i2c_lcd import I2cLcd
import time
import network
import urequests

SSID = "YOUR WIFI NAME"
PASSWORD = "WIFI PASSWORD"
API_KEY = "API KEY FROM THINGSPEAK"

# -------- WIFI --------
wifi = network.WLAN(network.STA_IF)
wifi.active(True)
wifi.connect(SSID, PASSWORD)

print("Connecting WiFi...")
while not wifi.isconnected():
    pass
print("WiFi Connected")

# -------- LCD SETUP (MOVE UP) --------
i2c = I2C(0, sda=Pin(0), scl=Pin(1), freq=400000)
devices = i2c.scan()

if len(devices) == 0:
    print("No LCD found")
else:
    lcd = I2cLcd(i2c, devices[0], 2, 16)
    lcd.clear()

# -------- IR (ROOMS) --------
room1 = Pin(17, Pin.IN)
room2 = Pin(18, Pin.IN)
room3 = Pin(19, Pin.IN)

# -------- IR (DOOR) --------
ir1 = Pin(14, Pin.IN)
ir2 = Pin(15, Pin.IN)

# -------- SERVO --------
servo = PWM(Pin(16))
servo.freq(50)

def set_angle(angle):
    duty = int(2000 + (angle / 180) * 8000)
    servo.duty_u16(duty)

# -------- ULTRASONIC --------
trig_w = Pin(3, Pin.OUT)
echo_w = Pin(2, Pin.IN)

trig_b = Pin(5, Pin.OUT)
echo_b = Pin(4, Pin.IN)

def get_distance(trig, echo):
    trig.low()
    time.sleep_us(2)
    trig.high()
    time.sleep_us(10)
    trig.low()
    duration = time_pulse_us(echo, 1)

    if duration < 0:
        return 0

    return duration * 0.034 / 2

# -------- GAS --------
gas = ADC(Pin(26))

# -------- COUNT --------
count = 0

print("System Started...")

#  SAFE LCD USE
if 'lcd' in globals():
    lcd.putstr("System Started")
    time.sleep(2)
    lcd.clear()

# -------- THINGSPEAK --------
def send_data(r1, r2, r3, bin_level, gas_val, clean, water):
    url = "https://api.thingspeak.com/update?api_key=" + API_KEY + \
          "&field1=" + str(r1) + \
          "&field2=" + str(r2) + \
          "&field3=" + str(r3) + \
          "&field5=" + str(bin_level) + \
          "&field6=" + str(gas_val) + \
          "&field7=" + str(clean) + \
          "&field8=" + str(water)

    try:
        response = urequests.get(url)
        response.close()
        print("Sent to ThingSpeak")
    except:
        print("Send Error")

# -------- MAIN LOOP --------
while True:

    # -------- ENTRY --------
    if ir1.value() == 0:
        time.sleep(0.2)
        if ir1.value() == 0:
            count += 1
            print("Entered:", count)

            if 'lcd' in globals():
                lcd.clear()
                lcd.putstr("Entered\nCount: {}".format(count))
                time.sleep(1)

            set_angle(90)
            time.sleep(1)
            set_angle(0)

            while ir1.value() == 0:
                pass

    # -------- EXIT --------
    if ir2.value() == 0:
        time.sleep(0.2)
        if ir2.value() == 0:
            if count > 0:
                count -= 1
            print("Exited:", count)

            if 'lcd' in globals():
                lcd.clear()
                lcd.putstr("Exited\nCount: {}".format(count))
                time.sleep(1)

            set_angle(90)
            time.sleep(1)
            set_angle(0)

            while ir2.value() == 0:
                pass

    # -------- ROOMS --------
    r1 = 1 if room1.value() == 0 else 0
    r2 = 1 if room2.value() == 0 else 0
    r3 = 1 if room3.value() == 0 else 0

    print("Rooms:", r1, r2, r3)

    if 'lcd' in globals():
        lcd.clear()
        lcd.putstr("R1:{} R2:{}\nR3:{}".format(r1, r2, r3))
        time.sleep(1)

    # -------- ULTRASONIC --------
    water = get_distance(trig_w, echo_w)
    bin_level = get_distance(trig_b, echo_b)

    print("Water:", water)
    print("Bin:", bin_level)

    if 'lcd' in globals():
        lcd.clear()
        lcd.putstr("Bin:{} WATER:{}".format(int(bin_level), int(water)))
        time.sleep(1)

    # -------- GAS --------
    val = gas.read_u16()
    print("Gas Value:", val)

    if 'lcd' in globals():
        lcd.clear()
        lcd.putstr("Gas:{}".format(val))
        time.sleep(1)

    if val > 3000:
        print("Bad Smell")
        print("Cleaning Needed")

    # -------- CLEANING --------
    if count >= 5:
        print("Cleaning Required")

    print("----------------------")

    clean_flag = 1 if count >= 5 else 0

    send_data(r1, r2, r3, bin_level, val, clean_flag, water)

    time.sleep(5)
