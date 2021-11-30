from selenium import webdriver
from selenium.webdriver.chrome.options import Options
chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument('--no-sandbox')
# chrome_options.add_argument('--disable-dev-shm-usage')
# chrome_options.add_argument('--remote-debugging-port=9222')
driver = webdriver.Chrome('/usr/bin/chromedriver', options=chrome_options)
driver.get('http://www.google.com')
print('test')
driver.close()