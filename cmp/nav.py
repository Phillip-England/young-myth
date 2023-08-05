from const.dom import GUEST_NAV_MENU_ID

def guest_nav_menu(path: str):
	return f'''
		<nav id="{GUEST_NAV_MENU_ID}" hx-boost="true" class="hidden fixed z-40 bg-white top-20 h-full w-3/5 border-r border-r-2 border-r-gray-200">
			<ul class="flex flex-col">
				{nav_menu_list_item(text="Home", href="/", path=path)}
				{nav_menu_list_item(text="Login", href="/login", path=path)}
				{nav_menu_list_item(text="Signup", href="/signup", path=path)}
			</ul>
		</nav>
	'''
        

def nav_menu_list_item(text: str, href: str, path: str):
    if href == path:
        return f'''
			<li class="flex border border-gray-200 m-1 rounded">
				<a class="p-4 w-full font-text text-sm underline text-main" href={href}>{text}</a>
			</li>
		'''
    return f'''
		<li class="flex border border-gray-200 m-1 rounded">
			<a class="p-4 w-full font-text text-sm" href={href}>{text}</a>
		</li>
	'''
