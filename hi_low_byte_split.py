#!/usr/local/bin/python3
# Extremely basic high/low byte splitter for ROMS -- Public Domain

fin = open( "tos.img", "rb" )

fhi = open( "2way_high.img", "wb" )
flo = open( "2way_low.img", "wb" )

byte = 1                # just want the next test to pass
while byte:             # stop at EOF
    byte = fin.read(1)  # read one byte
    fhi.write(byte)     # write it to the high file

    byte = fin.read(1)  # read one more byte
    flo.write(byte)     # write it the low file, then repeat

fin.close()
fhi.close()
flo.close()

fhi = open( "2way_high.img", "rb" )
flo = open( "2way_low.img", "rb" )

fhi0 = open( "6way_high_0.img", "wb" )
fhi1 = open( "6way_high_1.img", "wb" )
fhi2 = open( "6way_high_2.img", "wb" )

flo0 = open( "6way_low_0.img", "wb" )
flo1 = open( "6way_low_1.img", "wb" )
flo2 = open( "6way_low_2.img", "wb" )

# let's then further split those into 6 for the pre-STE range

byte = 1                # just want the next test to pass
while byte:             # stop at EOF
    byte = fhi.read(1)  # read one byte from high
    fhi0.write(byte)     # write it to the high 0 file

    byte = fhi.read(1)  # read one byte from high
    fhi1.write(byte)     # write it to the high 1 file

    byte = fhi.read(1)  # read one byte form high
    fhi2.write(byte)     # write it to the high 2 file


# same now for low

byte = 1                # just want the next test to pass
while byte:             # stop at EOF
    byte = flo.read(1)  # read one byte from low
    flo0.write(byte)     # write it to the low 0 file

    byte = flo.read(1)  # read one byte from low
    flo1.write(byte)     # write it to the low 1 file

    byte = flo.read(1)  # read one byte form low
    flo2.write(byte)     # write it to the low 2 file

fhi.close()
flo.close()

fhi0.close()
fhi1.close()
fhi2.close()
flo0.close()
flo1.close()
flo2.close()
