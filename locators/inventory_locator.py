class InventoryLocator :
    addtocart_btn = '//button[@id="add-to-cart-sauce-labs-backpack"]'
    shoppingcart_icon = '//a[@class="shopping_cart_link"]'
    filter_dropdown = "(//select[@class='product_sort_container'])"
    remove_btn = '//button[@id="remove-sauce-labs-backpack"]'
    first_item_price = "(//div[@class='inventory_item'])[1]//div[@class='inventory_item_price']"
    
    @staticmethod
    def item_name_by_text(text: str) -> str:
        return f"//div[normalize-space()='{text}'][1]"