# !/usr/bin/env python
import minimalmodbus
import time


###############################
# Settings:
# example set device baudrate
#
DEVICE_ADDRESS = 0x01 # connection address

ACTUAL_BAUDRATE = 4800 # actual baudrate for connection
NEW_BAUDRATE = 0x02

DEVICE_DEBUG = True
PORT_NAME = 'COM6'
TIMEOUT = 3
#REGISTER = 0x0102 # change baudrate for XY-MD02
REGISTER = 0x0101 # change baudrate for MD02
MODBUS_CODE = 0x06
#
###############################


# Use python extension minimalmodbus to request settings
# etablish a connection with the old baudrate
instrument = minimalmodbus.Instrument(PORT_NAME, DEVICE_ADDRESS, debug=DEVICE_DEBUG)

instrument.serial.baudrate = ACTUAL_BAUDRATE
instrument.serial.bytesize = 8
instrument.serial.polarity = minimalmodbus.serial.PARITY_NONE
instrument.serial.stopbits = 1
instrument.mode = minimalmodbus.MODE_RTU
instrument.serial.timeout = TIMEOUT

# try to chang to the new baudrate after change the device must power off to restart with new setting
while True:
    # Register number, number of register, function code
    instrument.write_register(REGISTER, NEW_BAUDRATE, 0, MODBUS_CODE)
    try:
        print(f"New baudrate set to: {NEW_BAUDRATE} restart device that affect")

    except IOError:
        print("Failed to read from instrument")
    time.sleep(1)
    instrument.serial.close()
    # close connection
