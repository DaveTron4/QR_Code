from qrcode.image.styles.moduledrawers import *
from qrcode.image.styles.colormasks import *

def get_drawer(qr_shape):
    if qr_shape =="none":
        return None
    elif qr_shape == "rounded":
        return RoundedModuleDrawer()
    elif qr_shape == "gapped_square":
        return GappedSquareModuleDrawer()
    elif qr_shape == "square":
        return SquareModuleDrawer()
    elif qr_shape == "circle":
        return CircleModuleDrawer()
    elif qr_shape == "vertical_bar":
        return VerticalBarsDrawer()
    elif qr_shape == "horizontal_bar":
        return HorizontalBarsDrawer()
    else:
        raise ValueError(f"Unknown QR shape: {qr_shape}")