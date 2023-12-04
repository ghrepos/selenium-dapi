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
  driver.get('https://snaptik.app/')
  input_element = driver.find_element(By.CLASS_NAME, "link-input")
  input_element.send_keys(url)
  submit_button = driver.find_element(By.CLASS_NAME, "button-go")
  submit_button.click()
  wait = WebDriverWait(driver, 10)
  try:
    download_video = wait.until(
    EC.presence_of_element_located((By.CLASS_NAME, "download-file")))
    fileurl = download_video.get_attribute("href")
    video = True
  except:
    download_photos = wait.until(
    EC.presence_of_all_elements_located((By.CLASS_NAME, "w100")))
    fileurl = fileurl = [element.get_attribute("href") for element in download_photos]
    video = False
  driver.quit()
  return fileurl, video