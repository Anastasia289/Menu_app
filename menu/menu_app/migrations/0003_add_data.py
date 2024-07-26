from django.db import migrations


def add_data(apps, schema_editor):

    Menu = apps.get_model("menu_app", "Menu")

    data = [
        {'name': 'первое'},
        {'name': 'второе'},
    ]
    for row in data:
        Menu.objects.update_or_create(**row)
    
    MenuItem = apps.get_model("menu_app", "MenuItem")

    data = [
        { "id": 1, 'name': 'подпункт1', "menu_id": 1, },
        { "id": 2, 'name': 'подпункт2', "menu_id": 1, },
        { "id": 3, 'name': 'подпункт3', "menu_id": 1, },
        { "id": 4, 'name': 'подпункт4', "menu_id": 2, },
        { "id": 5, 'name': 'подпункт5', "menu_id": 2, },
        { "id": 6, 'name': 'подпункт6', "menu_id": 2, },    
        { "id": 7, 'name': 'подпункт1-1', "menu_id": 1, "parent_id": 1},
        { "id": 8, 'name': 'подпункт1-2', "menu_id": 1, "parent_id": 1},
        { "id": 9, 'name': 'подпункт1-3', "menu_id": 1, "parent_id": 1},
        { "id": 10, 'name': 'подпункт2-1', "menu_id": 1, "parent_id": 2},
        { "id": 11, 'name': 'подпункт2-2', "menu_id": 1, "parent_id": 2},
        { "id": 12, 'name': 'подпункт2-3', "menu_id": 1, "parent_id": 2},
        { "id": 13, 'name': 'подпункт3-1', "menu_id": 1, "parent_id": 3},   
        { "id": 14, 'name': 'подпункт1-1-1', "menu_id": 1, "parent_id": 7},
        { "id": 15, 'name': 'подпункт1-1-2', "menu_id": 1, "parent_id": 7},    
        { "id": 16, 'name': 'подпункт1-2-1', "menu_id": 1, "parent_id": 8},
        { "id": 17, 'name': 'подпункт1-3-1', "menu_id": 1, "parent_id": 9},

    ]
    for row in data:
        MenuItem.objects.update_or_create(**row)
        
        
class Migration(migrations.Migration):
    dependencies = [
        ('menu_app', '0002_add_superuser'),
    ]

    operations = [
        migrations.RunPython(add_data),
    ]