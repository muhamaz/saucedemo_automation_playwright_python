import shutil
from dotenv import load_dotenv
import os
import pytest
from playwright.sync_api import sync_playwright
import allure

load_dotenv()

@pytest.fixture(scope="session")
def browser():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        yield browser
        browser.close()

@pytest.fixture(scope="function")
def page(browser):
    width = int(os.getenv("VIEWPORT_WIDTH", 1920))
    height = int(os.getenv("VIEWPORT_HEIGHT", 1080))

    context = browser.new_context(
        viewport={"width": width, "height": height},
        device_scale_factor=1
    )
    
    context = browser.new_context()
    page = context.new_page()
    page.goto(os.getenv("MAIN_URL"))
    yield page
    context.close()
    
# Delete file .pytest_cache dan __pycache__ 
def delete_dir(path):
    if os.path.exists(path):
        shutil.rmtree(path)
        print(f"[INFO] Deleted: {path}")
        
def create_dir_if_not_exists(path):
    if not os.path.exists(path):
        os.makedirs(path)
        print(f"[INFO] Created: {path}")

@pytest.hookimpl(tryfirst=True)
def pytest_sessionstart(session):
    # Hapus folder .pytest_cache
    delete_dir(".pytest_cache")
    delete_dir("allure-results")
    
    # Buat ulang folder allure-results agar Allure tidak error
    create_dir_if_not_exists("allure-results")
    
    # Hapus semua folder __pycache__ dalam proyek
    for root, dirs, _ in os.walk("."):
        for d in dirs:
            if d == "__pycache__":
                delete_dir(os.path.join(root, d))

# # Screenshot saat test gagal
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