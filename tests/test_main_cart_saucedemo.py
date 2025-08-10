import allure
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from utils.assertion_helpers import *
from utils.wait_helpers import *
from utils.allure_helpers import *
import pytest


@pytest.mark.cart
# @pytest.mark.suite_smoke ("Test ringan untuk cek fungsi utama")
@pytest.mark.suite_regression ("Full regression suite")
@allure.epic("Cart Functionality")
@allure.feature("Cart")
@allure.suite("Test Cart SauceDemo")
@allure.story("Menambahkan dan Menghapus Item dari Keranjang serta Melakukan Checkout")
class TestCartSauceDemo:
    @allure.title("Menambahkan Item ke Keranjang - SauceDemo")
    @allure.description("Melakukan penambahan item ke keranjang")
    def test_add_item_to_cart(self, login_and_go_to_nextpage):
        attach_timestamp("Waktu Mulai Test Menambahkan Item ke Keranjang")

        page = login_and_go_to_nextpage
        inventory = InventoryPage(page)
        cart = CartPage(page)
        inventory.click_addtocart_button()
        inventory.click_shopping_cart_icon()
        assert_equals(cart.get_first_item("Sauce Labs Backpack").is_visible(), True)
        assert_url_ends_with(page, "/cart.html")

    @allure.title("Menghapus Item dari Keranjang - SauceDemo")
    @allure.description("Melakukan penghapusan item dari keranjang")
    def test_remove_item_from_cart(self, page):
        attach_timestamp("Waktu Mulai Test Menghapus Item dari Keranjang")

        cart = CartPage(page)
        cart.remove_item("Sauce Labs Backpack")
        assert_equals(cart.get_first_item("Sauce Labs Backpack").is_visible(), False)
        assert_url_ends_with(page, "/cart.html")

    @allure.title("Melanjutkan Belanja - SauceDemo")
    @allure.description("Melakukan navigasi kembali ke halaman produk")
    def test_continue_shopping(self, page):
        attach_timestamp("Waktu Mulai Test Melanjutkan Belanja")

        cart = CartPage(page)
        cart.click_continue_button()
        assert_url_ends_with(page, "/inventory.html")

    @allure.title("Checkout - SauceDemo")
    @allure.description("Melakukan proses checkout")
    def test_checkout(self, page):
        attach_timestamp("Waktu Mulai Test Checkout")

        inventory = InventoryPage(page)
        cart = CartPage(page)
        
        inventory.click_addtocart_button()
        inventory.click_shopping_cart_icon()
        assert_url_ends_with(page, "/cart.html")
        
        cart.click_checkout_button()
        assert_url_ends_with(page, "/checkout-step-one.html")