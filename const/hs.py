

from const.dom import (
    GUEST_BANNER_BARS_ID,
    GUEST_BANNER_X_ID,
    GUEST_NAV_MENU_ID,
    GUEST_NAV_OVERLAY_ID,
    BIG_LOADER_ID,
)

# guest hyperscript commands
HS_CLICK_GUEST_BANNER_BARS = f"on click toggle .hidden on me then toggle .hidden on #{GUEST_BANNER_X_ID} then toggle .hidden on #{GUEST_NAV_MENU_ID} then toggle .hidden on #{GUEST_NAV_OVERLAY_ID}"
HS_CLICK_GUEST_BANNER_X = f"on click toggle .hidden on me then toggle .hidden on #{GUEST_BANNER_BARS_ID} then toggle .hidden on #{GUEST_NAV_OVERLAY_ID} then toggle .hidden on #{GUEST_NAV_MENU_ID}"
HS_CLICK_GUEST_NAV_OVERLAY = f"on click toggle .hidden on me then toggle .hidden on #{GUEST_BANNER_BARS_ID} then toggle .hidden on #{GUEST_NAV_MENU_ID} then toggle .hidden on #{GUEST_BANNER_X_ID}"
HS_CLICK_GUEST_NAV_LINK = f"on click toggle .hidden on #{GUEST_NAV_MENU_ID} then toggle .hidden on #{GUEST_NAV_OVERLAY_ID} then toggle .hidden on #{GUEST_BANNER_X_ID} then toggle .hidde on #{GUEST_BANNER_BARS_ID} then toggle .hidden on #{BIG_LOADER_ID}"
