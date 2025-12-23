# GUITION-JC-ESP32-P4.M3-Dev

This repository contains board definitions and build/flashing instructions for the ESP32-P4 development board, tested with MicroPython.

```text
.
├── boards
│   └── ESP32_P4_KAKI5
│       ├── board.json
│       ├── board.md
│       ├── mpconfigboard.cmake
│       ├── mpconfigboard.h
│       ├── mpconfigvariant_C5_WIFI.cmake
│       ├── mpconfigvariant_C6_WIFI.cmake
│       └── sdkconfig.p4_kaki5
├── build-ESP32_P4_KAKI5-C6_WIFI
│   ├── esp32p4_flash.sh
│   └── firmware.bin
├── mpb_esp32p4c6.sh
├── README.md
└── scripts
    └── sysinfo.py

```

## 📦 Board Definitions

Board configuration files are located in:
`boards/ESP32_P4_KAKI5/`

## 🔨 Build Instructions

To build the firmware, run:

```bash
./mpb_esp32p4c6.sh
```

## ⚡ Flashing
1. Install esptool

Older versions of esptool may not work. Ensure you have esptool v5.1.0 or newer:

```bash
pip install esptool
```

2. Flash the Firmware

Connect the board to /dev/ttyUSB0 (or your respective serial port) and run:
```bash
./esp32p4_flash.sh /dev/ttyUSB0
```

Example successful output:
```text
esptool v5.1.0
Connected to ESP32-P4 on /dev/ttyUSB0:
Chip type:          ESP32-P4 (revision v1.3)
Features:           Dual Core + LP Core, 400MHz
Crystal frequency:  40MHz
MAC:                30:ed:a0:e3:0e:09

Stub flasher running.
Changing baud rate to 460800...
Changed.

Configuring flash size...
Flash will be erased from 0x00002000 to 0x001b6fff...
Compressed 1789216 bytes to 1030921...
Writing at 0x00002000... (progress)
Wrote 1789216 bytes (1030921 compressed) at 0x00002000 in 29.0 seconds (494.1 kbit/s).
Hash of data verified.
Hard resetting via RTS pin...
```

## 🖥️ System Info

After flashing, you can check system information in the MicroPython REPL:
```python
>>> import sysinfo
>>> sysinfo.show()
ID ............: 30eda0e30e09
MCU ...........: Generic
Memory
   total ......: 32318.5 KB
   usage ......: 17.40625 KB (0.051006004%)
   free .......: 32301.078 KB (99.94939%)
Filesystem
   total ......: 14336.0 KB
   usage ......: 12.0 KB (0.08370536%)
   free .......: 14324.0 KB (99.9163%)
SYSTEM
   platform ...: MicroPython-1.27.0-riscv-IDFv5.5.1-with-newlib4.3.0
   type .......: ESP32P4
   node .......: esp32
   release ....: 1.27.0
   version ....: v1.27.0-kaki5 on 2025-12-23
   board ......: Generic ESP32P4 module with WIFI module of external ESP32C6 with ESP32P4
   speed ......: 360000000 Hz
```

## 🌐 Network Setup
### LAN (Ethernet)
```python
import network
lan = network.LAN(mdc=31, mdio=52, power=51, ref_clk=50, phy_type=network.PHY_IP101, phy_addr=1)
lan.active(True)
lan.ifconfig()
# Example output: ('192.168.5.28', '255.255.252.0', '192.168.4.1', '192.168.4.1')
```

### WiFi Access Point (AP) Mode
```python
ap = network.WLAN(network.AP_IF)
ap.active(True)
ap.config(essid='Mata4Kaki5', password='GuaMusang', authmode=3)
ap.ifconfig(('10.10.6.1', '255.255.255.0', '10.10.6.1', '1.1.1.1'))
```

### WiFi Station (STA) Mode
```python
wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect("YourSSID", "YourPassword")
```

## 📡 Bluetooth Low Energy (BLE)
```python
import bluetooth
ble = bluetooth.BLE()
ble.active(True)
```

## 📦 Available Modules

The firmware includes the following built-in modules:

* Core: builtins, micropython, gc, sys, platform

* Hardware: machine, esp32, network, bluetooth

* Data & Encoding: json, struct, hashlib, binascii, collections

* Networking: socket, requests, websocket, tls

* Multitasking: asyncio, _thread

* Utilities: os, time, math, random, re, select, vfs

## 🧵 Multitasking Support

Both `asyncio` and `_thread` are available for concurrent programming.

## 🌍 HTTP Client

The requests module is included for HTTP operations:
```python
import requests
r = requests.get("http://example.com")
```

## 📦 Package Management

MicroPython’s mip package manager is available for installing additional libraries:
```python
import mip
mip.install("package-name")
```

## ✅ Verification

After setting up network interfaces, you can ping the assigned IP addresses to confirm connectivity.

Example:
```bash
ping 192.168.5.28
```

## 🔗 References

    see: unofficial_guition_esp32p4_repo, https://github.com/p1ngb4ck/unofficial_guition_esp32p4_repo/tree/main/JC-ESP32P4-M3-Dev


