#!/usr/bin/env python
import minimalmodbus
import serial
import time

# slave address (in decimal)
DEVICE_ADDRESS = 1
# ENABLE/DISABLE communication debug mode
DEVICE_DEBUG = True
# Master PORT name -- Change as needed for your host.
PORT_NAME = 'COM6'
# Model type new or old default XY-MD02. Other MD02
MODEL_TYPE = 'XY-MD02'

# MODBUS instrument initialization
instrument = minimalmodbus.Instrument(PORT_NAME, DEVICE_ADDRESS, debug=DEVICE_DEBUG)

instrument.serial.baudrate = 9600
instrument.serial.bytesize = 8
instrument.serial.polarity = minimalmodbus.serial.PARITY_NONE
instrument.serial.stopbits = 1
instrument.mode = minimalmodbus.MODE_RTU
instrument.serial.timeout = 1.2

# Read register
REGISTER_ADDRESS = 1
ModBus_Command = 4


# change the divider for model type
match MODEL_TYPE:
    case 'XY-MD02':
        REGISTER_NUMBER_DECIMALS = 1
    case 'MD02':
        REGISTER_NUMBER_DECIMALS = 2
    case _:
        REGISTER_NUMBER_DECIMALS = 1

while True:
    # Register number, number of decimals, function code
    temperature = instrument.read_register(REGISTER_ADDRESS, REGISTER_NUMBER_DECIMALS, ModBus_Command)
    try:
        print(f"Temparatur: {temperature} °C")
    except IOError:
        print("Failed to read from instrument")
    time.sleep(1)
    instrument.serial.close()
    # close connection
