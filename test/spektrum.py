# Tests the spektrum communication module
import sys
from dronestorm.comm import SpektrumRemoteReceiver

N=100
print("Testing Spektrum remote receiver")
print("Please ensure that:")
print("  - the remote receiver is connected properly to the pc")
print("  - the transmitter and receiver are bound")
print("  - the transmitter is on\n")

rrx = SpektrumRemoteReceiver()
try:
    rrx.align_serial()
    for i in range(N):
        rc_data = rrx.get_data()
        print(rc_data)
        # ser.write(data_buf)
except(KeyboardInterrupt, SystemExit):
    rrx.close_serial()
except(Exception) as ex:
    print ex
    rrx.close_serial()
