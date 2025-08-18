from locators.cart_locator import CartLocator
from utils.allure_helpers import *
from utils.wait_helpers import *

global_step_counter = 4

class CartPage:
    def __init__(self, page):
        self.page = page

    def click_continue_button(self):
        with log_step("Klik tombol continue"):
            wait_and_click(self.page.locator(CartLocator.continue_btn))
            self._capture("Klik Tombol Continue")
    
    def click_checkout_button(self):
        with log_step("Klik tombol checkout"):
            wait_and_click(self.page.locator(CartLocator.checkout_btn))
            self._capture("Klik Tombol Checkout")

    def get_first_item(self, item_name):
        with log_step("Mengambil item pertama"):
            return self.page.locator(CartLocator.cart_item_locator(item_name))
    
    def remove_item(self, item_name):
        with log_step(f"Remove item {item_name}"):
            wait_and_click(self.page.locator(CartLocator.remove_item_btn(item_name)))
            self._capture(f"Remove item {item_name}")

    # Menyimpan Screenshot
    def _capture(self, step_name, base_folder=None):
        global global_step_counter
        # Tambahkan step counter ke nama step
        step_name_with_counter = f"{global_step_counter:02d}_{step_name}"  # pakai 2 digit, misalnya 01_Klik_Tombol
        
        save_and_attach_screenshot(self.page, step_name_with_counter, base_folder)
        # attach_playwright_screenshot(self.page, step_name_with_counter)
        global_step_counter += 1