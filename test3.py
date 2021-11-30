from selenium import webdriver

DRIVER_PATH = '/home/daniel/drivers/chromedriver'
driver = webdriver.Chrome(executable_path=DRIVER_PATH)
driver.get('https://google.com')