from seleniumbase import BaseCase
from page.login import Login
from page.trade import Trade
from page.trade_history import TradeHistory
import pytest


class TradeTest(BaseCase):
    def setUp(self):
        super().setUp()
        self.maximize_window()
        Login.login_and_otp_verify(self)
        self.open(Trade.URL)

    @pytest.mark.regression
    def test_860rvnuff(self):
        """送出後可成功交易"""
        Trade.buy(self)
        self.open(TradeHistory.URL)
        TradeHistory.search(self)
        self.assert_element(TradeHistory.RowData.format("TWD ➔ USDT", "300 TWD", "已完成"))

    @pytest.mark.regression
    def test_860rvnux6(self):
        """送出後可成功交易"""
        Trade.sell(self, "BTC", "USDT", 0.0006)
        self.open(TradeHistory.URL)
        TradeHistory.search(self)
        self.assert_element(TradeHistory.RowData.format("BTC ➔ USDT", "0.0006 BTC", "已完成"))

    def test_860rvnu9a(self):
        """可切換為TWD"""
        self.click(Trade.Payment)
        self.click(Trade.PaymentType.format("TWD"))
        self.assert_element(Trade.Img.format("TWD"))

    def test_860rvnu9v(self):
        """可切換為USDT"""
        self.click(Trade.Payment)
        self.click(Trade.PaymentType.format("USDT"))
        self.assert_element(Trade.Img.format("USDT"))

    def test_860rvnub3(self):
        """可切換為BTC"""
        self.click(Trade.Get)
        self.click(Trade.GetType.format("BTC"))
        self.assert_element(Trade.Img.format("BTC"))

    def test_860rvnuc2(self):
        """可切換為ETH"""
        self.click(Trade.Get)
        self.click(Trade.GetType.format("ETH"))
        self.assert_element(Trade.Img.format("ETH"))

    def test_860rvnucw(self):
        """支付幣種為TWD時，可切換為USDT"""
        self.click(Trade.Payment)
        self.click(Trade.PaymentType.format("TWD"))
        self.click(Trade.Get)
        self.click(Trade.GetType.format("USDT"))
        self.assert_element(Trade.Img.format("USDT"))

    def test_860rvnudm(self):
        """可切換為DOGE"""
        self.click(Trade.Get)
        self.click(Trade.GetType.format("DOGE"))
        self.assert_element(Trade.Img.format("DOGE"))

    def test_860rvnue0(self):
        """可切換為MATIC"""
        self.click(Trade.Get)
        self.click(Trade.GetType.format("MATIC"))
        self.assert_element(Trade.Img.format("MATIC"))
