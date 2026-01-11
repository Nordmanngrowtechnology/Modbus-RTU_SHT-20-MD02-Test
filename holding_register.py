#!/usr/bin/env python
import minimalmodbus
import serial
import time

DEVICE_ADDRESS = 1 # slave address (in decimal)
DEVICE_DEBUG = True # ENABLE/DISABLE communication debug mode
PORT_NAME = 'COM6' # Master PORT name -- Change as needed for your host.
MODEL_TYPE = 'MD02' # Model type new or old default XY-MD02. Other MD02

# Dictionaries default baudrate
DEFAULT_SERIAL_BAUD_RATE = {
    "xy-md02": {
        0: 9600,
        1: 14400,
        2: 19200,
    },
    "md02": {
        0: 2400,
        1: 4800,
        2: 9600,
    }
}

# Read register address
REGISTER_ADDRESS = 257
ModBus_Command = 3

# change the divider for model type
match MODEL_TYPE:
    case 'XY-MD02':
        REGISTER_NUMBER_DECIMALS = 1
        SERIAL_BAUD_RATE = DEFAULT_SERIAL_BAUD_RATE["xy-md02"][0]
    case 'MD02':
        REGISTER_NUMBER_DECIMALS = 1
        SERIAL_BAUD_RATE = DEFAULT_SERIAL_BAUD_RATE["md02"][2]
    case _:
        REGISTER_NUMBER_DECIMALS = 1
        SERIAL_BAUD_RATE = 9600


# MODBUS instrument initialization
instrument = minimalmodbus.Instrument(PORT_NAME, DEVICE_ADDRESS, debug=DEVICE_DEBUG)

instrument.serial.baudrate = SERIAL_BAUD_RATE
instrument.serial.bytesize = 8
instrument.serial.polarity = minimalmodbus.serial.PARITY_NONE
instrument.serial.stopbits = 1
instrument.mode = minimalmodbus.MODE_RTU
instrument.serial.timeout = 5.2



while True:
    # Register number, number of decimals, function code
    register = instrument.read_register(REGISTER_ADDRESS, REGISTER_NUMBER_DECIMALS, ModBus_Command)
    try:
        print(f"Response from holding register: {register.hex()} ")
    except IOError:
        print("Failed to read from instrument")
    time.sleep(1)
    instrument.serial.close()
    # close connection
