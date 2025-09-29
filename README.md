### Setup

##### Check I2C bus

```i2cdetect -y -r 0```

When the code is uploaded on the arduino so that it acts as a slave, you can see by running the i2cdetect command above that there is a device responding at I2C address 0x08 on bus 0. 

##### Python node

Install smbus to use the System Management Protocol(SMBus)
```pip install smbus``

### Why using an arduino and I2C?

You shouldn’t connect an ultrasonic sensor directly to the Jetson Nano because the Jetson runs Linux and can’t reliably measure the sensor’s fast microsecond echo pulse because the scheduler can delay the program for hundreds of microseconds or milliseconds, its GPIO pins are only 3.3 V tolerant while the HC-SR04 sensor output 5 V, and the sensor itself doesn’t use I2C but a timing-based trigger/echo interface. Using an Arduino in between solves these issues by handling the precise real-time pulse measurement safely and exposing the distance reading over I2C, which the Jetson can read easily.

### I2C

I2C contains 2 lines:
- SDA(Serial Data) : the line for the master and slave to send and receive data
- SCL(Serial Clock) : the line that carries the clock signal


## Sources

https://forums.developer.nvidia.com/t/questions-on-jetson-nano-arduino-i2c-communication/111277
https://www.circuitbasics.com/basics-of-the-i2c-communication-protocol/
