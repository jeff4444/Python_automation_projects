#!/usr/bin/python3
from pyzbar.pyzbar import decode
from PIL import Image
import sys
import os

if len(sys.argv) != 2:
    img_name = input("Please type in image path, including its extension: ").strip()
else:
    img_name = sys.argv[1]

while not os.path.isfile(img_name):
    img_name = input("Image not found, please re-enter the correct path, including its extension: ").strip()

img = Image.open(img_name)
img = img.convert("L")
decoded_data = decode(img)

if decoded_data is None:
    print("Image does not contain QR Code or QR code could not be decoded")
else:
    link = decoded_data[0].data
    print('Decoded link/Message:', link.decode('utf-8'))
