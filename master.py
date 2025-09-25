import smbus
import time

I2C_ADDR = 0x08
bus = smbus.SMBus(0)

def read_distance():
    try:
        data = bus.read_i2c_block_data(I2C_ADDR, 0, 2)
        distance_mm = (data[0] << 8) | data[1]
        distance_cm = distance_mm /10.0
        return distance_cm
    except Exception as e:
        print("I2C Error: ", e)
        return None

try:
    while True:
        distance = read_distance()
        if distance is not None:
            print(f"Distance: {distance} cm")
        time.sleep(0.2)

except KeyboardInterrupt:
    print("Stopping...")