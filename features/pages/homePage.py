from selenium.webdriver.common.keys import Keys
from features.pages.basePage import basePage

class homePage(basePage):
    idFristNameReg = 'firstname' # name
    idLastNameReg = 'lastname' # name
    idEmailReg = 'reg_email__' # name
    idConfirmEmailReg = 'reg_email_confirmation__'# name
    idPasswordReg = 'reg_passwd__' # name
    idMonthReg = 'birthday_month' # name
    idDateReg = 'birthday_day' # name
    idYearReg = 'birthday_year' # name
    idFemaleReg = 'u_0_6' # id
    idMaleReg = 'u_0_7' # id
    idSingUpButton = 'websubmit' # name
    idSingInButton = 'menu_login_show_link' # id
    idEmail = 'email' # name
    idPassword = 'pass' # name
    idLogInButton = 'u_0_c' # id

    def setName(self,name):
        elem = self.driver.find_element_by_name(self.idFristNameReg)
        elem.send_keys(name)

    def setLastName(self,lastName):
        elem = self.driver.find_element_by_name(self.idLastNameReg)
        elem.send_keys(lastName)

    def setEmailReg(self,email):
        elem = self.driver.find_element_by_name(self.idEmailReg)
        elem.send_keys(email)
    
    def setConfirmEmail(self,confirmEmail):
        elem = self.driver.find_element_by_name(self.idConfirmEmailReg)
        elem.send_keys(confirmEmail)
    
    def setPasswordReg(self,passwordReg):
        elem = self.driver.find_element_by_name(self.idPasswordReg)
        elem.send_keys(passwordReg)

    def setPrincipalUserInfo(self,name_,lastName_,email_,_password):
        self.setName(name_)
        self.setLastName(lastName_)
        self.setEmailReg(email_)
        self.setConfirmEmail(email_)
        self.setPasswordReg(_password)

    def setBirthday(self,day,month,year):
        date_ = self.driver.find_element_by_name(self.idDateReg)
        date_.send_keys(day)
        month_ = self.driver.find_element_by_name(self.idMonthReg)
        month_.send_keys(month)
        year_ = self.driver.find_element_by_name(self.idYearReg)
        year_.send_keys(year)

    def setFemale(self):
        elem = self.driver.find_element_by_id(self.idFemaleReg)
        elem.click()

    def setMale(self):
        elem = self.driver.find_element_by_id(self.idMaleReg)
        elem.click()

    def singUp(self, file):
        self.driver.get_screenshot_as_file(file)
        elem = self.driver.find_element_by_name(self.idSingUpButton)
        elem.click()
    
    def singIn(self):
        elem = self.driver.find_element_by_id(self.idSingInButton)
        print(elem)
        elem.click()
    
    def setEmail(self,email):
        elem = self.driver.find_element_by_id(self.idEmail)
        elem.send_keys(email)
    
    def setPassword(self,password):
        elem = self.driver.find_element_by_id(self.idPassword)
        elem.send_keys(password)

    def logIn(self,file):
        self.driver.save_screenshot(file)
        elem = self.driver.find_element_by_id(self.idLogInButton)
        elem.click()