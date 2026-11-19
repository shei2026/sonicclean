# pip install "qrcode[pil]"
import qrcode
url = input("Pega el enlace de Vercel: ").strip()
qrcode.make(url).save("SonicClean_QR.png")
print("QR creado: SonicClean_QR.png")
