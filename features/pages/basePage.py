from selenium import webdriver

class basePage():
    url = 'https://en-gb.facebook.com/r.php'
    
    def __init__ (self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()

    def navigate(self):
          self.driver.get(self.url)