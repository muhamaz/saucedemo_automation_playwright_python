class CartLocator:
    continue_btn = "//button[@id='continue-shopping']"
    checkout_btn = "//button[@id='checkout']"
    
    @staticmethod
    def remove_item_btn(item_name):
        return f"//div[text()='{item_name}']//ancestor::div[@class='cart_item']//button"
    @staticmethod
    def cart_item_locator(item_name):
        return f"//div[text()='{item_name}']//ancestor::div[@class='cart_item']"