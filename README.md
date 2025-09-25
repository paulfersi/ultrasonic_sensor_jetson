##### Check i2c bus

i2cdetect -y -r 0

When the code is uploaded on the arduino so that it acts as a slave, you can see by running the i2cdetect command above that there is a device responding at I2C address 0x08 on bus 0.  

##### Python node

Install smbus to use the System Management Protocol(SMBus)
(pip install smbus)



## Sources

https://forums.developer.nvidia.com/t/questions-on-jetson-nano-arduino-i2c-communication/111277
