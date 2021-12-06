import unittest
#from selenium import webdriver

# Test 06-12-21

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')
chrome_options.binary_location = '/usr/bin/google-chrome'

#chrome_driver = '/usr/bin/chromedriver'

#driver = webdriver.Chrome(executable_path=chrome_driver, chrome_options=chrome_options)

#############################################""


class TestUbuntuHomepage(unittest.TestCase):

    def setUp(self):
#        self.browser = webdriver.Chrome()
        self.browser = webdriver.Chrome(executable_path='/usr/bin/chromedriver')
        
    def testTitle(self):
        self.browser.get('http://www.ubuntu.com/')
        self.assertIn('Ubuntu', self.browser.title)

    def tearDown(self):
        self.browser.quit()


if __name__ == '__main__':
    unittest.main(verbosity=2)
