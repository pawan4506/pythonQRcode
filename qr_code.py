import qrcode as qr


img = qr.make("hello world, I am pawandeep")
img.save("qrcodeimg.png")