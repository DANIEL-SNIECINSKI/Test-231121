import unittest
from selenium import webdriver

# Test du 30-11-21 (lignes 5-6-7)
from selenium.webdriver.chrome.options import Options
chrome_options = Options()
chrome_options.add_argument("--headless")


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
