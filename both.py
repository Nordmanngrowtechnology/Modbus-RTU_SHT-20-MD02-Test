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
NUMBER_OF_REGISTER = 2 # ignored by model MD02 ??? open issus if you have more information
ModBus_Command = 4


# change the divider for model type
match MODEL_TYPE:
    case 'XY-MD02':
        REGISTER_NUMBER_DECIMALS = 1
        DIVIDER = 10
    case 'MD02':
        REGISTER_NUMBER_DECIMALS = 2
        DIVIDER = 100
    case _:
        REGISTER_NUMBER_DECIMALS = 1
        DIVIDER = 10

while True:
    # Register number, number of register, function code
    value = instrument.read_registers(REGISTER_ADDRESS, NUMBER_OF_REGISTER, ModBus_Command)
    try:
        print(f"Temperature: {value[0]/DIVIDER} °C")
        print(f"Humidity: {value[1]/DIVIDER} %Rf")
    except IOError:
        print("Failed to read from instrument")
    time.sleep(1)
    instrument.serial.close()
    # close connection

