
from const.dom import GUEST_NAV_OVERLAY_ID
from const.hs import HS_CLICK_GUEST_NAV_OVERLAY

class GuestNavOverlay:
    def __init__(self):
        pass
    def HTML(self):
        return f'<div {HS_CLICK_GUEST_NAV_OVERLAY} id="{GUEST_NAV_OVERLAY_ID}" class="fixed hidden opacity-50 bg-black top-0 w-full h-full z-30"></div>'