#!/usr/local/bin/python3
# Extremely basic high/low byte splitter for ROMS -- Public Domain

fin = open( "tos.img", "rb" )

fhi = open( "high.img", "wb" )
flo = open( "low.img", "wb" )

byte = 1                # just want the next test to pass
while byte:             # stop at EOF
    byte = fin.read(1)  # read one byte
    fhi.write(byte)     # write it to the high file

    byte = fin.read(1)  # read one more byte
    flo.write(byte)     # write it the low file, then repeat

fin.close()
fhi.close()
flo.close()
