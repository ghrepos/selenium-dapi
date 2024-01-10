from selenium import webdriver

options = webdriver.ChromeOptions()
options.add_argument('--headless')
# options.add_argument("--start-maximized")
options.add_argument('--no-sandbox')
#options.add_argument('--disable-gpu')
options.add_argument('--disable-dev-shm-usage')