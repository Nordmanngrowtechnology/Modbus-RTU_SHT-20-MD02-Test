# Read data with Modbus-RTU 485
### Modbus-RTU 485 T
Temp & Humidity sensor MD02

## Difference between sensor MD02 and XY-MD02

| Model   | Voltage    | Raster       | Onboard-LED | Advantage                                                    | Performence  |
|---------|------------|--------------|-------------|--------------------------------------------------------------|--------------|
| MD02    | DC 5-30V   | smaller 2,54 | Yes RED     |                                                              | A bit slower |
| XY-MD02 | DC 5-30V   | 2,54         | No          | The larger grid makes it easier to perform a factory reset.  |              |

<img src="difference_between_XY-MD02_MD02.jpg" width="800">

### Register difference
- XY-MD02 the values came as flot
- MD02 the values came no flot and must divided by 100

If the return value of humidity and temperature divide by 100 correct
and had the sensor a red LED onboard so is it in most case MD02 version.

Shown below in table difference in selectable baud rates


# Required 

- PC
- Modbus 485 serial to USB
- Sensor XY-MD02
- Voltage DC 5V - 28V for scenarios with long range
- Wiring

# Install
Install python and add python extension  **MinimalModbus**

`pip install -U minimalmodbus`

Clone project via git or download project files

`git clone https://github.com/Nordmanngrowtechnology/Modbus-RTU_SHT-20-MD02-Test.git`


# Usage

Open command line tool and navigate to project folder example:

```
>> C:\Users> cd C:\PyCharmMiscProject\Modbus-RTU_SHT-20-MD02-Test

>>> C:\PyCharmMiscProject\Modbus-RTU_SHT-20-MD02-Test>
```
Change the connection port in script ([sensor.py](sensor.py))


Run the files you want with python in command line terminal example temperature:

`python sensor.py`

Follow the instruction on screen and select the self-described function.


###### Keep in mind XY-MD02 or MD02
- There can use **UART** with Windows direct with a c++ script


## Modbus function register
This device support this standard modbus 485 function codes.

| Modbus code int |                              |
|-----------------|------------------------------|
| 3               | Read keep register           |
| 4               | Read input register          |
| 6               | Write a single keep register |
| 10              | Write more keep register     |


## Modbus register map difference

| Model    |                         | Register | Function code | Support                  |
|----------|-------------------------|----------|---------------|--------------------------|
| MD02     | set baudrate            | 257      | 6             | 0:2400, 1:4800, 2:9600   |
| MD02     | set new device address  | 256      | 6             |                          |
| XY-MD02  | set baudrate            | 258      | 6             | 0:9600, 1:14400, 2:19200 |
| XY-MD02  | set new device address  | 257      | 6             |                          |

## Response code
 
#### Change slave baudrate to 9600

|    | Function |    |    |    | New Baudrate |    |    |
|----|----------|----|----|----|--------------|----|----|
| 01 | 06       | 01 | 01 | 00 | 02           | 58 | 37 |


### Documentation

The original documentation of the python extension: **MinimalModbus**

https://minimalmodbus.readthedocs.io/en/stable/usage.html#typical-usage

Sensor datasheet:
[MD02-manual.pdf](MD02-manual.pdf)

[xy-md02-manual.pdf](xy-md02-manual.pdf)

# HELP ERRORS & PROBLEMS

#### No connection no receive data from device
In some cases came sensors to me, I had ordered the labeling on
case was incorrect after opening the device see on the pcb board
the correct connection.

<img src="Modbus-SHT20_MD02_incorrect_label.jpg" width="300">

Remove the label and turn around.

# Hardware reset of MD02 and XY-MD02
If you lose the connection to the devices by losing the device address.

## Do a hardware reset:
Open the case and bridge the bin GND+RST tron power on and wait 20 seconds
for restoring the factory defaults.

# TODO
- [ ] Add wiring png
- [ ] Add single bus wiring 4 x sensor and write python script
- [ ] Extend scrip for device address change
- [ ] Add address change function
- [x] ~~Add baudrate change function~~
- [ ] Add function read keep register 0x03 address 0x0102 read baudrate
- [ ] Add function read keep register 0x03 address 0x0101 read device address with device id 0x00 ???
- Add option for set baud
- Add option for set device id