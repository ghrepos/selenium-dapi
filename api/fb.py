from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import Firefox as WebDriver
from selenium.webdriver.firefox.options import Options

options = Options()
options.add_argument('-headless')

def get(url):
  driver = WebDriver(options=options)
  driver.get("https://fdownloader.net/")
  search_box = driver.find_element(By.ID, "s_input")
  search_box.send_keys(url)
  download_button = driver.find_element(
      By.XPATH, "//button[@class='btn-red' and contains(text(),'Download')]")
  download_button.click()
  try:
    video_link = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((
            By.XPATH,
            "//a[@class='button is-success is-small download-link-fb' and contains(@title, 'Download 720p (HD)')]"
        ))).get_attribute("href")
  except:
    video_link = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((
            By.CSS_SELECTOR,
            "//a[@class='button is-success is-small download-link-fb' and contains(@title, 'Download 360p (SD)')]"
        ))).get_attribute("href")
  driver.quit()
  return [video_link]
