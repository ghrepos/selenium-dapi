from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import logging

options = webdriver.ChromeOptions()
options.add_argument('--headless')
options.add_argument("--start-maximized")
options.add_argument('--no-sandbox')
options.add_argument('--disable-gpu')
options.add_argument('--disable-dev-shm-usage')

def get(url):
    driver = webdriver.Chrome(options=options)
    driver.get(f"https://snapinsta.to/en?q={url}")
    wait = WebDriverWait(driver, 15)
    
    try:
        elements = wait.until(EC.presence_of_all_elements_located((By.XPATH, "//a[@title='Download Video']")))
        download_links = [element.get_attribute("href") for element in elements]
        is_video = True
    except:
        elements = wait.until(EC.presence_of_all_elements_located((By.XPATH, "//a[@title='Download Photo']")))
        download_links = [element.get_attribute("href") for element in elements]
        is_video = False

    driver.quit()
    return is_video, download_links