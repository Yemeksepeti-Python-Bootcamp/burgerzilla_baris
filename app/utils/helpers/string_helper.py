class StringHelper:
    """
    This class is used to store all the string 
    constants used in the application.
    """
    

    # Error messages
    INTERNAL_SERVER_ERROR = "Internal Server Error"
    SERVER_ERROR = "Server Error"

    # USER
    USER_NOT_FOUND = "User not found"
    USERNAME_ALREADY_EXISTS = "Username already exists"
    PASSWORD_NOT_ACCESSIBLE = "Password is not a readable attribute"
    SUCCESS_LOGIN = "Success Login!"
    SUCCESS_REGISTER = "Success Register!"
    INVALID_PASSWORD_OR_EMAIL = "Invalid password or email"
    EMAIL_ALREADY_EXISTS = "Email already exists"

    # ORDERS
    SUCCESS_ORDER_CREATED = "Order created"
    SUCCESS_ORDER_UPDATED = "Order updated"
    SUCCESS_ORDER_DELETED = "Order deleted"
    SUCCESS_ORDERS_FOUND = "Orders found"
    SUCCESS_ORDER_CANCEL = "Order canceled"
    ORDER_ALREADY_DELIVERED_OR_CANCELED = "Order already delivered or canceled"
    ORDER_STATUS_UPDATED = "Order status updated"
    FAIL_ORDER_FOUND = "Orders not found"
    FAIL_ORDER_CREATED = "Order not created"
    FAIL_ORDER_UPDATED = "Order not updated"
    FAIL_ORDER_DELETED = "Order not deleted"
    FAIL_ACTIVE_ORDERS = "No active orders"
    THERE_IS_NO_ORDER = "There is no order"

    # RESTAURANTS
    YOUR_ARE_NOT_OWNER_RESTAURANT = "You are not owner of this restaurant"
    YOU_ARE_NOT_RESTAURANT_USER = "You are not restaurant user"
    RESTAURANT_NAME_ALREADY_EXISTS = "Restaurant name already exists"
    FAIL_RESTAURANT_FOUND = "Restaurant not found"
    SUCCES_RESTAURANT_FOUND = "Restaurant found"
    SUCCES_MENU_FOUND = "Menu found"

    # PRODUCTS
    SUCCESS_PRODUCT_CREATED = "Product created"
    SUCCESS_PRODUCT_UPDATED = "Product updated"
    SUCCESS_PRODUCT_DELETED = "Product deleted"
    SUCCESS_PRODUCTS_FOUND = "Products found"
    FAIL_PRODUCT_CREATED = "Product not created"
    FAIL_PRODUCT_UPDATED = "Product not updated"
    FAIL_PRODUCT_DELETED = "Product not deleted"
    FAIL_PRODUCTS_FOUND = "Product not found"

    # MENU
    SUCCESS_MENU_CREATED = "Menu created"
    SUCCESS_MENU_UPDATED = "Menu updated"
    SUCCESS_MENU_DELETED = "Menu Menu and all belonging products deleted"
    SUCCESS_MENUS_FOUND = "Menus found"
    FAIL_MENU_CREATED = "Menu not created"
    FAIL_MENU_UPDATED = "Menu not updated"
    FAIL_MENU_DELETED = "Menu not deleted"
    FAIL_MENU_FOUND = "Menus not found"
    MENU_ALREADY_EXISTS = "Menu already exists"