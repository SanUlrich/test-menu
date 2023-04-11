from django import template
from ..models import Menu, MenuItem

register = template.Library()


@register.inclusion_tag("menu/menu.html")
def draw_menu(menu_name, slug=None, is_active=True):
    try:
        obj = Menu.objects.get(title__iexact=menu_name)

    except Menu.DoesNotExist:
        return {"header": f'Меню {menu_name} не существует'}

    context = {
        "id": obj.pk,
        "url": obj.get_absolute_url(),
        "header": obj.title,
    }

    if is_active:
        context["items"] = obj.children.all()

    return context
