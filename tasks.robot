*** Settings ***
Documentation       Reads QR code image from file

Library             qrreader


*** Tasks ***
Minimal task
    ${data_from_qr}    Read Qrcode From Image    devdata${/}qr-link.png
    Log    ${data_from_qr}    console=true
