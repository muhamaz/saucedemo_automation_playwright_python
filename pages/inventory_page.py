from locators.inventory_locator import InventoryLocator
from utils.allure_helpers import *
from utils.wait_helpers import *

class InventoryPage:
    def __init__(self, page):
        self.page = page
        self.step_counter = 1
    
    def click_addtocart_button(self):
        with log_step("Klik tombol add to cart"):
            wait_and_click(self.page.locator(InventoryLocator.addtocart_btn))
            self._capture("Klik Tombol Add to Cart")

    def click_remove_button(self):
        with log_step("Klik tombol remove"):
            wait_and_click(self.page.locator(InventoryLocator.remove_btn))
            self._capture("Klik Tombol Remove")

    def filter_product_by(self, label):
        with log_step(f"Melakukan filter product berdasarkan: {label}"):
            wait_and_select_option(self.page.locator(InventoryLocator.filter_dropdown), label)
            self._capture(f"Filter product by {label}")
    
    def get_price_first_product(self):
        with log_step("Mengambil harga produk pertama"):
            return self.page.locator(InventoryLocator.first_item_price)
        
    def get_name_first_product(self, name_product):
        with log_step("Mengambil nama produk pertama"):
            return self.page.locator(InventoryLocator.item_name_by_text(name_product))
        
    def click_shopping_cart_icon(self):
        with log_step("Klik ikon keranjang belanja"):
            wait_and_click(self.page.locator(InventoryLocator.shoppingcart_icon))
            self._capture("Klik Ikon Keranjang Belanja")

    # Menyimpan Screenshot
    def _capture(self, step_name, base_folder=None):
        save_and_attach_screenshot(self.page, step_name, base_folder)
        self.step_counter += 1