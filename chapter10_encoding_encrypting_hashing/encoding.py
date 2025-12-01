import base64 

# FILE NAME - encoding.py

# NAME - Nick Carlson
# DATE - 12/1/2025
# DESCRIPTION - encoding and printing text from a file

  



def main():
    encode_data()

def encode_data():
    # OPEN FILE
    filename = input("File name? ")
    file = open(filename, "r")

    # GET DATA
    data = file.readlines()
    convert = data.encode('ascii')
    base64_bytes = base64.b64encode(convert)
    base64_string = base64_bytes.decode('ascii')

    # OUTPUT ENCODED DATA
    print(base64_string)





main()
