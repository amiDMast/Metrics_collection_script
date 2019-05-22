#!/usr/local/bin/python
import psutil
from sys import argv

data_cpu = psutil.cpu_times()
data_mem = psutil.virtual_memory()
data_sw  = psutil.swap_memory()

def cpu():
        print'CPU'
        print'  system metrics:'
        print'          idle   = ', data_cpu[3]
        print'          user   = ', data_cpu[0]
        print'          guest  = ', data_cpu[8]
        print'          iowai  = ', data_cpu[5]
        print'          stolen = ', data_cpu[7]
        print'          system = ', data_cpu[2]

def mem():
        print'Memory'
        print'  vitrual:'
        print'          total  = ', data_mem[0]
        print'          used   = ', data_mem[3]
        print'          free   = ', data_mem[4]
        print'          shared = ', data_mem[9]
        print'  swap:'
        print'          total  = ', data_sw[0]
        print'          used   = ', data_sw[1]
        print'          free   = ', data_sw[2]

if len(argv) != 2:
        cpu()
        mem()
        exit()
script, argv = argv
if 'cpu' in argv: cpu()
elif 'mem' in  argv: mem()
else:
        print'You can use two parameters: cpu or mem. ', argv, ' - wrong parameter'
        cpu()
        mem()
