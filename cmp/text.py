from cmp.icon import fontawesome_icon

def header_lg(text: str, add_class: str = ""):
    return f'<h1 class="font-header text-headerColor text-lg {add_class}">{text}</h1>'

def header_xl(text: str, add_class: str = ""):
    return f'<h1 class="font-header text-headerColor text-xl {add_class}">{text}</h1>'

def header_xxl(text: str, add_class: str = ""):
    return f'<h1 class="font-header text-headerColor text-2xl {add_class}">{text}</h1>'


def text_sm(text: str, add_class: str = ""):
    return f'<p class="font-text text-sm text-textColor {add_class}">{text}</p>'

def text_form_error(text: str, add_class: str = ""):
    return f'''<p class="font-text text-xs text-errColor {add_class}">{text}</p>'''