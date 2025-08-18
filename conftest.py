import os
import shutil
import allure
import pytest
from dotenv import load_dotenv
from playwright.sync_api import sync_playwright

from pages.login_page import LoginPage
from utils.wait_helpers import *

# =====================================================
#  Load Environment Variables
# =====================================================
load_dotenv()


# =====================================================
#  Fixtures
# =====================================================

@pytest.fixture(scope="session")
def browser():
    """Fixture untuk inisialisasi browser sekali per session."""
    with sync_playwright() as p:
        browser = p.chromium.launch(
            headless=False
            # args=["--start-maximized"] # Uncomment if you want to start maximized
        )
        yield browser
        browser.close()

@pytest.fixture(scope="class")
def page(browser):
    """Fixture untuk setup page dan otomatis logout saat teardown."""
    width = int(os.getenv("VIEWPORT_WIDTH", 1920))
    height = int(os.getenv("VIEWPORT_HEIGHT", 1080))
    
    context = browser.new_context(
        viewport={"width": width, "height": height},
        device_scale_factor=1
        # no_viewport=True  # Disable viewport to use full window size
    )
    page = context.new_page()
    page.goto(os.getenv("MAIN_URL"))

    yield page

    # Teardown: logout sebelum close browser
    try:
        burger_btn = page.locator("//div[@class='bm-burger-button']")
        logout_btn = page.locator("//a[@id='logout_sidebar_link']")
        if burger_btn.is_visible():
            wait_and_click(burger_btn)
            wait_and_click(logout_btn)
            wait_until_page_loaded(page)
            print("✅ Berhasil logout.")
    except Exception as e:
        print(f"⚠️ Gagal logout: {e}")
        os.makedirs("screenshots", exist_ok=True)
        page.screenshot(path="screenshots/logout_error.png")

    context.close()


@pytest.fixture(scope="class")
def login_and_go_to_nextpage(page):
    """Fixture untuk login ke aplikasi sebelum menjalankan test."""
    login = LoginPage(page)
    login.input_username(os.getenv("LOGIN_USERNAME"))
    login.input_password(os.getenv("LOGIN_PASSWORD"))
    login.click_login_button()
    yield page

# =====================================================
#  Helper Functions
# =====================================================

def delete_dir(path):
    """Hapus folder jika ada."""
    if os.path.exists(path):
        shutil.rmtree(path)
        print(f"[INFO] Deleted: {path}")

def create_dir_if_not_exists(path):
    """Buat folder jika belum ada."""
    if not os.path.exists(path):
        os.makedirs(path)
        print(f"[INFO] Created: {path}")

# =====================================================
#  Pytest Hooks
# =====================================================

@pytest.hookimpl(tryfirst=True)
def pytest_configure(config):
    """Konfigurasi awal pytest: siapkan folder screenshot & allure-results per test file."""
    test_paths = config.args
    for path in test_paths:
        filename = os.path.basename(path)
        test_name = os.path.splitext(filename)[0]

        # Buat folder screenshot
        screenshot_path = os.getenv("SCREENSHOT_SUBFOLDER") or os.path.join("screenshots", test_name)
        delete_dir(screenshot_path)
        create_dir_if_not_exists(screenshot_path)
        os.environ["SCREENSHOT_SUBFOLDER"] = screenshot_path

        # Buat folder allure results
        allure_result_path = os.path.join("allure-results", test_name)
        delete_dir(allure_result_path)
        create_dir_if_not_exists(allure_result_path)
        os.environ["ALLURE_RESULTS_DIR"] = allure_result_path

        # # ⚠️ Jika user belum tentukan --alluredir, override nilainya
        # if not config.option.alluredir:
        #     config.option.alluredir = allure_result_path
        #     print(f"📦 [DEBUG] Allure dir set to: {allure_result_path}")

# # Kosongkan jika tidak dipakai
# def pytest_addoption(parser):
#     pass

# Mapping untuk suite
SUITE_MAPPING = {
    "suite_regression": "Regression Tests",
}

@pytest.hookimpl(tryfirst=True)
def pytest_runtest_setup(item):
    for marker, suite_name in SUITE_MAPPING.items():
        if item.get_closest_marker(marker):
            allure.dynamic.parent_suite("Saucedemo Automation")
            allure.dynamic.suite(suite_name)
            break


@pytest.hookimpl(tryfirst=True)
def pytest_sessionstart(session):
    """Bersihkan cache & __pycache__ sebelum test dimulai."""
    delete_dir(".pytest_cache")
    for root, dirs, _ in os.walk("."):
        for d in dirs:
            if d == "__pycache__":
                delete_dir(os.path.join(root, d))


# =====================================================
#  (Optional) Screenshot on Failure
# =====================================================
# @pytest.hookimpl(tryfirst=True, hookwrapper=True)
# def pytest_runtest_makereport(item):
#     os.makedirs("screenshots", exist_ok=True)  # buat folder kalau belum ada
#     outcome = yield
#     report = outcome.get_result()

#     if report.when == "call" and report.failed:
#         page = item.funcargs.get("page")
#         if page:
#             screenshot_path = "screenshots/failed_screenshot.png"
#             page.screenshot(path=screenshot_path, full_page=True)
#             allure.attach.file(screenshot_path, name="Screenshot on failure", attachment_type=allure.attachment_type.PNG)