#!/usr/bin/env python

# Description of the device model: XY-MD01
# Standard settings und function dictionary
DEVICE_XY_MD01 = {
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
        'number_registers': 1,
        'out_divider': 100
    },
    'function_change_baudrate': {
        'name': 'Change baudrate',
        'description': 'Change baudrate the communication baudrate of slave',
        'register_address': 0x0101,  # is the register 257 for storing the sensor baud rate
        'modbus_function_code': 0x06,
        'number_decimals': 0,
        'baudrate': {
            0: 2400,
            1: 4800,
            2: 9600,
        },
    },
    'function_change_address': {
        'name': 'Change device address',
        'description': 'Change the device address of slave',
        'register_address': 0x0100,# is the register 256 for storing the device address
        'modbus_function_code': 0x06,
        'number_decimals': 0,
        'address_range': {
            'min': 1,
            'max': 247, # device range 01-247
        },
    },

}

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
    'function_change_baudrate': {
        'name': 'Change baudrate',
        'description': 'Change baudrate the communication baudrate of slave',
        'register_address': 0x0101,  # is the register 257 for storing the sensor baud rate
        'modbus_function_code': 0x06,
        'number_decimals': 0,
        'baudrate': {
            0: 2400,
            1: 4800,
            2: 9600,
        },
    },
    'function_change_address': {
        'name': 'Change device address',
        'description': 'Change the device address of slave',
        'register_address': 0x0100,# is the register 256 for storing the device address
        'modbus_function_code': 0x06,
        'number_decimals': 0,
        'address_range': {
            'min': 1,
            'max': 251, # device range 01-251
        },
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
    'function_change_baudrate': {
        'name': 'Change baudrate',
        'description': 'Change baudrate the communication baudrate of slave',
        'register_address': 0x0102,# 258 for storing the sensor baud rate
        'modbus_function_code': 0x06,
        'number_decimals': 0,
        'baudrate': {
            0: 9600,
            1: 14400,
            2: 19200,
        }

    },
    'function_change_address': {
        'name': 'Change device address',
        'description': 'Change the device address of slave',
        'register_address': 0x0101,# is the register 256 for storing the device address
        'modbus_function_code': 0x06,
        'number_decimals': 0,
        'address_range': {
            'min': 1,
            'max': 247, # device range 01-247
        },
    },
}

# Description of the device model: Humidity & Temperature sensor SHT30 with asian label
# Standard settings und function dictionary
DEVICE_SHT30_ASIAN = {
    'name': 'SHT30-ASIAN',
    'baudrate': 9600,
    'parity': 'N',
    'stopbits': 1,
    'bytesize': 8,
    'device_address': 0x01,
    'function_read_temperature': {
        'name': 'Read temperature',
        'description': 'Read the temperature from slave',
        'register_address': 0x0001,
        'modbus_function_code': 0x03,
        'number_decimals': 1,
    },
    'function_read_humidity': {
        'name': 'Read humidity',
        'description': 'Read the humidity from slave',
        'register_address': 0x0000,
        'modbus_function_code': 0x03,
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
    'function_change_baudrate': {
        'name': 'Change baudrate',
        'description': 'Change baudrate the communication baudrate of slave',
        'register_address': 0x0102,# 258 for storing the sensor baud rate
        'modbus_function_code': 0x06,
        'number_decimals': 0,
        'baudrate': {
            0: 9600,
            1: 14400,
            2: 19200,
        }

    },
    'function_change_address': {
        'name': 'Change device address',
        'description': 'Change the device address of slave',
        'register_address': 0x0101,# is the register 256 for storing the device address
        'modbus_function_code': 0x06,
        'number_decimals': 0,
        'address_range': {
            'min': 1,
            'max': 255, # device range 01-255
        },
    },
}

DEVICES = {
    "MD02": DEVICE_MD02,
    "XY-MD01": DEVICE_XY_MD01,
    "XY-MD02": DEVICE_XY_MD02,
    "SHT30-ASIAN": DEVICE_SHT30_ASIAN,
}
