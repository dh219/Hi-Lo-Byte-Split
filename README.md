# Hi-Lo-Byte-Split
An extremely basic Python script to split word-based data into high and low byte files. This is for use in programming 16 bit computer ROMs.

# Usage

* Place a ROM image to split in the same directory as the python script and name it 'tos.img' (this was written for Atari TOS, but will split anything it finds with that name).

* Run "python3 hi_low_byte_split.py"

* You should now find 'high.img' and 'low.img' in the working directory. These should be exactly half the size of the input file.

# Public Domain

This script was written by D Henderson in 2021. It is released to the public domain with no copyright claim.

# C version

There is an (even more basic) C version included here for systems that can't run python.
