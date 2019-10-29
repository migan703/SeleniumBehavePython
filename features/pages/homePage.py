from basePage import basePage

class homePage(basePage):
    idFristNameReg = 'firstname' # name
    idLastNameReg = 'lastname' # name
    idEmailReg = 'reg_email__' # name
    idConfirmEmailReg = 'reg_email_confirmation__'# name
    idPasswordReg = 'reg_passwd__' # name
    idMonthReg = 'birthday_month' # name
    idDateReg = 'birthday_day' # name
    idYearReg = 'birthday_year' # name
    idFemaleReg = '._8esa[value="1"]'  # xpath
    idMaleReg = '._8esa[value="2"]' # xpath
    idSingUpButton = 'websubmit' # name
    idSingInButton = 'u_0_b' # id
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
        #self.setConfirmEmail(email_) # No registrar el usuario
        self.setPasswordReg(_password)

    def setBirthday(self,day,month,year):
        date_ = self.driver.find_element_by_name(self.idDateReg)
        date_.send_keys(day)
        month_ = self.driver.find_element_by_name(self.idMonthReg)
        month_.send_keys(month)
        year_ = self.driver.find_element_by_name(self.idYearReg)
        year_.send_keys(year)

    def setFemale(self):
        elem = self.driver.find_element_by_xpath(self.idFemaleReg)
        elem.click()

    def setMale(self):
        elem = self.driver.find_element_by_xpath(self.idMaleReg)
        elem.click()

    def singUp(self):
        elem = self.driver.find_element_by_name(self.idSingUpButton)
        elem.click()
    
    def singIn(self):
        elem = self.driver.find_elements_by_id(self.idSingInButton)
        elem.click()
    
    def setEmail(self,email):
        elem = self.driver.find_elements_by_name(self.idEmail)
        elem.send_keys(email)
    
    def setPassword(self,password):
        elem = self.driver.find_elements_by_name(self.idPassword)
        elem.send_keys(password)

    def logIn(self):
        elem = self.driver.find_elements_by_id(self.idLogInButton)
        elem.click()