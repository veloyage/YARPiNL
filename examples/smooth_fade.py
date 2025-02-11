# Smooth fade animation based on cosine
from pi5neo import Pi5Neo
import time
from math import cos


def smooth_fade(neo):
    t = time.time()
    for i in range(neo.num_leds):
        intensity = int((cos(i * 0.01 + t) * 0.5 + 0.5) * 255)
        neo.set_led_color(i, intensity, intensity, intensity)
    neo.update_strip(sleep_duration=0.01)


# Initialize Pi5Neo with 300 LEDs
neo = Pi5Neo('/dev/spidev0.0', num_leds=300, spi_speed_khz=800)

# Smooth fade effect
while True:
    smooth_fade(neo)
