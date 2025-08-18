import allure
from locators.checkout_locator import CheckoutLocator
from pages.checkout_page import CheckoutPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from utils.assertion_helpers import *
from utils.wait_helpers import *
from utils.allure_helpers import *
import pytest


@pytest.mark.checkout
# @pytest.mark.suite_smoke ("Test ringan untuk cek fungsi utama")
@pytest.mark.suite_regression
@allure.epic("Checkout Functionality")
@allure.feature("Checkout")
@allure.story("Melakukan Checkout dan Mengisi Informasi Pengiriman")
class TestCheckoutSauceDemo:
    @allure.title("Mengisi Informasi Pengiriman - SauceDemo")
    @allure.description("Melakukan pengisian informasi pengiriman")
    def test_fill_shipping_information(self, login_and_go_to_nextpage):
        attach_timestamp("Waktu Mulai Test Mengisi Informasi Pengiriman")

        page = login_and_go_to_nextpage
        inventory = InventoryPage(page)
        cart = CartPage(page)
        checkout = CheckoutPage(page)

        inventory.click_addtocart_button()
        inventory.click_shopping_cart_icon()
        assert_equals(cart.get_first_item("Sauce Labs Backpack").is_visible(), True)
        assert_url_ends_with(page, "/cart.html")
        
        cart.click_checkout_button()
        assert_url_ends_with(page, "/checkout-step-one.html")
        assert_has_text(checkout.get_checkout_your_information_text(), "Checkout: Your Information")    
        
        checkout.fill_first_name("John")
        checkout.fill_last_name("Doe")
        checkout.fill_zip_code("12345")

    @allure.title("Membatalkan Informasi Pengiriman - SauceDemo")
    @allure.description("Menghapus informasi pengiriman")
    def test_cancel_checkout_your_information(self, page):
        checkout = CheckoutPage(page)
        checkout.click_cancel_button()
        assert_url_ends_with(page, "/cart.html")

    @allure.title("Melanjutkan Informasi Pengiriman - SauceDemo")
    @allure.description("Melanjutkan pengisian informasi pengiriman")
    def test_continue_to_checkout_overview(self, page):
        checkout = CheckoutPage(page)
        cart = CartPage(page)
        cart.click_checkout_button()
        
        checkout.fill_first_name("John")
        checkout.fill_last_name("Doe")
        checkout.fill_zip_code("12345")
        
        checkout.click_continue_button()
        assert_url_ends_with(page, "/checkout-step-two.html")
        assert_has_text(checkout.get_checkout_overview_text(), "Checkout: Overview")

    @allure.title("Membatalkan Ringkasan Pembayaran - SauceDemo")
    @allure.description("Membatalkan informasi pembayaran")
    def test_cancel_checkout_overview(self, page):
        checkout = CheckoutPage(page)
        checkout.click_cancel_button()
        assert_url_ends_with(page, "/inventory.html")

    @allure.title("Menyelesaikan Checkout - SauceDemo")
    @allure.description("Menyelesaikan proses checkout")
    def test_finish_checkout(self, page):
        checkout = CheckoutPage(page)
        cart = CartPage(page)
        inventory = InventoryPage(page)

        inventory.click_shopping_cart_icon()
        cart.click_checkout_button()
        checkout.fill_first_name("John")
        checkout.fill_last_name("Doe")
        checkout.fill_zip_code("12345")
        checkout.click_continue_button()
        assert_url_ends_with(page, "/checkout-step-two.html")
        assert_equals(checkout.get_total_price_text(), "Total: $32.39")
        assert_equals(checkout.get_tax_text(), "Tax: $2.40")

        checkout.click_finish_button()
        assert_url_ends_with(page, "/checkout-complete.html")
        assert_has_text(checkout.get_checkout_finish_text(), "Checkout: Complete!")

    @allure.title("Kembali ke Produk - SauceDemo")
    @allure.description("Kembali ke halaman produk")
    def test_back_to_products(self, page):
        checkout = CheckoutPage(page)
        checkout.click_back_to_products_button()
        assert_url_ends_with(page, "/inventory.html")