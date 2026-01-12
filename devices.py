#!/usr/bin/env python

# Description of the device model: MD02
# Standard settings und function dictionary
DEVICE_MD02 = {
    'name': 'MD02',
    'baudrate': 9600,
    'parity': 'N',
    'stopbits': 1,
    'bytesize': 8,
    'device_address': 0x01,
    'function_read_temperature': {
        'name': 'Read temperature',
        'description': 'Read the temperature from slave',
        'register_address': 0x0001,
        'modbus_function_code': 0x04,
        'number_decimals': 2,
    },
    'function_read_humidity': {
        'name': 'Read humidity',
        'description': 'Read the humidity from slave',
        'register_address': 0x0002,
        'modbus_function_code': 0x04,
        'number_decimals': 2,
    },
    'function_read_device_address': {
        'name': 'Read the device address',
        'description': 'Read the device address from slave',
        'register_address': 0x0101,
        'modbus_function_code': 0x03,
        'number_decimals': 0,
    },
    'function_read_humi_temp': {
        'name': 'Read Humidity & Temperature',
        'description': 'Read Humidity & Temperature from slave',
        'register_address': 0x0001,
        'modbus_function_code': 0x04,
        'number_registers': 2,
        'out_divider': 100
    },

}

# Description of the device model: XY-MD02
# Standard settings und function dictionary
DEVICE_XY_MD02 = {
    'name': 'XY-MD02',
    'baudrate': 9600,
    'parity': 'N',
    'stopbits': 1,
    'bytesize': 8,
    'device_address': 0x01,
    'function_read_temperature': {
        'name': 'Read temperature',
        'description': 'Read the temperature from slave',
        'register_address': 0x0001,
        'modbus_function_code': 0x04,
        'number_decimals': 1,
    },
    'function_read_humidity': {
        'name': 'Read humidity',
        'description': 'Read the humidity from slave',
        'register_address': 0x0002,
        'modbus_function_code': 0x04,
        'number_decimals': 1,
    },
    'function_read_device_address': {
        'name': 'Read the device address',
        'description': 'Read the device address from slave',
        'register_address': 0x0101,
        'modbus_function_code': 0x03,
        'number_decimals': 0,
    },
    'function_read_humi_temp': {
        'name': 'Read Humidity & Temperature',
        'description': 'Read Humidity & Temperature from slave',
        'register_address': 0x0001,
        'modbus_function_code': 0x04,
        'number_registers': 2,
        'out_divider': 10
    },

}

DEVICES = {
    "MD02": DEVICE_MD02,
    "XY-MD02": DEVICE_XY_MD02,
}
