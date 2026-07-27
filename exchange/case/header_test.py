from seleniumbase import BaseCase
from page.login import Login
from page.header import Header
from page.common import Common
import os
from dotenv import load_dotenv

load_dotenv()


class HeaderTest(BaseCase):
    def setUp(self):
        super().setUp()
        self.maximize_window()
        Login.login_and_otp_verify(self)

    def test_860ruqvc6(self):
        """帳號顯示正確"""
        self.click(Header.Account)
        self.assert_text(os.getenv("ACCOUNT"))

    def test_860ruqvct(self):
        """登出功能正常"""
        Header.logout(self)
        self.assert_url(Login.URL)


# class HeaderTest_LV0(BaseCase):
#     def setUp(self):
#         super().setUp()
#         self.maximize_window()
#         Login.login_and_otp_verify(self, os.getenv("ACCOUNT_LV0"), os.getenv("PASSWORD_LV0"))

#     def test_860ruqv5z(self):
#         """入出金功能皆無法使用"""
#         self.click(Header.TransferMoney)
#         Common.assert_disabled(self, Header.Deposit)
#         Common.assert_disabled(self, Header.Withdraw)

#     def test_860ruqv67(self):
#         """入提幣功能皆無法使用"""
#         self.click(Header.TransferMoney)
#         Common.assert_disabled(self, Header.CryptosDeposit)
#         Common.assert_disabled(self, Header.CryptosWithdraw)


# class HeaderTest_LV1(BaseCase):
#     def setUp(self):
#         super().setUp()
#         self.maximize_window()
#         Login.login_and_otp_verify(self, os.getenv("ACCOUNT_LV1"), os.getenv("PASSWORD_LV1"))

#     def test_860ruqv95(self):
#         """入出金功能皆無法使用"""
#         self.click(Header.TransferMoney)
#         Common.assert_disabled(self, Header.Deposit)
#         Common.assert_disabled(self, Header.Withdraw)

#     def test_860ruqv9h(self):
#         """入提幣功能可正常使用"""
#         self.click(Header.TransferMoney)
#         Common.assert_disabled(self, Header.CryptosDeposit)
#         Common.assert_disabled(self, Header.CryptosWithdraw)
