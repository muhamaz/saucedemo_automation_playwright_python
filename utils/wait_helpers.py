from playwright.sync_api import expect
from utils.allure_helpers import log_step

def wait_until_visible(locator, timeout=5000):
    """Tunggu hingga elemen terlihat"""
    with log_step(f"Menunggu elemen terlihat: {locator}"):
        expect(locator).to_be_visible(timeout=timeout)

def wait_until_hidden(locator, timeout=5000):
    """Tunggu hingga elemen tersembunyi"""
    with log_step(f"Menunggu elemen tersembunyi: {locator}"):
        expect(locator).to_be_hidden(timeout=timeout)

def wait_until_attached(locator, timeout=5000):
    """Tunggu hingga elemen muncul di DOM"""
    with log_step(f"Menunggu elemen muncul di DOM: {locator}"):
        expect(locator).to_be_attached(timeout=timeout)

def wait_until_detached(locator, timeout=5000):
    """Tunggu hingga elemen hilang dari DOM"""
    with log_step(f"Menunggu elemen hilang dari DOM: {locator}"):
        expect(locator).to_be_detached(timeout=timeout)

def wait_until_enabled(locator, timeout=5000):
    """Tunggu sampai elemen bisa diinteraksi (enabled)"""
    with log_step(f"Menunggu elemen aktif (enabled): {locator}"):
        expect(locator).to_be_enabled(timeout=timeout)

def wait_until_disabled(locator, timeout=5000):
    """Tunggu sampai elemen tidak aktif (disabled)"""
    with log_step(f"Menunggu elemen tidak aktif (disabled): {locator}"):
        expect(locator).not_to_be_enabled(timeout=timeout)

def wait_and_click(locator, timeout=5000):
    """Tunggu sampai elemen terlihat dan enabled lalu klik"""
    with log_step(f"Klik setelah tunggu: {locator}"):
        wait_until_visible(locator, timeout)
        wait_until_enabled(locator, timeout)
        locator.click()

def wait_and_fill(locator, text, timeout=5000):
    """Tunggu sampai elemen terlihat dan enabled lalu isi teks"""
    with log_step(f"Isi field setelah tunggu: {locator} dengan teks: {text}"):
        wait_until_visible(locator, timeout)
        wait_until_enabled(locator, timeout)
        locator.fill(text)

def wait_and_upload_file(locator, file_path, timeout=5000):
    with log_step(f"Tunggu dan upload file: {file_path}"):
        wait_until_visible(locator, timeout)
        locator.set_input_files(file_path)

def wait_and_select_option(locator, value: str, timeout=5000):
    """Tunggu dropdown terlihat dan aktif lalu pilih option berdasarkan value"""
    with log_step(f"Pilih option dropdown: {value}"):
        wait_until_visible(locator, timeout)
        wait_until_enabled(locator, timeout)
        locator.select_option(value=value)

def wait_and_check(locator, timeout=5000):
    """Tunggu checkbox terlihat dan aktif lalu centang jika belum"""
    with log_step(f"Centang checkbox: {locator}"):
        wait_until_visible(locator, timeout)
        wait_until_enabled(locator, timeout)
        if not locator.is_checked():
            locator.check()

def wait_and_uncheck(locator, timeout=5000):
    """Tunggu checkbox terlihat dan aktif lalu hapus centang jika dicentang"""
    with log_step(f"Hapus centang checkbox: {locator}"):
        wait_until_visible(locator, timeout)
        wait_until_enabled(locator, timeout)
        if locator.is_checked():
            locator.uncheck()

def assert_visible(locator, timeout=5000):
    """Assertion + wait bahwa elemen terlihat"""
    with log_step(f"Assertion: elemen terlihat - {locator}"):
        expect(locator).to_be_visible(timeout=timeout)

def assert_has_text(locator, expected_text, timeout=5000):
    """Assertion + wait bahwa elemen mengandung teks tertentu"""
    with log_step(f"Assertion: elemen mengandung teks - {locator}"):
        expect(locator).to_have_text(expected_text, timeout=timeout)

def wait_until_page_loaded(page, state="load", timeout=10000):
    """Tunggu halaman selesai dimuat (load, domcontentloaded, networkidle)"""
    with log_step("Tunggu halaman selesai dimuat"):
        page.wait_for_load_state(state=state, timeout=timeout)

def wait_until_url_contains(page, partial_url, timeout=5000):
    """Tunggu sampai URL mengandung string tertentu"""
    with log_step(f"Tunggu URL mengandung string: {partial_url}"):
        for _ in range(int(timeout / 100)):
            if partial_url in page.url:
                return
            page.wait_for_timeout(100)
        raise TimeoutError(f"URL '{partial_url}' not found in time.")

def wait_until_url_equals(page, expected_url, timeout=5000):
    """Tunggu sampai URL sama persis dengan yang diharapkan"""
    with log_step(f"Tunggu URL sama persis dengan: {expected_url}"):
        for _ in range(int(timeout / 100)):
            if page.url == expected_url:
                return
            page.wait_for_timeout(100)
        raise TimeoutError(f"URL did not match expected: {expected_url}")

def wait_fixed_timeout(page, milliseconds):
    """Tunggu dengan delay paksa (tidak disarankan sering)"""
    with log_step(f"Tunggu delay paksa: {milliseconds} ms"):
        page.wait_for_timeout(milliseconds)
