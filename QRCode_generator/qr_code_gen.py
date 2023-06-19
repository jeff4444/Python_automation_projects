#!/usr/bin/python3
import qrcode
import sys

if len(sys.argv) != 2:
    link = input("Please enter message or link: ").strip()
else:
    link = sys.argv[1]
qr_code = qrcode.QRCode()
qr_code.add_data(link)
qr_code.make()
img = qr_code.make_image()
img_name = input("Please enter the image name without extension: ").strip()
img.save(img_name + '.png')
