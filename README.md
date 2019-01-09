# 2smpb02e-grove-raspberrypi
It is a module for evaluating Omron sensor 2SMPB-02E with Raspberry Pi 3 Model B and a sample program when using a module.  

2SMPB-02E is a compact MEMS absolute pressure sensor with high accuracy and low current consumption.  
Built-in 24-bit ADC with low noise, it can measure atmospheric pressure with high accuracy.  
Control and output are digital methods via the I2C/SPI interface, which realizes low current consumption by automatic sleep mode.

## language
- [English](./README.md)
- [Japanase](./README_ja.md)

## Description
- grove_2smpb_02e.py  
Driver module for acquiring data from 2SMPB-02E via GrovePi+.

- sample_2smpb_02e.py  
It is a sample program that allows you to check the data acquired via the driver module on the console.

- sample_gui_2smpb_02e.py  
It is a sample program that enables you to visualize and check the data acquired via the driver module with graphs.

***DEMO:***  
When you run sample_gui_2smpb_02e.py, you can see the following graph.  

![Graph_2SMPB](Graph_2SMPB.png)

## Installation
1. It is necessary to install dependency software beforehand.  
    [Dependencies](#link)
2. Open Terminal and execute the following command.    
    ```
    $ mkdir omron_sensor
    $ git clone https://github.com/omron-devhub/2smpb02e-grove-raspberrypi.git
    ```

## Usage
Procedure to operate the sample program.
-  sample_2smpb_02e.py  
Open Terminal and execute the following command.  
    ```
    $ cd omron_sensor
    $ sudo python3 sample_2smpb_02e.py
    ```
- sample_gui_2smpb_02e.py  
Open Terminal and execute the following command.  
    ```
    $ cd omron_sensor
    $ sudo python3 sample_gui_2smpb_02e.py
    ```

## Dependencies
2smpb02e-grove-raspberrypi requires the following dependencies:
- [Python3](https://www.python.org/)
- [GrovePi+](http://wiki.seeedstudio.com/GrovePi_Plus/)
- [matplotlib](https://matplotlib.org/)
- [smbus2](https://pypi.org/project/smbus2/)

## Licence
Copyright (c) OMRON Corporation. All rights reserved.

Licensed under the MIT License.
