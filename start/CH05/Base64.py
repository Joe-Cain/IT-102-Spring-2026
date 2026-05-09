#!/usr/bin/env python3
# Script that "encrypts"/"decrypts" text using base64 encoding
# By Joe Cain

'''
This script is to encode and decode input using BASE64
'''

#imported libraries
import base64


def encode_to_base64(plaintext: str) -> str:
    '''
encoding plaintext to base64
1.) Convert string using UTF-8
2.) Pass the bytes into a function called b64.encode
3.) Resulted bytes and return
    '''
    text_as_bytes = plaintext.encode("utf-8")
    encoded_bytes = base64.b64encode(text_as_bytes)
    return encoded_bytes.decode("utf-8")


def decode_to_base_64(encoded_text: str) -> str:
    '''
Taking base64 string back to original plaintext
1.) Convert base64 sring to get original bytes
2.) Decode bytes back to utf-8 string
    '''
    encoded_as_bytes = encoded_text.encode("utf-8")
    decoded_bytes = base64.b64encode(encoded_as_bytes)
    return decoded_bytes.decode("utf-8")

#Define main - What we want to call and how

def main():
    print("Base64 Encoder / Decoder")
    print("This is NOT encryption")
    #User input to encode
    message = input("Enter message to encode: ").strip()
    if not message:
        print("No message entered. Exiting")
        return    
    #Encode
    encoded = encode_to_base64(message)
    print(f"Base64 : {encoded}")     


    #Decode
    decoded = decode_to_base_64(encoded)

    #Validation
    match = decoded == message
    print("Confirmation matched")
    print()



if __name__ == "__main__":
        main()