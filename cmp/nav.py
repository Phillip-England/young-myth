from const.dom import GUEST_NAV_MENU_ID
from const.hs import HS_CLICK_GUEST_NAV_LINK

def guest_nav_menu(path: str):
	return f'''
		<nav id="{GUEST_NAV_MENU_ID}" hx-boost="true" class="hidden fixed z-40 bg-white top-20 h-full w-3/5 border-r border-r-2 border-r-gray-200">
			<ul class="flex flex-col">
				{nav_menu_list_item(text="Home", href="/", path=path, hs_event=HS_CLICK_GUEST_NAV_LINK)}
				{nav_menu_list_item(text="Login", href="/login", path=path, hs_event=HS_CLICK_GUEST_NAV_LINK)}
				{nav_menu_list_item(text="Signup", href="/signup", path=path, hs_event=HS_CLICK_GUEST_NAV_LINK)}
			</ul>
		</nav>
	'''
        

def nav_menu_list_item(text: str, href: str, path: str, hs_event: str = ""):
    if href == path:
        return f'''
			<li _="{hs_event}" class="flex border border-l-2 border-t-2 border-gray-200 m-1 rounded">
				<a class="p-4 w-full font-text text-sm underline text-main" href={href}>{text}</a>
			</li>
		'''
    return f'''
		<li _="{hs_event}" class="flex border border-gray-200 m-1 rounded">
			<a class="p-4 w-full font-text text-sm" href={href}>{text}</a>
		</li>
	'''
