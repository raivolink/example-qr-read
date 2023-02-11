from PIL import Image
from pyzbar import pyzbar


def read_qrcode_from_image(filename):
    """Reads imagefile and returns list of decoded data"""
    img = Image.open(filename)
    output = pyzbar.decode(img)
    return output
