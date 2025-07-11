import qrcode
from qrcode.image import svg

img = qrcode.make("Добрий день, Everybody!")
img.save("qr1.png")

# PNG QR

qr = qrcode.QRCode(
    version = 1,
    error_correction = qrcode.constants.ERROR_CORRECT_L,
    box_size=20,
    border=2
)

qr.add_data("https://github.com/AnnaKompan")
qr.make(fit=True)

img1 = qr.make_image(fill_color="pink",back_color="black")
img1.save("qr.png")

# SVG QR

factory = qrcode.image.svg.SvgPathImage
svg_img = qrcode.make("https://github.com/AnnaKompan", image_factory=factory)
svg_img.save("qr.svg")