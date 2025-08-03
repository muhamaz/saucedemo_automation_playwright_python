import allure
import json
from datetime import datetime
import os


def log_step(step_description: str):
    """
    Gunakan untuk mencatat langkah dinamis di Allure Report.
    Contoh:
        with log_step("Klik tombol login"):
            page.click("#login")
    """
    return allure.step(step_description)


def log_info(message: str, name: str = "Info"):
    """
    Attach teks biasa ke Allure Report sebagai informasi tambahan.
    """
    allure.attach(
        body=message,
        name=name,
        attachment_type=allure.attachment_type.TEXT
    )

    
def attach_playwright_screenshot(page, step_name="Screenshot", full_page=True):
    """
    Ambil screenshot dari page dan langsung attach ke Allure (tanpa simpan lokal).
    """
    screenshot = page.screenshot(full_page=full_page)
    allure.attach(
        screenshot,
        name=step_name,
        attachment_type=allure.attachment_type.PNG
    )

def save_and_attach_screenshot(page, step_name, base_folder):
    """
    Simpan screenshot Playwright ke folder lokal dan attach ke Allure.
    """
    os.makedirs(base_folder, exist_ok=True)
    timestamp = datetime.now().strftime("%Y%m%d")
    filename = f"{step_name.replace(' ', '_')}_{timestamp}.png"
    path = os.path.join(base_folder, filename)

    page.screenshot(path=path, full_page=True)

    # Attach screenshot to Allure
    with open(path, "rb") as img:
        allure.attach(
            img.read(),
            name=step_name,
            attachment_type=allure.attachment_type.PNG
        )

    return path


def attach_html(page, name="HTML Snapshot"):
    """
    Ambil HTML saat ini dari page dan attach ke Allure.
    """
    html = page.content()
    allure.attach(
        html,
        name=name,
        attachment_type=allure.attachment_type.HTML
    )


def attach_json(data: dict, name="JSON Data"):
    """
    Attach data JSON ke Allure Report.
    """
    allure.attach(
        json.dumps(data, indent=2),
        name=name,
        attachment_type=allure.attachment_type.JSON
    )


def attach_file(file_path: str, name="File Attachment"):
    """
    Attach file eksternal (log, txt, dll) ke Allure.
    """
    with open(file_path, "rb") as f:
        allure.attach(
            f.read(),
            name=name,
            attachment_type=allure.attachment_type.TEXT
        )


def attach_timestamp(name="Timestamp"):
    """
    Lampirkan timestamp (waktu saat ini) ke report.
    """
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_info(now, name=name)