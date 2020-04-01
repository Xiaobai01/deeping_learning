import qrcode
ipa="id 123456789 type asjkhiu "
qr=qrcode.QRCode(version=1,
                 error_correction=qrcode.constants.ERROR_CORRECT_L,
                 box_size=8,
                 border=8,
                 )
qr.add_data(ipa)
qr.make(fit=True)
img=qr.make_image()
img.save('data.png')