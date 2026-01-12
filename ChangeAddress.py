#!/usr/bin/env python
import sys

import minimalmodbus
import serial
import time

REGISTER_NUMBER_DECIMALS = 1

# To change the address of your sensor device
# Provides upper computer debugging software, allowing users to modify the device address
# (range: 0 to 255), baud rate (range: 4800bps to 9600bps), and parity method by themselves,
# and these settings can be saved after power-off

# slave address (in decimal)
DEVICE_ADDRESS = 1  # connect to default address
DEVICE_DEBUG = True  # ENABLE/DISABLE communication debug mode
PORT_NAME = 'COM6'  # Master PORT name -- Change as needed for your host.
MODEL_TYPE = 'MD02'  # Model type new or old default XY-MD02. Other MD02

# change the divider for model type
match MODEL_TYPE:
    case 'XY-MD02':
        REGISTER_NUMBER_DECIMALS = 1
        DEVICE_ADDRESS_MAX = 255
    case 'MD02':
        REGISTER_NUMBER_DECIMALS = 2
        DEVICE_ADDRESS_MAX = 251
    case _:
        REGISTER_NUMBER_DECIMALS = 1
        DEVICE_ADDRESS_MAX = 255


def _check_new_address(new_address):
    # MODBUS instrument initialization
    test = minimalmodbus.Instrument(PORT_NAME, new_address, debug=DEVICE_DEBUG)

    test.serial.baudrate = 9600
    test.serial.bytesize = 8
    test.serial.polarity = minimalmodbus.serial.PARITY_NONE
    test.serial.stopbits = 1
    test.mode = minimalmodbus.MODE_RTU
    test.serial.timeout = 1.2

    while True:
        # Register number, number of decimals, function code
        temperature = test.read_register(1, REGISTER_NUMBER_DECIMALS, 4)
        try:
            print(f"Temparatur: {temperature} °C")
        except IOError:
            print("Failed to read from instrument")
        time.sleep(1)
        test.serial.close()
        # test end close serial port on WINDOWS


def change_address(address, new_address):
    # check new number 1-255
    if 1 <= new_address <= DEVICE_ADDRESS_MAX:

        # Init the device with default connection
        instrument = minimalmodbus.Instrument(PORT_NAME, address, debug=DEVICE_DEBUG)

        instrument.serial.baudrate = 9600
        instrument.serial.bytesize = 8
        instrument.serial.polarity = minimalmodbus.serial.PARITY_NONE
        instrument.serial.stopbits = 1
        instrument.mode = minimalmodbus.MODE_RTU
        instrument.serial.timeout = 5

        while True:
            # Register number, number of register, function code
            instrument.write_register(257, new_address, 0, 6)
            time.sleep(3)
            # add todo register soft reset??
            # add CRC check
            try:
                print(f"Changed address: {address} -> {new_address}")
            except IOError:
                print("Failed change instrument address")
            time.sleep(1)
            instrument.serial.close()
            # close connection
    else:
        print("New address must between 1-255")
        sys.exit()  # end def change_address


#########################################
#
#   main function add console vars
#
#########################################
while True:
    try:
        old_address = int(input("Enter the old number of the device whose address we would like to change: "))
        print("Your entry was: ", old_address)

        new_address = int(input("Enter the new address we want to set: "))
        print("Your entry was: ", new_address)

        print("......")
        print("#########################################################")

        change_address(old_address, new_address)
        print(f"New address was set to: {new_address}")
    except IOError:
        print("...Failed set new address...exit program! Use debug mode!")
        time.sleep(3)
        sys.exit()
    try:
        # test the new device connection
        # todo add a routine to wait for restart device
        _check_new_address(new_address)
        print(f"New address work")
    except IOError:
        print("The new address dont work...exit program! Use debug mode!")
        time.sleep(1)
        sys.exit()
