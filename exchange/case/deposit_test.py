from seleniumbase import BaseCase
from page.login import Login
from page.deposit import Deposit
from page.assets import Assets
import pyperclip


class DepositTest(BaseCase):
    def setUp(self):
        super().setUp()
        self.maximize_window()
        Login.login_and_otp_verify(self)
        self.click(Assets.Deposit)

    def test_860rvh13t(self):
        """檢視各欄位顯示正確"""
        for text in ["遠銀受託禾亞數位科技信託財產專戶", "805 遠東國際商業銀行", " ｜ 0012 營業部"]:
            self.assert_text(text)

    def test_860rvh13w(self):
        """銀行帳號欄位複製功能正常"""
        bank_account = self.get_attribute(Deposit.BankAccount, "value")
        self.click(Deposit.CopyBankAccount)
        assert bank_account == pyperclip.paste()

    def test_860rvh148(self):
        """單日限額符合等級限制"""
        self.assert_text("單日限額：無上限")

    def test_860rvh14t(self):
        """單月限額符合等級限制"""
        self.assert_text("單月限額：無上限")
