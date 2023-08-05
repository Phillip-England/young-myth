
from const.hs import HS_CLICK_GUEST_BANNER_BARS, HS_CLICK_GUEST_BANNER_X
from const.dom import GUEST_BANNER_BARS_ID, GUEST_BANNER_X_ID

from cmp.text import header_xl, text_sm
from cmp.icon import fontawesome_icon


def guest_banner():
	return f'''
		<div class="h-20 fixed bg-white z-50 top-0 w-full border-b-4 border-gray-200 justify-between flex items-center">
			<div class="p-4">
				{header_xl(text="CFA Suite")}
				{text_sm(text="Keep up with your ever growing team")}
			</div>
			<div {HS_CLICK_GUEST_BANNER_BARS} id="{GUEST_BANNER_BARS_ID}" class="p-4">
				{fontawesome_icon('fa-bars', 'fa-lg')}
			</div>
			<div {HS_CLICK_GUEST_BANNER_X} id="{GUEST_BANNER_X_ID}" class="p-4 hidden">
				{fontawesome_icon('fa-x', 'fa-lg')}
			</div>
		</div>
		<div class="h-20"></div>
	'''


