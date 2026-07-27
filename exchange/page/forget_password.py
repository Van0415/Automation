from page.common import Common
from seleniumbase import BaseCase
import os
from dotenv import load_dotenv

load_dotenv()


class ForgetPassword(BaseCase):
    URL = f"{Common.URL}/forget-password"
    Account = '//*[@id="account"]'
    Submit = '//*[@data-testid="signup"]'
    BackToLogin = '//*[text()="返回登入"]'

    def send_member_account(self, account=os.getenv("ACCOUNT")):
        self.type(ForgetPassword.Account, account)
        self.click(ForgetPassword.Submit)


class ResetPassword:
    SetNewPassword = '//*[@id="password"]'
    ConfirmPassword = '//*[@id="passwordConfirmation"]'
    SetNewPasswordShowPassword = (
        '//*[@role="group"][contains(.,"設置新密碼")]//*[contains(@class,"chakra-input__right-element")]'
    )
    ConfirmPasswordShowPassword = (
        '//*[@role="group"][contains(.,"再次確認")]//*[contains(@class,"chakra-input__right-element")]'
    )
    Submit = '//*[@data-testid="signup"]'
