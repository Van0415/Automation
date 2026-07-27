from seleniumbase import BaseCase
from page.articles import Articles
from page.signup import Signup
from page.login import Login
from page.common import Common


class SignupTest(BaseCase):
    def setUp(self):
        super().setUp()
        self.maximize_window()
        self.open(Signup.URL)

    def test_860ru9qm7(self):
        """電子信箱格式錯誤，顯示提示正確"""
        self.type(Signup.Email, "wrong_format")
        self.click(Signup.Submit)
        self.assert_text("格式不符")

    def test_860ru9qmv(self):
        """設置密碼不符合規則，無法送出"""
        self.type(Signup.Password, "wrong_format")
        Common.assert_disabled(self, Signup.Submit)

    def test_860ru9qp5(self):
        """設置密碼欄位右側，顯示明碼功能正常"""
        self.click(Signup.ShowPassword)
        Common.assert_type_is_text(self, Signup.Password)

    def test_860ru9qrq(self):
        """註冊下方，使用者條款連結正確"""
        self.click(Signup.UserTerms)
        self.assert_url(Articles.TermsURL)

    def test_860ru9qtu(self):
        """註冊下方，隱私權政策連結正確"""
        self.click(Signup.PrivacyPolicy)
        self.assert_url(Articles.PolicyURL)

    def test_860ru9que(self):
        """立即登入導向頁面正確"""
        self.click(Signup.LoginNow)
        self.assert_url(Login.URL)
