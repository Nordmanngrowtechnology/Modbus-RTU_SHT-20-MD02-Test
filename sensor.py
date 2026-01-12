#!/usr/bin/env python
import sys
import minimalmodbus
import time
import devices

# slave address (in decimal)
DEVICE_ADDRESS = 1
# ENABLE/DISABLE communication debug mode
DEVICE_DEBUG = True
# Master PORT name -- Change as needed for your host.
PORT_NAME = 'COM6'
# Model type new or old default XY-MD02. Other MD02
MODEL_TYPE = 'MD02'
TIMEOUT = 3

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
                    instrument.serial.close()  # todo add baudrate change function
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
