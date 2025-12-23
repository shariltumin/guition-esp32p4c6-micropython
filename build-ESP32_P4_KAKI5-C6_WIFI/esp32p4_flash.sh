#!/bin/sh
esptool --port $1 \
    --chip esp32p4 \
    --baud 460800 write-flash \
    -z 0x2000 firmware.bin

