import os
import allure
import pytest
from pages.login_page import LoginPage
from utils.assertion_helpers import *
from utils.allure_helpers import *


@pytest.mark.login
# @pytest.mark.suite_smoke
@pytest.mark.suite_regression
@allure.epic("Autentikasi")
@allure.feature("Login")
@allure.suite("Test Login SauceDemo")
@allure.story("Login dengan kredensial valid dan tidak valid")
class TestLoginSauceDemo:
    @allure.title("Login Salah Password - SauceDemo")
    @allure.description("Melakukan login dengan username valid tapi password salah")
    def test_login_wrong_password(self, page):
        attach_timestamp("Waktu Mulai Test Login Salah Password")

        login = LoginPage(page)
        login.input_username(os.getenv("LOGIN_USERNAME"))
        login.input_password("wrong_password")
        login.click_login_button()

        assert_text_in_page(page, "Epic sadface: Username and password do not match any user in this service", "Pesan error login salah password")
        
    @allure.title("Login Salah Username - SauceDemo")
    @allure.description("Melakukan login dengan username salah tapi password valid")
    def test_login_wrong_username(self, page):
        attach_timestamp("Waktu Mulai Test Login Salah Username")

        login = LoginPage(page)
        login.input_username("wrong_username")
        login.input_password(os.getenv("LOGIN_PASSWORD"))
        login.click_login_button()

        assert_text_in_page(page, "Epic sadface: Username and password do not match any user in this service", "Pesan error login salah password")

    @allure.title("Login Username Kosong - SauceDemo")
    @allure.description("Melakukan login dengan username kosong dan password valid")
    def test_login_empty_username(self, page):
        attach_timestamp("Waktu Mulai Test Login Username Kosong")

        login = LoginPage(page)
        login.input_username("")
        login.input_password(os.getenv("LOGIN_PASSWORD"))
        login.click_login_button()

        assert_text_in_page(page, "Epic sadface: Username is required", "Pesan error login username kosong")

    @allure.title("Login Password Kosong - SauceDemo")
    @allure.description("Melakukan login dengan username valid dan password kosong ")
    def test_login_empty_password(self, page):
        attach_timestamp("Waktu Mulai Test Login Password Kosong")

        login = LoginPage(page)
        login.input_username(os.getenv("LOGIN_USERNAME"))
        login.input_password("")
        login.click_login_button()

        assert_text_in_page(page, "Epic sadface: Password is required", "Pesan error login password kosong")
        
    @allure.title("Login Username & Password Kosong - SauceDemo")
    @allure.description("Melakukan login dengan username kosong dan password kosong")
    def test_login_empty_username_and_password(self, page):
        attach_timestamp("Waktu Mulai Test Login Username & Password Kosong")

        login = LoginPage(page)
        login.input_username("")
        login.input_password("")
        login.click_login_button()

        assert_text_in_page(page, "Epic sadface: Username is required", "Pesan error login username & password kosong")
        
    @allure.title("Login Valid - SauceDemo")
    @allure.description("Melakukan login ke situs dengan username dan password dari .env")
    def test_login(self, page):
        attach_timestamp("Waktu Mulai Test Login Valid")

        login = LoginPage(page)
        login.input_username(os.getenv("LOGIN_USERNAME"))
        login.input_password(os.getenv("LOGIN_PASSWORD"))
        login.click_login_button()

        assert_url_ends_with(page, "/inventory.html")