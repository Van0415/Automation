from seleniumbase import BaseCase
from page.assets import Assets
from page.wallet_history import WalletHistory
from page.login import Login
from page.withdraw import Withdraw
from page.common import OTP
from api.login import LoginAPI
from api.withdraw_crypto import WithdrawCryptoAPI
from api.common import OTPAPI
import os
from dotenv import load_dotenv

load_dotenv()


class WalletHistoryTest(BaseCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.login_api = LoginAPI()
        token = cls.login_api.login_and_otp_verify()
        cls.withdraw_crypto_api = WithdrawCryptoAPI(token)
        cls.otp_api = OTPAPI(token)

    def setUp(self):
        super().setUp()
        self.maximize_window()
        Login.login_and_otp_verify(self)
        self.click(Assets.WalletHistory)

    def test_860rvh03c(self):
        """全部搜尋，顯示資料正確"""
        mfa_id = self.withdraw_crypto_api.withdraw(os.getenv("CRYPTO_ADDRESS"))
        self.otp_api.verify(mfa_id)
        self.withdraw_crypto_api.withdraw_confirm(mfa_id)
        WalletHistory.search(self)
        self.assert_element(WalletHistory.RowData.format("USDT", "提幣", "處理中"))

    def test_860rvh06h(self):
        """切換為提幣搜尋，顯示資料正確"""
        mfa_id = self.withdraw_crypto_api.withdraw(os.getenv("CRYPTO_ADDRESS"))
        self.otp_api.verify(mfa_id)
        self.withdraw_crypto_api.withdraw_confirm(mfa_id)
        WalletHistory.search(self)
        self.assert_element(WalletHistory.RowData.format("USDT", "提幣", "處理中"))

    def test_860rvh09g(self):
        """全部搜尋，顯示資料正確"""
        mfa_id = self.withdraw_crypto_api.withdraw(os.getenv("CRYPTO_ADDRESS"))
        self.otp_api.verify(mfa_id)
        self.withdraw_crypto_api.withdraw_confirm(mfa_id)
        WalletHistory.search(self)
        self.assert_element(WalletHistory.RowData.format("USDT", "提幣", "處理中"))

    def test_860rvh0e3(self):
        """檢視頁面資訊顯示正確"""
        mfa_id = self.withdraw_crypto_api.withdraw(os.getenv("CRYPTO_ADDRESS"))
        self.otp_api.verify(mfa_id)
        self.withdraw_crypto_api.withdraw_confirm(mfa_id)
        WalletHistory.search(self)
        self.click(WalletHistory.Detail)
        for text in ["提幣", os.getenv("CRYPTO_ADDRESS"), "automation", "處理中"]:
            self.assert_text(text)

    def test_860rvh0rc(self):
        """全部搜尋，顯示資料正確"""
        self.open(Assets.URL)
        self.click(Assets.Withdraw)
        Withdraw.withdraw(self)
        OTP.verify(self)
        self.click(Withdraw.Finish)
        self.open(WalletHistory.URL)
        self.click(WalletHistory.FiatTender)
        WalletHistory.search(self, _type="出金")
        self.assert_element(WalletHistory.RowData.format("TWD", "出金", "處理中"))

    def test_860rvh0wf(self):
        """切換為出金搜尋，顯示資料正確"""
        self.open(Assets.URL)
        self.click(Assets.Withdraw)
        Withdraw.withdraw(self)
        OTP.verify(self)
        self.click(Withdraw.Finish)
        self.open(WalletHistory.URL)
        self.click(WalletHistory.FiatTender)
        WalletHistory.search(self, _type="出金")
        self.assert_element(WalletHistory.RowData.format("TWD", "出金", "處理中"))

    def test_860rvh0yz(self):
        """全部搜尋，顯示資料正確"""
        self.open(Assets.URL)
        self.click(Assets.Withdraw)
        Withdraw.withdraw(self)
        OTP.verify(self)
        self.click(Withdraw.Finish)
        self.open(WalletHistory.URL)
        self.click(WalletHistory.FiatTender)
        WalletHistory.search(self, _type="出金")
        self.assert_element(WalletHistory.RowData.format("TWD", "出金", "處理中"))

    def test_860rvh12f(self):
        """檢視頁面資訊顯示正確"""
        self.open(Assets.URL)
        self.click(Assets.Withdraw)
        Withdraw.withdraw(self)
        OTP.verify(self)
        self.click(Withdraw.Finish)
        self.open(WalletHistory.URL)
        self.click(WalletHistory.FiatTender)
        WalletHistory.search(self, _type="出金")
        self.click(WalletHistory.Detail)
        for text in ["出金", "處理中"]:
            self.assert_text(text)
