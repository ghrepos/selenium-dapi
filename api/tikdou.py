from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from preset import options
from douyin_tiktok_scraper.scraper import Scraper
import asyncio

api = Scraper()

def get(url):
    try:
        file_url, music_url, is_video = asyncio.run(get_api(url))
    except:
        file_url, is_video = get_web(url)
        music_url = None 
    return file_url, music_url, is_video

async def get_api(url: str) -> dict:
    result = await api.hybrid_parsing(url)
    if result.get("video_data"):
        is_video = True
        file_url = result["video_data"]["nwm_video_url"]
    else:
        is_video = False
        file_url = result["image_data"]["no_watermark_image_list"]
    music_url = result["music"]["play_url"]["url_list"][0]
    return file_url, music_url, is_video

def get_web(url):
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
    file_url = download_video.get_attribute("href")
    is_video = True
  except:
    download_photos = wait.until(
    EC.presence_of_all_elements_located((By.CLASS_NAME, "w100")))
    file_url = file_url = [element.get_attribute("href") for element in download_photos]
   is_video = False
  driver.quit()
  return file_url, is_video