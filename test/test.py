# !/usr/bin/env python
import minimalmodbus
import time

###############################
# Settings:
# example get device address
#
# DEVICE_ADDRESS = 0x01
# DEVICE_DEBUG = True
# PORT_NAME = 'COM6'
# TIMEOUT = 3
# REGISTER = 0x0101
# MODBUS_CODE = 0x03
#
###############################

###############################
# Settings:
# example get device baudrate
#
# DEVICE_ADDRESS = 0x01
# DEVICE_DEBUG = True
# PORT_NAME = 'COM6'
# TIMEOUT = 3
# REGISTER = 0x0102
# MODBUS_CODE = 0x03
#
###############################

###############################
# Settings:
# example get device temperature correction
#
#DEVICE_ADDRESS = 0x01
#DEVICE_DEBUG = True
#PORT_NAME = 'COM6'
#TIMEOUT = 3
#REGISTER = 0x0103
#MODBUS_CODE = 0x03
#
###############################

###############################
# Settings:
# example get device humidity correctio
#
# DEVICE_ADDRESS = 0x01
# DEVICE_DEBUG = True
# PORT_NAME = 'COM6'
# TIMEOUT = 3
# REGISTER = 0x0104
# MODBUS_CODE = 0x03
#
###############################

###############################
# Settings:
#
DEVICE_ADDRESS = 1
DEVICE_DEBUG = True
PORT_NAME = 'COM6'
TIMEOUT = 3
REGISTER = 0x0000 #
MODBUS_CODE = 0x03
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

# Print MODBUS configuration
print ("MODBUS Configuration\n")
print ("********************\n")
print (instrument)
print ("\n********************\n")


while True:
    # Register number, number of register, function code
    #value = instrument.read_registers(REGISTER,1,MODBUS_CODE)
    value = instrument.read_register(REGISTER, 1, MODBUS_CODE)
    try:
        print(f" {value}")

    except IOError:
        print("Failed to read from instrument")
    time.sleep(1)
    instrument.serial.close()
    # close connection
