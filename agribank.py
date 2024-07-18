from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import threading
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium_stealth import stealth


# config
user_data_dir = r"C:\Users\Van Nghia\AppData\Local\CocCoc\Browser\User Data"
coccoc_path = r"C:\Program Files\CocCoc\Browser\Application\browser.exe"  # Cập nhật đường dẫn này nếu cần thiết

service = Service(ChromeDriverManager().install())
chrome_options = [webdriver.ChromeOptions()]
profile_dirs = "Profile 9"
drivers = []

for options in chrome_options:
    options.binary_location = coccoc_path
    # options.add_argument(
    #     "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"
    # )
    options.add_experimental_option("detach", True)

    driver = webdriver.Chrome(service=service, options=options)
    drivers.append(driver)


def automate_user(driver):
    wait = WebDriverWait(driver, 3)
    try:
        driver.get("https://www.agribank.com.vn/vn/ca-nhan")

        wait.until(
            EC.presence_of_element_located(
                (
                    By.XPATH,
                    '//*[@id="layoutContainers"]/div[1]/div[2]/div/div/section[3]/div/div[1]/div[1]/div[3]/div[1]/a/img',
                )
            )
        ).click()

        wait.until(
            EC.presence_of_element_located((By.XPATH, r"//input[@id='input-25']"))
        ).click()

        wait.until(
            EC.presence_of_element_located(
                (
                    By.CSS_SELECTOR,
                    r"body > div:nth-child(2) > div:nth-child(3) > div:nth-child(1) > div:nth-child(1) > div:nth-child(3) > div:nth-child(1) > div:nth-child(1) > div:nth-child(6) > div:nth-child(1) > div:nth-child(1)",
                )
            )
        ).click()

        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, r"//button[contains(text(),'Tiếp tục')]")
            )
        ).click()
        wait.until(
            EC.presence_of_element_located((By.XPATH, r"//input[@id='input-114']"))
        ).click()

        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, r"//li[normalize-space()='2002']")
            )
        ).click()

        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, r"//div[normalize-space()='Tháng 4']")
            )
        ).click()

        wait.until(
            EC.presence_of_element_located((By.XPATH, r"//div[normalize-space()='23']"))
        ).click()

        # handle_booking(driver, data)

    except Exception as e:
        print(f"Starting")


automate_user(driver=drivers[0])
# threading.Thread(
#     target=automate_user,
#     args=(drivers[0],),
# ).start()
