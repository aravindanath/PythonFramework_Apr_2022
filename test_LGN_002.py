from pages.LoginPage import Login
from pages.PoductPage import Product
from utilities.Generic import Reusable


class Test_RA_001():

    baseUrl  = "https://admin-demo.nopcommerce.com/login?ReturnUrl=%2Fadmin%2F"

    email = "admin@yourstore.com"
    password = "admin"


    def test_Reg(self,setup):
            self.driver = setup
            self.driver.get(self.baseUrl)
            self.lg =  Login(self.driver)
            self.lg.login(self.email,self.password)
            self.pg =  Product(self.driver)
            self.pg.navigateToProductPage()
