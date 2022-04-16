from pages.Register import RegisterAccount
from utilities.Generic import Reusable


class Test_RA_001():

    baseUrl  = "https://demo.opencart.com/"
    name = Reusable.getFirstName()
    ln = Reusable.getLastName()
    email = Reusable.getEmail()
    tel = Reusable.getMobile()
    password = name
    confPassword = name

    def test_Reg(self,setup):
            self.driver = setup
            self.driver.get(self.baseUrl)

            self.reg =  RegisterAccount(self.driver)
            self.reg.navigateToRegisterPage()
            self.reg.createAccount(self.name,self.ln,self.email,self.tel, self.password,self.confPassword)
