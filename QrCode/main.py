import segno  #import library

lien = input("Entrez le lien du Qr Code: ") #Qr Code link
qrcode = segno.make_qr(lien)
qrcode.save('qr.png', scale=10) #Qr Code generation  name: "qr.png"
