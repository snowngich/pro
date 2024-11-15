import pyqrcode
from PIL import Image
link=input("enter anthing to generate QR code: ")
qr_code=pyqrcode.create(link)
qr_code.png("QRCode.png",scale=5)
Image.open("QRCode.png")
