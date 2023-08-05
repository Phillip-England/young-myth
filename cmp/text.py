def header_xl(text: str, add_class: str = ""):
    return f'<h1 class="font-header text-main text-xl {add_class}">{text}</h1>'

def header_xxl(text: str, add_class: str = ""):
    return f'<h1 class="font-header text-main text-2xl {add_class}">{text}</h1>'


def text_sm(text: str):
    return f'<p class="font-text text-sm">{text}</p>'