import allure
from utils.allure_helpers import *


def assert_equals(actual, expected, message=""):
    """
    Assert bahwa `actual == expected`.
    Melampirkan hasil ke Allure, baik berhasil maupun gagal.
    """
    if actual != expected:
        _attach_assert_failure(f"{message}\nExpected: {expected}\nActual: {actual}")
        raise AssertionError(f"{message}\nExpected: {expected}\nActual: {actual}")
    _attach_assert_success(f"{message or 'Assertion passed'}\n{actual} == {expected}")


def assert_not_equals(actual, expected, message=""):
    """
    Assert bahwa `actual != expected`.
    """
    if actual == expected:
        _attach_assert_failure(f"{message}\nValue should not be: {actual}")
        raise AssertionError(f"{message}\nValue should not be: {actual}")
    _attach_assert_success(f"{message or 'Assertion passed'}\n{actual} != {expected}")


def assert_true(condition, message="Condition is not True"):
    """
    Assert bahwa kondisi adalah True.
    """
    if not condition:
        _attach_assert_failure(message)
        raise AssertionError(message)
    _attach_assert_success(message or "Condition is True")


def assert_false(condition, message="Condition is not False"):
    """
    Assert bahwa kondisi adalah False.
    """
    if condition:
        _attach_assert_failure(message)
        raise AssertionError(message)
    _attach_assert_success(message or "Condition is False")


def assert_in(member, container, message=""):
    """
    Assert bahwa `member` ada dalam `container`.
    """
    if member not in container:
        msg = f"{message}\n'{member}' not found in container"
        _attach_assert_failure(msg)
        raise AssertionError(msg)
    _attach_assert_success(f"{message or 'Assertion passed'}\n'{member}' found in container")


def assert_text_in_page(page, text, message="Text not found in page"):
    """
    Assert bahwa teks muncul di konten halaman.
    """
    content = page.content()
    if text not in content:
        allure.attach(content, name="Page HTML", attachment_type=allure.attachment_type.HTML)
        _attach_assert_failure(f'{message}\nExpected text: "{text}"')
        raise AssertionError(f'{message}\nExpected text: "{text}"')
    _attach_assert_success(f'Text "{text}" ditemukan di halaman')

def _attach_assert_success(message: str):
    allure.attach(
        message,
        name="✅ Assertion Passed",
        attachment_type=allure.attachment_type.TEXT
    )


def _attach_assert_failure(message: str):
    allure.attach(
        message,
        name="❌ Assertion Failed",
        attachment_type=allure.attachment_type.TEXT
    )



def assert_url_ends_with(page, expected_suffix: str):
    """
    Assert bahwa URL saat ini di browser berakhir dengan string tertentu.
    """
    with log_step(f"Assertion: URL berakhir dengan '{expected_suffix}'"):
        actual_url = page.url
        assert actual_url.endswith(expected_suffix), (
            f"Expected URL to end with '{expected_suffix}', but got '{actual_url}'"
        )
