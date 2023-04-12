from django import template
from ..models import Menu

register = template.Library()


@register.inclusion_tag("menu/menu.html")
def draw_menu(menu_name):
    try:
        obj = Menu.objects.get(title__iexact=menu_name)
    except Menu.DoesNotExist:
        return {"header": f'Меню {menu_name} не существует'}

    context = {
        "id": obj.pk,
        "url": obj.get_absolute_url(),
        "header": obj.title,
        "items": obj.children.all(),
    }

    return context
