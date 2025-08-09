from locators.login_locator import LoginLocator
from utils.allure_helpers import *
from utils.wait_helpers import *

global_step_counter = 1

class LoginPage:  
    def __init__(self, page):
        self.page = page

    def input_username(self, username):
        with log_step(f"Mengisi username: {username}"):
            wait_and_fill(self.page.locator(LoginLocator.username_field), username)
            self._capture(f"Isi Username {username}")

    def input_password(self, password):
        with log_step("Mengisi password: ********"):
            wait_and_fill(self.page.locator(LoginLocator.password_field), password)
            self._capture(f"Isi Password {password}")

    def click_login_button(self):
        with log_step("Klik tombol login"):
            wait_and_click(self.page.locator(LoginLocator.login_button))
            self._capture("Klik Tombol Login")

    # Menyimpan Screenshot
    def _capture(self, step_name, base_folder=None):
        global global_step_counter
        # Tambahkan step counter ke nama step
        step_name_with_counter = f"{global_step_counter:02d}_{step_name}"  # pakai 2 digit, misalnya 01_Klik_Tombol

        save_and_attach_screenshot(self.page, step_name_with_counter, base_folder)
        global_step_counter += 1