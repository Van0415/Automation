from seleniumbase import BaseCase
from page.login import Login
from page.withdraw_crypto import WithdrawCrypto
from page.assets import Assets
from page.wallet_history import WalletHistory
from page.common import OTP, Common
import pytest
import os
from dotenv import load_dotenv

load_dotenv()


class WithdrawCryptoTest(BaseCase):
    def setUp(self):
        super().setUp()
        self.maximize_window()
        Login.login_and_otp_verify(self)
        self.click(Assets.WithdrawCrypto.format("USDT"))

    @pytest.mark.regression
    def test_860rvh300(self):
        """USDT-TRC20提領成功"""
        WithdrawCrypto.withdraw(self)
        OTP.verify(self)
        self.click(WithdrawCrypto.Confirm)
        self.open(WalletHistory.URL)
        WalletHistory.search(self)
        self.assert_element(WalletHistory.RowData.format("USDT", "提幣", "處理中"))

    def test_860rvh4k7(self):
        """檢視各欄位值與Step1填寫一致"""
        self.type(WithdrawCrypto.Address, os.getenv("CRYPTO_ADDRESS"))
        self.type(WithdrawCrypto.Name, "automation")
        self.click(WithdrawCrypto.Submit)
        for text in ["USDT", "TRC20", os.getenv("CRYPTO_ADDRESS"), "automation"]:
            self.assert_text(text)

    def test_860rvh4nx(self):
        """資金密碼輸入錯誤資金密碼，無法送出"""
        WithdrawCrypto.withdraw(self, pincode="111111")
        self.assert_text("資金密碼錯誤")

    def test_860rvh4pp(self):
        """資金密碼欄位右側，顯示明碼功能正常"""
        self.type(WithdrawCrypto.Address, os.getenv("CRYPTO_ADDRESS"))
        self.type(WithdrawCrypto.Name, "automation")
        self.click(WithdrawCrypto.Submit)
        self.click(WithdrawCrypto.PincodeView)
        Common.assert_type_is_text(self, WithdrawCrypto.Pincode)

    def test_860rvh4qd(self):
        """提幣數額顯示為提領數額減去手續費數值"""
        self.type(WithdrawCrypto.Address, os.getenv("CRYPTO_ADDRESS"))
        self.type(WithdrawCrypto.Name, "automation")
        self.click(WithdrawCrypto.Submit)
        self.type(WithdrawCrypto.Amount, 20)
        self.assert_text("18.8 USDT")

    def test_860rvh4x8(self):
        """檢視各欄位值與Step1、Step2填寫一致"""
        WithdrawCrypto.withdraw(self)
        OTP.verify(self)
        for text in ["USDT", os.getenv("CRYPTO_ADDRESS"), "automation", "20 USDT", "18.8 USDT"]:
            self.assert_text(text)
