from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import Firefox as WebDriver
from selenium.webdriver.firefox.options import Options

options = Options()
options.add_argument('-headless')

def get(url):
  driver = WebDriver(options=options)
  driver.get('https://snaptik.app/')

  input_element = driver.find_element(By.CLASS_NAME, "link-input")
  input_element.send_keys(url)
  submit_button = driver.find_element(By.CLASS_NAME, "button-go")
  submit_button.click()
  wait = WebDriverWait(driver, 10)
  try:
    download_video = wait.until(
    EC.presence_of_element_located((By.CLASS_NAME, "download-file")))
    fileurl = download_link.get_attribute("href")
    video = True
  except:
    download_photos = wait.until(
    EC.presence_of_all_elements_located((By.CLASS_NAME, "w100")))
    fileurl = [button.get_attribute("href") for button in download_photos]
    video = False
  driver.quit()
  return fileurl, video
