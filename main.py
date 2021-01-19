
import machine
import utime

# Get the temperature from the internal RP2040 temperature sensor.
sensor_temp = machine.ADC(4)

# See Raspberry Pi Pico datasheet for the conversion factor.
conversion_factor = 3.3 / (65535)

# Set up LEDs.
led_onboard = machine.Pin(25, machine.Pin.OUT)
led_green = machine.Pin(15, machine.Pin.OUT)
led_red = machine.Pin(14, machine.Pin.OUT)
led_blue = machine.Pin(13, machine.Pin.OUT)

def leds_off():
    led_onboard.value(0)
    led_green.value(0)
    led_red.value(0)
    led_blue.value(0)

def leds_on():
    led_onboard.value(1)
    led_green.value(1)
    led_red.value(1)
    led_blue.value(1)

# Flash all the LEDs on startup.
leds_off()
leds_on()
utime.sleep(1)
leds_off()

# Go into a loop.
while True:
    # Get a temperature reading.
    reading = sensor_temp.read_u16() * conversion_factor

    # Convert the temperature into degrees celsius.
    temperature = 27 - (reading - 0.706)/0.001721

    # If a safe temperature, light the green LED.
    if 20.00 <= temperature <= 22.20:
        leds_off()
        led_green.value(1)
    # If too hot, light the red LED.
    elif temperature > 22.20:
        leds_off()
        led_red.value(1)
    # If too cold, light the blue LED.
    elif temperature < 20.00:
        leds_off()
        led_blue.value(1)
    # If no condition met, we're in an error state, light 'em up!
    else:
        leds_on()

    print(temperature)

    # Sleep for 5 seconds.
    utime.sleep(5)

