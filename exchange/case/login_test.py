from seleniumbase import BaseCase
from page.login import Login
from page.signup import Signup
from page.forget_password import ForgetPassword
from page.assets import Assets
from page.common import Common, OTP


class LoginTest(BaseCase):
    def setUp(self):
        super().setUp()
        self.maximize_window()
        self.open(Login.URL)

    def test_860ru8j38(self):
        """帳號密碼輸入正確，OTP驗證成功登入"""
        Login.login(self)
        OTP.verify(self)
        self.assert_url(Assets.URL)

    def test_860ru8j3z(self):
        """帳號密碼輸入正確，OTP輸入錯誤驗證碼，登入失敗"""
        Login.login(self)
        OTP.verify(self, "1")
        self.assert_text("驗證碼錯誤")

    def test_860ru8j6b(self) -> None:
        """帳號格式錯誤，顯示提示正確"""
        self.type(Login.Account, "wrong_format")
        self.assert_text("請輸入正確的電子信箱或手機號碼")

    def test_860ru8j72(self):
        """帳號錯誤密碼正確，無法登入"""
        Login.login(self, account="wrong_account@hoyabit.com")
        Common.assert_text_contains(self, "帳號或密碼不相符")

    def test_860ru8j77(self):
        """密碼不符合規則，顯示提示正確"""
        self.type(Login.Password, "wrong_format")
        self.assert_text("包含至少一大寫及小寫英文字母，長度為 8 - 16 位數的英數組合")

    def test_860ru8j7b(self):
        """帳號正確密碼錯誤，無法登入"""
        Login.login(self, password="WrongPassword0")
        Common.assert_text_contains(self, "帳號或密碼不相符")

    def test_860ru8j7k(self):
        """密碼欄位右側，顯示明碼功能正常"""
        self.click(Login.ShowPassword)
        Common.assert_type_is_text(self, Login.Password)

    def test_860rybx3z(self):
        """忘記密碼導向頁面正確"""
        self.click(Login.ForgetPassword)
        self.assert_url(ForgetPassword.URL)

    def test_860ru8jaw(self):
        """立即註冊導向頁面正確"""
        self.click(Login.SignupNow)
        self.assert_url(Signup.URL)
