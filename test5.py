chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-gpu")
browser = webdriver.Chrome(options=chrome_options)


browser.get("https://www.google.com")
"Page title was '{}'".format(browser.title)

browser.quit()