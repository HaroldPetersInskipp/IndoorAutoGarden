# SPDX-FileCopyrightText: 2021 ladyada for Adafruit Industries
# SPDX-License-Identifier: MIT

"""
Initializes the sensor, gets and prints readings every two seconds.
"""
import time
import board
import adafruit_si7021
import sys

# Create library object using our Bus I2C port
sensor = adafruit_si7021.SI7021(board.I2C())

#print("\nTemperature: %0.1f C" % sensor.temperature)
#print("Humidity: %0.1f %%" % sensor.relative_humidity)
print("%0.1f" % sensor.relative_humidity)
sys.exit(0)
