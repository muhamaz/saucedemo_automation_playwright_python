from playwright.sync_api import expect
from utils.allure_helpers import *
from utils.wait_helpers import *



def scroll_into_view(locator, timeout=5000):
    """Scroll sampai elemen tertentu terlihat di viewport"""
    with log_step(f"Scroll ke elemen: {locator}"):
        wait_until_attached(locator, timeout)
        locator.scroll_into_view_if_needed(timeout=timeout)
        wait_until_visible(locator, timeout)


def scroll_and_click(locator, timeout=5000):
    """Scroll ke elemen lalu klik"""
    with log_step(f"Scroll dan klik elemen: {locator}"):
        scroll_into_view(locator, timeout)
        wait_until_enabled(locator, timeout)
        locator.click()


def scroll_and_fill(locator, text, timeout=5000):
    """Scroll ke elemen lalu isi teks"""
    with log_step(f"Scroll dan isi teks ke elemen: {locator} dengan teks: {text}"):
        scroll_into_view(locator, timeout)
        wait_until_enabled(locator, timeout)
        locator.click()
        locator.press("Control+A")
        locator.press("Delete")
        locator.fill(text)


def scroll_and_select_option(locator, value: str, timeout=5000):
    """Scroll ke dropdown lalu pilih option berdasarkan value"""
    with log_step(f"Scroll dan pilih option dropdown: {value} pada elemen {locator}"):
        scroll_into_view(locator, timeout)
        wait_until_enabled(locator, timeout)
        locator.select_option(value=value)


def scroll_and_check(locator, timeout=5000):
    """Scroll ke checkbox lalu centang jika belum dicentang"""
    with log_step(f"Scroll dan centang checkbox: {locator}"):
        scroll_into_view(locator, timeout)
        wait_until_enabled(locator, timeout)
        if not locator.is_checked():
            locator.check()


def scroll_and_uncheck(locator, timeout=5000):
    """Scroll ke checkbox lalu hapus centang jika sudah dicentang"""
    with log_step(f"Scroll dan hapus centang checkbox: {locator}"):
        scroll_into_view(locator, timeout)
        wait_until_enabled(locator, timeout)
        if locator.is_checked():
            locator.uncheck()
