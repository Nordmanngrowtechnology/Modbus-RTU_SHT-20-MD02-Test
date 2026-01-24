# !/usr/bin/env python
import minimalmodbus
import time


###############################
# Settings:
# example set device new address
#
DEVICE_ADDRESS = 0x01 # connection address
NEW_DEVICE_ADDRESS = 0x03 # change to address
DEVICE_DEBUG = True
PORT_NAME = 'COM6'
TIMEOUT = 3
REGISTER = 0x0101 # change address for XY-MD02
#REGISTER = 0x0100 # change address for MD02
MODBUS_CODE = 16
#
###############################


# Use python extension minimalmodbus to request settings
instrument = minimalmodbus.Instrument(PORT_NAME, DEVICE_ADDRESS, debug=DEVICE_DEBUG)

instrument.serial.baudrate = 9600
instrument.serial.bytesize = 8
instrument.serial.polarity = minimalmodbus.serial.PARITY_NONE
instrument.serial.stopbits = 1
instrument.mode = minimalmodbus.MODE_RTU
instrument.serial.timeout = TIMEOUT

while True:
    # Register number, number of register, function code
    value = instrument.write_register(REGISTER, NEW_DEVICE_ADDRESS,0,MODBUS_CODE)
    try:
        print(f" {value}") # return none its work

    except IOError:
        print("Failed to read from instrument")
    time.sleep(1)
    instrument.serial.close()
    # close connection
