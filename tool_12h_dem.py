from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import threading
from webdriver_manager.chrome import ChromeDriverManager
import json
import sys
import io
import gc
from datetime import datetime


# đọc file
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")
with open("dulieu.txt", "r", encoding="utf-8") as file:
    data = file.read()
data_list = json.loads(data)
print(len(data_list))


# config
service = Service(ChromeDriverManager().install())
chrome_options = [webdriver.ChromeOptions() for _ in range(len(data_list))]
drivers = []

# extension config
# extension_path1 = r"Free-VPN-for-Chrome-by-1clickVPN-Chrome-Web-Store.crx"
extension_path2 = r"I-m-not-robot-captcha-clicker-Chrome-Web-Store.crx"
extension_path3 = r"rektCaptcha-reCaptcha-Solver-Chrome-Web-Store.crx"

for options in chrome_options:
    options.page_load_strategy = "normal"
    # options.add_argument("--disable-popup-blocking")
    # options.add_extension(extension_path1)
    # options.add_extension(extension_path2)
    options.add_extension(extension_path3)
    options.add_argument("--disable-infobars")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-gpu")
    options.add_experimental_option("detach", True)
    options.add_argument("--window-size=350,450")
    driver = webdriver.Chrome(service=service, options=options)
    drivers.append(driver)


def loop_click(driver, data):
    wait = WebDriverWait(driver, 5)

    try:
        while True:
            current_time = datetime.now().strftime("%H:%M:%S")
            end_time = "00:02:00"
            # Check if captcha has timed out and refresh
            # if elapsed_time > refresh_threshold:
            #     driver.refresh()
            #     time.sleep(1)
            #     handle_booking(driver, data)
            # break
            if current_time == "00:00:00":
                break
            elif current_time > "00:00:00" and current_time < end_time:
                break
            if current_time == "11:59:00":
                driver.refresh()
                time.sleep(1)
                handle_booking(driver, data)
                break
            # time.sleep(0.00001)
        submit_button = WebDriverWait(driver, 3).until(
            EC.visibility_of_element_located((By.ID, "register_form_submit"))
        )
        submit_button.click()
        confirm_button = wait.until(
            EC.presence_of_element_located(
                (
                    By.CSS_SELECTOR,
                    "#kt_app_body > div.swal2-container.swal2-center.swal2-backdrop-show > div > div.swal2-actions > button.swal2-confirm.btn.btn-primary",
                )
            )
        )
        driver.execute_script("arguments[0].click();", confirm_button)
        handle_booking(driver, data)

    except Exception as e:
        print("error click")
        driver.refresh()
        handle_booking(driver, data)


def handle_booking(driver, data):
    try:
        wait = WebDriverWait(driver, 15)

        # button chọn vùng
        religon_point = wait.until(
            EC.presence_of_element_located(
                (By.XPATH, '//*[@id="register_form"]/div[1]/div[1]/span/span[1]')
            )
        )
        religon_point.click()
        time.sleep(0.1)
        # button chọn vùng con
        choose_religon = wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "/html/body/span/span/span[2]/ul/li")
            )
        )
        choose_religon.click()
        time.sleep(0.1)
        # button chọn điểm giao dịch
        transaction_point = wait.until(
            EC.presence_of_element_located(
                (By.XPATH, '//*[@id="register_form"]/div[1]/div[2]/span/span[1]')
            )
        )
        transaction_point.click()
        time.sleep(0.1)

        # chọn điểm giao dịch option
        if data["address"].lower() == "gò vấp":
            choose_trans = wait.until(
                EC.presence_of_element_located(
                    (By.XPATH, "/html/body/span/span/span[2]/ul/li[2]")
                )
            )
            choose_trans.click()
        elif data["address"].lower() == "trụ sở":
            choose_trans = wait.until(
                EC.presence_of_element_located(
                    (By.XPATH, "/html/body/span/span/span[2]/ul/li[1]")
                )
            )
            choose_trans.click()
        else:
            choose_trans = wait.until(
                EC.presence_of_element_located(
                    (By.XPATH, "/html/body/span/span/span[2]/ul/li[3]")
                )
            )
            choose_trans.click()

        # # Tìm phần tử chứa số lượng tối đa bằng XPath
        # so_luong_toi_da_element = wait.until(
        #     EC.presence_of_element_located(
        #         (By.XPATH, '//div[@class="mt-2"]/b[@id="txtSoLuongToiDa"]')
        #     )
        # )
        # # Lấy giá trị văn bản từ phần tử
        # so_luong_toi_da = so_luong_toi_da_element.text
        # print(f"quantity số lượng: {so_luong_toi_da}")
        # time.sleep(0.5)
        # purchase_quantity = driver.find_element(By.XPATH, '//*[@id="id_qty"]')
        # purchase_quantity.clear()
        # purchase_quantity.send_keys(so_luong_toi_da)

        time.sleep(0.1)
        payment_method = wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, '//*[@id="pnChiTiet"]/div[2]/div[2]/span/span[1]')
            )
        )
        payment_method.click()
        time.sleep(0.1)
        if data["method"].lower() == "ck":
            choosen_method = driver.find_element(
                By.XPATH, "/html/body/span/span/span[2]/ul/li[1]"
            )
            time.sleep(0.1)
            choosen_method.click()
        else:
            choosen_method = driver.find_element(
                By.XPATH, "/html/body/span/span/span[2]/ul/li[2]"
            )
            time.sleep(0.1)
            choosen_method.click()
        time.sleep(1)
        loop_click(driver, data)
    except Exception as e:
        handle_booking(driver, data)


def automate_user(driver, data):
    try:
        driver.get("https://tructuyen.sjc.com.vn/")
        wait = WebDriverWait(driver, 30)

        name_input = wait.until(EC.presence_of_element_located((By.ID, "id_cccd")))
        login_button = driver.find_element(
            By.XPATH, '//*[@id="register_form"]/div[6]/a'
        )
        login_button.click()

        name_input = wait.until(EC.presence_of_element_located((By.ID, "id_name")))
        print(data["name"])
        name_input.send_keys(data["name"])
        cccd_input = driver.find_element(By.ID, "id_cccd")
        cccd_input.send_keys(data["cccd"])

        login_button = driver.find_element(By.ID, "sign_in_submit")
        driver.execute_script("arguments[0].click();", login_button)

        handle_booking(driver, data)

    except Exception as e:
        print(f"Starting")
        driver.refresh()
        handle_booking(driver, data)


# Mở trang web trên mỗi tab và thực hiện tự động hóa
for index, dr in enumerate(drivers):
    try:
        threading.Thread(
            target=automate_user,
            args=(dr, data_list[index]),
        ).start()
    except Exception as e:
        gc.collect()
