from PIL import Image
from pyzbar import pyzbar

filename = "devdata/qr-link.png"


def read_qrcode_from_image(filename):
    img = Image.open(filename)
    output = pyzbar.decode(img)
    data_as_string = output[0].data.decode("utf-8")
    print(data_as_string)
    # return output


read_qrcode_from_image(filename)
