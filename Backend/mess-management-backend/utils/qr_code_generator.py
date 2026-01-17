from io import BytesIO
import qrcode
from django.core.files.base import ContentFile

def generate_qr_code(data):
    """Generate a QR code image from the given data."""
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    img_bytes = BytesIO()
    img.save(img_bytes, format='PNG')
    img_bytes.seek(0)

    return ContentFile(img_bytes.read(), name='qr_code.png')