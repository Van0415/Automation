from page.common import Common, OTP
from seleniumbase import BaseCase
import os
from dotenv import load_dotenv

load_dotenv()


class Login(BaseCase):
    URL = f"{Common.URL}/login?skipRecaptcha=true"
    Account = '//input[@id="account"]'
    Password = '//input[@id="password"]'
    ShowPassword = '//*[contains(@class,"absolute")]'
    LoginBtn = '//button[text()="登入"]'
    ForgetPassword = '//*[text()="忘記密碼"]'
    SignupNow = '//*[text()="立即註冊"]'

    def login(self, account=os.getenv("ACCOUNT"), password=os.getenv("PASSWORD")):
        self.type(Login.Account, account)
        self.type(Login.Password, password)
        self.click(Login.LoginBtn)

    def login_and_otp_verify(self, account=os.getenv("ACCOUNT"), password=os.getenv("PASSWORD")):
        self.open(Login.URL)
        Login.login(self, account, password)
        OTP.verify(self)
        self.assert_text("錢包紀錄")
        self.sleep(0.5)
        self.reload()
        self.sleep(0.5)
        self.reload()
