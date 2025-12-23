import gc
import os
import sys
import time
import machine as mc
from platform import platform
import binascii

def show():
    uname = os.uname()
    mem_total = gc.mem_alloc()+gc.mem_free()
    free_percent = "("+str((gc.mem_free())/mem_total*100.0)+"%)"
    alloc_percent = "("+str((gc.mem_alloc())/mem_total*100.0)+"%)"
    stat = os.statvfs('/flash')
    block_size = stat[0]
    total_blocks = stat[2]
    free_blocks  = stat[3]
    rom_total = (total_blocks * block_size)/1024
    rom_free = (free_blocks * block_size)/1024
    rom_usage = (rom_total-rom_free)
    rfree_percent = "("+str(rom_free/rom_total*100.0)+"%)"
    rusage_percent = "("+str(rom_usage/rom_total*100.0)+"%)"
    ID = binascii.hexlify(mc.unique_id())
    print("ID ............: ", end="")
    print(ID.decode())
    
    print("MCU ...........:",sys.implementation[2].split()[0])
    print("Memory")
    print("   total ......:",mem_total/1024,"KB")
    print("   usage ......:",gc.mem_alloc()/1024,"KB",alloc_percent)
    print("   free .......:",gc.mem_free()/1024,"KB",free_percent)
    print("Filesystem")
    print("   total ......:", rom_total,"KB" )
    print("   usage ......:", rom_usage,"KB",rusage_percent )
    print("   free .......:", rom_free,"KB",rfree_percent )
    print("SYSTEM")
    print("   platform ...:",platform())
    print("   type .......:",sys.implementation[2].split()[-1])
    print("   node .......:",uname.nodename)
    print("   release ....:",uname.release)
    print("   version ....:",uname.version)
    print("   board ......:",uname.machine)
    try:
       print("   speed ......:",mc.freq(), 'Hz')
    except:
       pass # nrf

