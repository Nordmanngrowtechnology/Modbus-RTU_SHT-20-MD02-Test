# Read data with Modbus-RTU 485
### Modbus-RTU 485 Temp & Humidity sensor MD02

# Required 

- PC
- Modbus 485 serial to USB
- Sensor XY-MD02
- Voltage 12V DC
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
Change the connection port in script ([temp.py](temp.py), [humidity.py](humidity.py), [both.py](both.py))
to your experiment.

Run the files you want with python in command line terminal example temperature:

`python temp.py`

```
> C:\PyCharmMiscProject\Modbus-RTU_SHT-20-MD02-Test>python temp.py

MinimalModbus debug mode. Create serial port COM6
MinimalModbus debug mode. Will write to instrument (expecting 7 bytes back): 01 04 00 01 00 01 60 0A (8 bytes)
MinimalModbus debug mode. Clearing serial buffers for port COM6
MinimalModbus debug mode. No sleep required before write. Time since previous read: 556020781.36 ms, minimum silent period: 4.01 ms.
MinimalModbus debug mode. Response from instrument: 01 04 02 01 07 F9 62 (7 bytes), roundtrip time: 0.2 ms. Timeout for reading: 200.0 ms.

Temparatur: 26.3 °C

```

# In IDE use this running by clicking

`python temp.py`

`python humidity.py`

`python both.py`



### Keep in mind XY-MD02 or MD02
- There can use **UART** with Windows direct with a c++ script


### Documentation

The original documentation of the python extension: **MinimalModbus**

https://minimalmodbus.readthedocs.io/en/stable/usage.html#typical-usage

Sensor datasheet:
[xy-md02-manual.pdf](xy-md02-manual.pdf)


# Example 2

#### Connection schemata for 5 sensors
![ConnectionShemata.png](ConnectionShemata.png)

Create with https://lucid.app/lucidchart/ 'i become no money for that 🙄'

# TODO
- [ ] Add fritzing wiring png
- [ ] Add single bus wiring 4 x sensor and write python script