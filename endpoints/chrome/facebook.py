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
  driver.get("https://fdownloader.net/")
  search_box = driver.find_element(By.ID, "s_input")
  search_box.send_keys(url)
  download_button = driver.find_element(
      By.XPATH, "//button[@class='btn-red' and contains(text(),'Download')]")
  download_button.click()
  try:
    elements = WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located((
            By.XPATH,
            "//a[@class='button is-success is-small download-link-fb' and contains(@title, 'Download 720p (HD)')]"
        )))
    links = [element.get_attribute("href") for element in elements]
  except:
    elements = WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located((
            By.CSS_SELECTOR,
            "//a[@class='button is-success is-small download-link-fb' and contains(@title, 'Download 360p (SD)')]"
        )))
    links = [element.get_attribute("href") for element in elements]
  driver.quit()
  return links
  
 