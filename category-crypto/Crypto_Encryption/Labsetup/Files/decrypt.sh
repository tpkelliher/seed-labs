#!/bin/bash

# This bash script will "decrypt" the file ciphertext.txt by using tr
# to replace each letter in 'cipher' with the corresponding letter in
# 'plain', piping the resulting decryption to the less pager for viewing.

# cipher MUST only contain lowercase letters.  For example:
#     cipher="aie"

cipher=""

# plain MUST only contain uppercase letters.

plain=""


# Perform some validity checking on cipher and plain.

if [[ "$cipher" == "" || "$plain" == "" ]]; then
    echo "cipher is empty or plain is empty.  Fix."
    exit 1
fi

if [[ ${#cipher} -ne ${#plain} ]]; then
    echo "cipher and plain have different lengths.  Fix."
    exit 1
fi

if [[ "$cipher" =~ [[:upper:]] ]]; then
    echo "cipher must not contain uppercase letters."
    exit 1
fi

if [[ "$plain" =~ [[:lower:]] ]]; then
    echo "plain must not contain lowercase letters."
    exit 1
fi

tr $cipher $plain < ciphertext.txt | less
exit 0
