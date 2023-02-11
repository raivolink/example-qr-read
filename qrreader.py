from PIL import Image
from pyzbar import pyzbar


def read_qrcode_from_image(filename):
    """Reads imagefile and returns list of decoded data"""
    imgage = Image.open(filename)
    datalist_from_image = pyzbar.decode(imgage)
    return datalist_from_image
