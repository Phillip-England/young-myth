class GuestNavOverlay:
    def __init__(self):
        self.id = 'guest-nav-overlay'
        self.selector = f'#{self.id}'
    def HTML(self):
        return f'<div _="" id="{self.id}" class="fixed hidden opacity-50 bg-black top-0 w-full h-full z-30"></div>'