import allure
from pages.inventory_page import InventoryPage
from utils.assertion_helpers import *
from utils.wait_helpers import *
from utils.allure_helpers import *
import pytest


@pytest.mark.login
# @pytest.mark.suite_smoke ("Test ringan untuk cek fungsi utama")
@pytest.mark.suite_regression ("Full regression suite")
@allure.epic("Inventory Functionality")
@allure.feature("Inventory")
@allure.suite("Test Inventory SauceDemo")
@allure.story("Menambahkan dan Menghapus Item dari Keranjang serta Melakukan Filter")
class TestInventorySauceDemo:
    @allure.title("Menambahkan Item ke Keranjang - SauceDemo")
    @allure.description("Melakukan penambahan item ke keranjang")
    def test_add_item_to_cart(self, login_and_go_to_nextpage):
        attach_timestamp("Waktu Mulai Test Menambahkan Item ke Keranjang")

        page = login_and_go_to_nextpage
        inventory = InventoryPage(page)
        inventory.click_addtocart_button()
        assert_text_in_page(page, "1", "Jumlah item di keranjang setelah penambahan")
        assert_url_ends_with(page, "/inventory.html")

    @allure.title("Menghapus Item dari Keranjang - SauceDemo")
    @allure.description("Melakukan penghapusan item dari keranjang")
    def test_remove_item_from_cart(self, page):
        attach_timestamp("Waktu Mulai Test Menghapus Item dari Keranjang")

        inventory = InventoryPage(page)
        inventory.click_remove_button()
        assert_text_in_page(page, "0", "Jumlah item di keranjang setelah penghapusan")
        assert_url_ends_with(page, "/inventory.html")
    
    @allure.title("Memfilter Item di Inventory A to Z - SauceDemo")
    @allure.description("Melakukan filter item A to Z di inventory")
    def test_filter_inventory_items_by_Name_A_to_Z(self, page):
        attach_timestamp("Waktu Mulai Test Memfilter Item di Inventory")

        inventory = InventoryPage(page)
        inventory.filter_product_by("Name (A to Z)")
        assert_has_text(inventory.get_name_first_product("Sauce Labs Backpack"), "Sauce Labs Backpack")
        assert_url_ends_with(page, "/inventory.html")

    @allure.title("Memfilter Item di Inventory Z to A - SauceDemo")
    @allure.description("Melakukan filter item Z to A di inventory")
    def test_filter_inventory_items_by_Name_Z_to_A(self, page):
        attach_timestamp("Waktu Mulai Test Memfilter Item di Inventory")

        inventory = InventoryPage(page)
        inventory.filter_product_by("Name (Z to A)")
        assert_has_text(inventory.get_name_first_product("Test.allTheThings() T-Shirt (Red)"), "Test.allTheThings() T-Shirt (Red)")
        assert_url_ends_with(page, "/inventory.html")

    @allure.title("Memfilter Item di Inventory Price (Low to High) - SauceDemo")
    @allure.description("Melakukan filter item Price (Low to High) di inventory")
    def test_filter_inventory_items_by_Price_Low_to_High(self, page):
        attach_timestamp("Waktu Mulai Test Memfilter Item di Inventory")

        inventory = InventoryPage(page)
        inventory.filter_product_by("Price (low to high)")
        expected_text = inventory.get_price_first_product()
        assert_has_text(expected_text, "$7.99")
        assert_url_ends_with(page, "/inventory.html")

    @allure.title("Memfilter Item di Inventory Price (High to Low) - SauceDemo")
    @allure.description("Melakukan filter item Price (High to Low) di inventory")
    def test_filter_inventory_items_by_Price_High_to_Low(self, page):
        attach_timestamp("Waktu Mulai Test Memfilter Item di Inventory")

        inventory = InventoryPage(page)
        inventory.filter_product_by("Price (high to low)")
        expected_text = inventory.get_price_first_product()
        assert_has_text(expected_text, "$49.99")
        assert_url_ends_with(page, "/inventory.html")
    
    @allure.title("Menambahkan Item ke Keranjang dan Pergi ke Keranjang - SauceDemo")
    @allure.description("Melakukan penambahan item ke keranjang dan pergi ke halaman keranjang")
    def test_add_item_to_cart_and_go_to_cart(self, page):
        attach_timestamp("Waktu Mulai Test Menambahkan Item ke Keranjang dan Pergi ke Keranjang")

        inventory = InventoryPage(page)
        inventory.click_addtocart_button()
        inventory.click_shopping_cart_icon()
        assert_url_ends_with(page, "/cart.html")