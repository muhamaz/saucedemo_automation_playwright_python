from locators.checkout_locator import CheckoutLocator
from utils.allure_helpers import *
from utils.wait_helpers import *

global_step_counter = 4

class CheckoutPage:
    def __init__(self, page):
        self.page = page

    def fill_first_name(self, first_name):
        with log_step("Mengisi nama depan"):
            wait_and_fill(self.page.locator(CheckoutLocator.first_name_input), first_name)
            self._capture("Mengisi Nama Depan")

    def fill_last_name(self, last_name):
        with log_step("Mengisi nama belakang"):
            wait_and_fill(self.page.locator(CheckoutLocator.last_name_input), last_name)
            self._capture("Mengisi Nama Belakang")

    def fill_zip_code(self, zip_code):
        with log_step("Mengisi kode pos"):
            wait_and_fill(self.page.locator(CheckoutLocator.zip_code_input), zip_code)
            self._capture("Mengisi Kode Pos")

    def click_continue_button(self):
        with log_step("Klik tombol continue"):
            wait_and_click(self.page.locator(CheckoutLocator.continue_button))
            self._capture("Klik Tombol Continue")

    def click_cancel_button(self):
        with log_step("Klik tombol cancel"):
            wait_and_click(self.page.locator(CheckoutLocator.cancel_button))
            self._capture("Klik Tombol Cancel")

    def get_checkout_your_information_text(self):
        with log_step("Mengambil teks 'Checkout: Your Information'"):
            return self.page.locator(CheckoutLocator.checkout_your_information_text)

    def get_checkout_overview_text(self):
        with log_step("Mengambil teks 'Checkout: Overview'"):
            return self.page.locator(CheckoutLocator.checkout_overview_text)
    
    def get_total_price_text(self):
        with log_step("Mengambil teks 'Total Price'"):
            return self.page.locator(CheckoutLocator.total_price_text).inner_text()

    def get_tax_text(self):
        with log_step("Mengambil teks 'Tax'"):
            return self.page.locator(CheckoutLocator.tax_text).inner_text()

    def click_finish_button(self):
        with log_step("Klik tombol finish"):
            wait_and_click(self.page.locator(CheckoutLocator.finish_button))
            self._capture("Klik Tombol Finish")
    
    def get_checkout_finish_text(self):
        with log_step("Mengambil teks 'Checkout: Complete'"):
            return self.page.locator(CheckoutLocator.checkout_finish_text)
    
    def click_back_to_products_button(self):
        with log_step("Klik tombol back to products"):
            wait_and_click(self.page.locator(CheckoutLocator.back_to_products_button))
            self._capture("Klik Tombol Back to Products")

    # Menyimpan Screenshot
    def _capture(self, step_name, base_folder=None):
        global global_step_counter
        # Tambahkan step counter ke nama step
        step_name_with_counter = f"{global_step_counter:02d}_{step_name}"  # pakai 2 digit, misalnya 01_Klik_Tombol
        
        save_and_attach_screenshot(self.page, step_name_with_counter, base_folder)
        # attach_playwright_screenshot(self.page, step_name_with_counter)
        global_step_counter += 1