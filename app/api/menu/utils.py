
def loadMenuData(menu_db_object):
    from app.models.menu.menu_schema import MenuSchema

    menu_schema = MenuSchema()
    menu_data = menu_schema.dump(menu_db_object)
    
    return menu_data