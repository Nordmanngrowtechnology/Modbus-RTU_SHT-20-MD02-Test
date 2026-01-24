#!/usr/bin/env python
# https://github.com/Nordmanngrowtechnology/Modbus-RTU_SHT-20-MD02-Test
# Description:
# Yes this is the main file for run the communication with different types of sensors.
# Run this file in console.
# Navigate in console to this file location and run it with console command:
# python sensor.py

# **************** DFAULT INCLUDES        ****************************************
# **************** NOTHING TO CHANGE HERE ****************************************
# ********************************************************************************
import sys
from operator import index
import minimalmodbus
import time
import devices
# ********************************************************************************


# **************** ADD YOUR HARDWARE PROPERTY        *****************************
# ********************************************************************************

# The slave address (in decimal) of your connected device in most case: 1
DEVICE_ADDRESS = 1

# ENABLE/DISABLE communication debug mode yes we won debugging mode on
DEVICE_DEBUG = True

# Master PORT name -- Change as needed for your host in most case connect your device with a 485 RS to USB dongle.
#PORT_NAME = '/dev/ttyUSB0' # on Linux usp port 0 = ttyUSB0
PORT_NAME = 'COM6'          # on Windows usb port 6 = COM6

# Enter your model device here supported device you can see in the devices.py file.
#MODEL_TYPE = 'XY-MD02'
MODEL_TYPE = 'MD02'

# The timeout so long wait the script for response
TIMEOUT = 3 # 3 seconds is a very long time out 0.3 is normal enough.


# **************** END OF YOUR SETTING NOTHING MORE TO DO   **********************
# ********************************************************************************
# ********************************************************************************



# settings for different models
match MODEL_TYPE:
    case 'XY-MD02':
        DEVICE = devices.DEVICES['XY-MD02']
    case 'MD02':
        DEVICE = devices.DEVICES['MD02']
    case _:
        DEVICE = devices.DEVICES['MD02']

# Init the device
instrument = minimalmodbus.Instrument(PORT_NAME, DEVICE["device_address"], debug=DEVICE_DEBUG)

instrument.serial.baudrate = DEVICE['baudrate']
instrument.serial.bytesize = DEVICE['bytesize']
instrument.serial.polarity = minimalmodbus.serial.PARITY_NONE
instrument.serial.stopbits = DEVICE['stopbits']
instrument.mode = minimalmodbus.MODE_RTU
instrument.serial.timeout = TIMEOUT


def read_temperature():
    while True:
        # Register number, number of decimals, function code
        temperature = instrument.read_register(DEVICE['function_read_temperature']['register_address'],
                                               DEVICE['function_read_temperature']['number_decimals'],
                                               DEVICE['function_read_temperature']['modbus_function_code'])
        try:
            print(f"Value from Model: {MODEL_TYPE}")
            print(f"Temperature: {temperature} °C")
        except IOError:
            print("Failed to read from instrument")
        time.sleep(1)
        instrument.serial.close()
        # close connection


def read_humidity():
    while True:
        # Register number, number of decimals, function code
        humidity = instrument.read_register(DEVICE['function_read_humidity']['register_address'],
                                            DEVICE['function_read_humidity']['number_decimals'],
                                            DEVICE['function_read_humidity']['modbus_function_code'])
        try:
            print(f"Value from Model: {MODEL_TYPE}")
            print(f"Humidity: {humidity} %Rf")
        except IOError:
            print("Failed to read from instrument")
        time.sleep(1)
        instrument.serial.close()
        # close connection


def read_device_address():
    while True:
        # Register number, number of decimals, function code
        id = instrument.read_register(DEVICE['function_read_device_address']['register_address'],
                                      DEVICE['function_read_device_address']['number_decimals'],
                                      DEVICE['function_read_device_address']['modbus_function_code'])
        try:
            print(f"Value from Model: {MODEL_TYPE}")
            print(f"Hardware slave ID: {id} ")
        except IOError:
            print("Failed to read from instrument")
        time.sleep(1)
        instrument.serial.close()
        # close connection


def read_humidity_and_temp():
    while True:
        # Register number, number of register, function code
        value = instrument.read_registers(DEVICE['function_read_humi_temp']['register_address'],
                                          DEVICE['function_read_humi_temp']['number_registers'],
                                          DEVICE['function_read_humi_temp']['modbus_function_code'])
        try:
            print(f"Value from Model: {MODEL_TYPE}")
            print(f"Temperature: {value[0] / DEVICE['function_read_humi_temp']['out_divider']} °C")
            print(f"Humidity: {value[1] / DEVICE['function_read_humi_temp']['out_divider']} %Rf")
        except IOError:
            print("Failed to read from instrument")
        time.sleep(1)
        instrument.serial.close()
        # close connection

def change_baudrate(baudrate):
    while True:

        # Register number, number of register, function code
        instrument.write_register(DEVICE['function_change_baudrate']['register_address'],
                                          baudrate,
                                             DEVICE['function_change_baudrate']['number_decimals'],
                                          DEVICE['function_change_baudrate']['modbus_function_code'])
        try:
            print(f"Set Model Baudrate: {MODEL_TYPE}")
            print(f"Baudrate: {baudrate} HEX")
        except minimalmodbus.ModbusException:
            print("Failed to set new baudrate")
        time.sleep(1)
        instrument.serial.close()
        # close connection

# function list create
function = ("to exit program","temperature", "humidity", "humi_and_temp", "read_address","change device address","change baudrate")

# being output to CMD
while True:
    try:
        # Function selection block for CMD
        print("\r")
        print("Which function do you want to perform?")
        print("Choose from the following:")
        print("...........................................................................\r")
        for f in range(len(function)):
            print("What for a function do run:..(",  f , ")", function[f])
        print("...........................................................................\r")
        call_function = int(input("Enter the number of function:"))

        print("...........................................................................\r")
        print("Your selection was: ", function[call_function])

        # load function after selection
        match call_function:
            case 1:
                read_temperature()
            case 2:
                read_humidity()
            case 3:
                read_humidity_and_temp()
            case 4:
                read_device_address()
            case 5:
                print("Attention change the device address can lose connection!")
                choice = str.lower(input("Do you really want to change the address? Enter [Yes] or [No] :"))[:1]
                if choice == "y":
                    instrument.serial.close()  # todo add address change function
                    print(
                        "You need to disconnect the device from the power supply and restart it for the change to take effect.")
                if choice == "n":
                    print("\r Abort: Restart..............")
            case 6:
                print("Attention change the device baudrate can lose connection!")
                choice = str.lower(input("Do you really want to change the baudrate? Enter [Yes] or [No] :"))[:1]
                if choice == "y":
                    print("...........................................................................\r")
                    for key, value in DEVICE['function_change_baudrate']['baudrate'].items():
                        print("Supported baudrate:..(", key, ") = ", index(value))
                    print("...........................................................................\r")
                    baudrate = int(input("Select baudrate number:"))
                    selection = int(DEVICE['function_change_baudrate']['baudrate'][baudrate])
                    change_baudrate(selection)
                    # todo baudrate change get response from RX and handle exceptions
                    print(
                        "You need to disconnect the device from the power supply and restart it for the change to take effect.")
                if choice == "n":
                    print("\r Abort: Restart..............")
            case 0:
                time.sleep(1)
                sys.exit()

    except IOError:
        print("...function failure! Use debug mode!")
        time.sleep(3)
        sys.exit()
