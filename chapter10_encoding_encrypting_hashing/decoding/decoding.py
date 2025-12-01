import base64 

# FILE NAME - decoding.py

# NAME - Nick Carlson
# DATE - 12/1/2025
# DESCRIPTION - decoding data from a file



def main():
    decode_data()

def decode_data():
    # OPEN FILE
    filename = input("File name? ")
    file = open(filename, "r")

    # GET DATA
    data = file.read()
    base64_bytes = data.encode('ascii')
    convert = base64.b64decode(base64_bytes)

    # OUTPUT DECODED DATA
    print(convert)

main()

