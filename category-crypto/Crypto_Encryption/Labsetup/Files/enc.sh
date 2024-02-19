#!/bin/bash

# The first line is necessary to inform the shell that this file
# is a bash shell script.  Script files must be marked executable
# by using chmod:
#
#     chmod u+x enc.sh
#
# Then they may be run:
#
#     ./enc.sh

# In the command below, replace '-ciphertype' with an actual cipher type
# and replace the input and output filenames.
#
# The key and initialization vector values will work with cipher
# block sizes up to 128 bits.  I.e., 32 hex digits, where a single hex digit
# is four bits, gives 128 bits.

# The '-e' switch is used for encryption.  Replace it with '-d' for
# decryption.

# The '\' at the very end of a line indicates that the current
# line should be continued on the next line.  This is a way to split
# up a long command without resorting to linewrapping.  Linewrapping should
# be banned.

openssl enc -ciphertype -e -in plain.txt -out cipher.bin \
    -K  00112233445566778899aabbccddeeff \
    -iv aabbccddeeff00112233445566778899

# You can copy, paste, and modify the lines above to work with multiple
# cipher types, input/output files, etc.
