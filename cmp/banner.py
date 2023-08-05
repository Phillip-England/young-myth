from cmp.text import header_xl, text_sm
from cmp.icon import fontawesome_icon

class GuestBanner:
    def __init__(self):
        self.bars_id = 'guest-banner-bars'
        self.x_id = 'guest-banner-x'
    def HTML(self):
        return f'''
			<div class="h-20 fixed top-0 w-full border-b-4 border-gray-200 justify-between flex items-center">
				<div class="p-4">
					{header_xl(text="CFA Suite")}
					{text_sm(text="Keep up with your ever growing team")}
				</div>
				<div id="{self.bars_id}" class="p-4">
					{fontawesome_icon('fa-bars', 'fa-lg')}
				</div>
				<div id="{self.x_id}" class="p-4 hidden">
					{fontawesome_icon('fa-x', 'fa-lg')}
				</div>
			</div>
			<div class="h-20"></div>
		'''


