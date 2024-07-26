from django import template
from menu_app.models import MenuItem
from django.core.exceptions import ObjectDoesNotExist

register = template.Library()


@register.inclusion_tag('menu/menu.html')
def draw_menu(menu_name: str = None, menu_item: str = None):

    items_to_draw = MenuItem.objects.filter(
        menu__name=menu_name)

    def get_current_menu(menu_item: str = None):
        if not menu_item:
            return list(items_to_draw.filter(parent=None))          
        return list(items_to_draw.filter(parent__name=menu_item))

    def insert_submenu(submenu: list = None, current_menu: list = None):
        if submenu:
            parent_index = current_menu.index(
                submenu[0].parent)
            current_menu.insert(
                parent_index + 1, submenu)
        return current_menu

    def build_menu(menu_item: str = None, submenu: list = None):
        current_menu = get_current_menu(menu_item=menu_item)
        insert_submenu(submenu=submenu, current_menu=current_menu)
        try:
            next_menu_item = items_to_draw.get(name=menu_item).parent.name
            return build_menu(menu_item=next_menu_item, submenu=current_menu)
        except AttributeError:
            return build_menu(submenu=current_menu)
        except ObjectDoesNotExist:
            return current_menu

    if menu_name == menu_item:
        return {'menu': build_menu()}
    else:
        return {'menu': build_menu(menu_item=menu_item)}
