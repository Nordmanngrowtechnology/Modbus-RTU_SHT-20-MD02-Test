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
instrument.serial.timeout = 0.2




# Read Humidity & Temperature
REGISTER_ADDRESS_ALL = 1
NUMBER_OF_REGISTER = 2 # We will read tow register
ModBus_Command = 4


while True:
    # Register number, number of register, function code
    value = instrument.read_registers(REGISTER_ADDRESS_ALL, NUMBER_OF_REGISTER, ModBus_Command)
    try:
        print(f"Temperature: {value[0]/10} °C")
        print(f"Humidity: {value[1]/10} %Rf")
    except IOError:
        print("Failed to read from instrument")
    time.sleep(1)
    instrument.serial.close()
    # close connection

