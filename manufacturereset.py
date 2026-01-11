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

# MODBUS instrument initialization
instrument = minimalmodbus.Instrument(PORT_NAME, DEVICE_ADDRESS, debug=DEVICE_DEBUG)

instrument.serial.baudrate = 9600
instrument.serial.bytesize = 8
instrument.serial.polarity = minimalmodbus.serial.PARITY_NONE
instrument.serial.stopbits = 1
instrument.mode = minimalmodbus.MODE_RTU
TIMEOUT = 10.0
instrument.serial.timeout = TIMEOUT

# Read Temperature
REGISTER_ADDRESS_TEMP = 1
REGISTER_NUMBER_DECIMALS = 1
ModBus_Command = 4

# todo read register address 256

for i in range(255):
    try:
        # Register number, number of decimals, function code
        temperature = instrument.read_register(i, REGISTER_NUMBER_DECIMALS, ModBus_Command)
        print(f"Temparatur: {temperature} °C")
        time.sleep(TIMEOUT)
        #instrument.serial.close()
        # close connection
    except minimalmodbus.NoResponseError:
        print("No communication with the instrument (no answer) Device: ", i)
        pass


