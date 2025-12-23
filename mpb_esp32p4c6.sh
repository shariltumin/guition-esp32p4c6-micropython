#!/bin/bash

export PATH="$HOME/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin"

echo "=========================================================="
echo "Setting up for esp32xx build"
echo "Using esp-idf-551"
export IDF_PATH="$HOME/disk/esp/esp-idf-551"
echo "MCU type esp32p4-c6"
export IDF_TARGET="esp32p4"
source $IDF_PATH/export.sh

# clean-up last build
rm -rf build-ESP32_P4_KAKI5-C6_WIFI

# ESP32-P4+C6
make V=1 BOARD=ESP32_P4_KAKI5 BOARD_VARIANT=C6_WIFI
echo "=========================================================="

