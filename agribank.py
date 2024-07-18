from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import threading
from webdriver_manager.chrome import ChromeDriverManager


# config
service = Service(ChromeDriverManager().install())
chrome_options = [webdriver.ChromeOptions()]
drivers = []

for options in chrome_options:
    options.page_load_strategy = (
        "normal"  # Đảm bảo không bỏ qua bất kỳ bước tải trang nào
    )
    options.add_experimental_option("detach", True)
    options.add_argument("--window-size=450,̀500")
    driver = webdriver.Chrome(service=service, options=options)
    drivers.append(driver)


def automate_user(driver):
    try:
        driver.get("https://bookingonline.agribank.com.vn/muavangSJCtructuyen")
        # wait = WebDriverWait(driver, 5)

        # name_input = wait.until(EC.presence_of_element_located((By.ID, "id_cccd")))
        diemGiaoDich = driver.find_element(By.XPATH, r"//input[@id='input-25']")
        diemGiaoDich.click()

        login_button = driver.find_element(
            By.CSS_SELECTOR,
            "body > div:nth-child(2) > div:nth-child(3) > div:nth-child(1) > div:nth-child(1) > div:nth-child(3) > div:nth-child(1) > div:nth-child(1) > div:nth-child(6) > div:nth-child(1) > div:nth-child(1)",
        )
        driver.execute_script("arguments[0].click();", login_button)
        driver.find_element(By.XPATH, r"//button[contains(text(),'Tiếp tục')]").click()

        # handle_booking(driver, data)

    except Exception as e:
        print(f"Starting")


threading.Thread(
    target=automate_user,
    args=(drivers[0],),
).start()
