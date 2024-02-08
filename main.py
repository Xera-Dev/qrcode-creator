import segno

lien = input("Entrez le lien du Qr Code: ")
qrcode = segno.make_qr(lien)
qrcode.save('qr.png', scale=10)