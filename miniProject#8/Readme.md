# RN2903 RF Interface Board — I²C EEPROM, UART and GPIO

## Overview

This project is a compact interface board designed for integration of a
Microchip RN2903 RF module with an external controller.

The board combines several useful interfaces on a single PCB:

- RN2903 UART communication
- Hardware RESET control
- I²C interface
- Two external AT24HC02C EEPROM devices
- Separate I²C addressing for both EEPROMs
- I²C pull-up resistors
- Additional GPIO connections for future expansion
- 3.3 V operation

The PCB was manufactured, assembled and tested with real hardware.

Two identical boards were assembled and used to validate bidirectional
RF communication.

---

## System Architecture

The external controller acts as the main controller of the system.

The basic architecture is:

    External Controller
           |
           |-- UART TX/RX --------> RN2903 RF Module
           |
           |-- RESET -------------> RN2903
           |
           |-- I²C SDA/SCL -------> EEPROM #1
           |                    |
           |                    +--> EEPROM #2
           |
           +-- GPIO -------------> Expansion / Test

The RN2903 and the EEPROM devices are independent interfaces.

The RN2903 communicates with the external controller through UART,
while the two EEPROM devices are accessed through the I²C bus.

---

## Power Supply

The board operates directly from a regulated **3.3 V supply**.

No DC/DC converter or voltage regulator is included on this PCB.

The 3.3 V supply must therefore be provided by the external system.

Local decoupling capacitors are used close to the devices to improve
power-supply stability.

---

## I²C EEPROM

Two **AT24HC02C EEPROM** devices are installed on the board.

Both devices share the same:

- SDA line
- SCL line
- 3.3 V supply
- Ground

Different hardware address configurations are used so that each EEPROM
can be accessed independently by the external I²C master.

The EEPROMs can be used to store, for example:

- configuration parameters
- device information
- calibration values
- identification data
- application-specific parameters

I²C pull-up resistors are included on the board.

When the board is connected to a controller that already contains
I²C pull-ups, the resulting equivalent pull-up resistance should be
checked.

---

## RN2903 RF Interface

The RN2903 module communicates with the external controller through
a standard UART interface.

Main signals:

    TX
    RX
    RESET
    3.3 V
    GND

The RESET signal is available to the external controller, allowing the
RN2903 to be restarted when required.

Additional GPIO signals are also available on the PCB for future
development and testing.

---

## RN2903 Communication

The RN2903 is controlled through its serial command interface.

Typical commands used during testing include:

    sys get ver
    mac pause
    radio set freq 923300000
    radio set sf sf7
    radio set bw 125
    radio set crc on
    radio rx 0

The exact RF configuration should always be selected according to the
application and the applicable regional radio-frequency regulations.

---

## Hardware Validation

Two identical interface boards were assembled for functional testing.

The test configuration was based on two independent RF nodes:

    PC / Terminal                         PC / Terminal
          |                                    |
        UART                                  UART
          |                                    |
       Board A                              Board B
          |                                    |
       RN2903  <--------- RF Link -------->  RN2903

Both boards were tested in transmission and reception.

This configuration made it possible to verify the complete
communication path in both directions.

Received and transmitted information was monitored through serial
terminals connected to the two test systems.

The assembled hardware was successfully tested and confirmed to be
functional.

---

## Python Test Utilities

Several Python utilities were developed during hardware validation.

The scripts communicate with the RN2903 through the serial port and
were used to:

- verify communication with the module
- send RN2903 commands
- configure RF parameters
- place the module in receive mode
- monitor received RF packets
- automate repetitive test sequences
- display module responses in a terminal

For example, the receiver test can automatically configure the module
and continuously restart the receive operation while monitoring
incoming `radio_rx` responses.

The Python scripts require a serial communication library such as
`pyserial`.

Example installation:

    pip install pyserial

The COM port defined in the scripts may need to be changed according
to the computer configuration.

---

## AT Command Interface — Practical Considerations

The RN2903 command interface is convenient for prototypes and relatively
small embedded applications.

It allows the external controller to configure and operate the RF module
without implementing the complete radio stack directly.

For applications requiring a limited amount of data exchange, this
approach is simple and practical.

For larger applications, however, the host software may become more
complex because it must manage:

- command sequences
- module responses
- timing
- communication states
- error handling
- data formatting

For this reason, this architecture is particularly suitable for:

- prototypes
- small RF projects
- telemetry
- remote control
- sensor communication
- low-volume data exchange
- laboratory testing

---

## PCB

The PCB was designed specifically for this project and has been
manufactured and assembled.

The repository includes the PCB design files as well as the manufacturing
outputs.

The hardware design provides access to the main communication signals
and additional GPIO connections for testing and future expansion.

---

## Gerber Files

Gerber manufacturing files are included in this repository.

They can be used to reproduce the PCB with a compatible PCB
manufacturing service.

Before ordering a PCB, it is recommended to verify:

- board dimensions
- layer configuration
- drill files
- Gerber files
- component footprints
- connector orientation

---

## Repository Contents

A typical repository structure is:

    RN2903-RF-Interface/
    |
    +-- README.md
    |
    +-- Schematic/
    |   +-- RN2903_Interface_Schematic.pdf
    |
    +-- PCB/
    |   +-- PCB design files
    |
    +-- Gerber/
    |   +-- Gerber manufacturing files
    |   +-- Drill files
    |
    +-- Datasheet/
    |   +-- RN2903 technical information
    |   +-- EEPROM technical information
    |
    +-- Software/
    |   +-- Python test utilities
    |
    +-- Images/
        +-- PCB views
        +-- Assembled board
        +-- Test setup

---

## Project Files

This repository provides the main resources required to study or
reproduce the project:

- complete electrical schematic
- PCB design
- Gerber manufacturing files
- component information
- RN2903 documentation
- EEPROM information
- Python test utilities
- hardware photographs
- test information

---

## Development and Test Status

**Schematic:** Completed  
**PCB:** Completed  
**PCB Manufacturing:** Completed  
**Assembly:** Completed  
**UART Interface:** Tested  
**RN2903 Communication:** Tested  
**Bidirectional RF Test:** Tested  
**Two-board Test:** Tested  
**Python Test Utilities:** Tested  
**I²C EEPROM Interface:** Implemented

---

## Future Development

The available GPIO connections make it possible to extend the project
without redesigning the complete interface board.

Possible future developments include:

- additional sensors
- external digital I/O
- automated RF test sequences
- EEPROM configuration tools
- communication diagnostics
- integration with another embedded controller

---

## Technologies

- Microchip RN2903
- AT24HC02C EEPROM
- I²C
- UART
- RF Communication
- 3.3 V Logic
- GPIO
- PCB Design
- Gerber
- Python
- PySerial
- Serial Terminal
- Embedded Systems

---

## Notes

This project was developed as a practical hardware and embedded
communication project.

RF parameters and operating frequencies must be configured according
to the regulations applicable in the country or region where the
hardware is used.

The design files and test software are provided for development,
education, prototyping and hardware evaluation purposes.
