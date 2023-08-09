def icon_bars():
    return f'<i class="fa-solid fa-bars fa-lg"></i>'


def icon_x():
    return f'<i class="fa-solid fa-bars fa-lg"></i>'


def fontawesome_icon(icon_name: str, add_class: str = "", icon_size: str = ""):
    return (
        f'<i class="fa-solid {icon_name} {icon_size} text-textColor {add_class}"></i>'
    )
