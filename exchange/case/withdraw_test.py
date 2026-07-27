from seleniumbase import BaseCase
from page.login import Login
from page.wallet_history import WalletHistory
from page.assets import Assets
from page.withdraw import Withdraw
from page.common import OTP, Common
import pytest


class WithdrawTest(BaseCase):
    def setUp(self):
        super().setUp()
        self.maximize_window()
        Login.login_and_otp_verify(self)
        self.click(Assets.Withdraw)

    def test_860rvh190(self):
        """檢視各欄位顯示正確"""
        for text in ["出金到你「 已綁定 」的銀行帳戶：", "可用餘額："]:
            self.assert_text(text)

    @pytest.mark.regression
    def test_860rvh19t(self):
        """輸入符合規則的金額及正確資金密碼，可成功出金"""
        Withdraw.withdraw(self)
        OTP.verify(self)
        self.click(Withdraw.Finish)
        self.open(WalletHistory.URL)
        self.click(WalletHistory.FiatTender)
        WalletHistory.search(self, _type="出金")
        self.assert_element(WalletHistory.RowData.format("TWD", "出金", "處理中"))

    def test_860rvh1az(self):
        """資金密碼驗證輸入錯誤資金密碼，無法出金"""
        Withdraw.withdraw(self, pincode="123456")
        self.assert_text("資金密碼錯誤")

    def test_860rvh1bq(self):
        """資金密碼驗證欄位右側，顯示明碼功能正常"""
        self.click(Withdraw.PincodeView)
        Common.assert_type_is_text(self, Withdraw.Pincode)

    def test_860rvh1ca(self):
        """到帳金額為提領金額減去銀行手續費"""
        self.type(Withdraw.Amount, "123")
        self.assert_element(Withdraw.TotalAmount.format("108 TWD"))
