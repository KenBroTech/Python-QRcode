import qrcode
url = 'https://www.youtube.com/kenbrotech'
image = qrcode.make(url)
image.save('kbt_qrcode.jpg')
