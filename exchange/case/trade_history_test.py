from seleniumbase import BaseCase
from page.home import Home
from page.trade_history import TradeHistory
from page.login import Login
from page.trade import Trade
from api.login import LoginAPI
from api.trade import TradeAPI


class TradeHistoryTest(BaseCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.login_api = LoginAPI()
        token = cls.login_api.login_and_otp_verify()
        cls.trade_api = TradeAPI(token)

    def setUp(self):
        super().setUp()
        self.maximize_window()
        Login.login_and_otp_verify(self)
        self.click(Home.SpotTrading)
        self.click(Trade.TradeHistory)

    def test_860rvntmf(self):
        """切換為全部後，查詢正確"""
        order_id = self.trade_api.order()
        self.trade_api.confirm(order_id)
        TradeHistory.search(self)
        self.assert_element(TradeHistory.RowData.format("TWD ➔ USDT", "300 TWD", "已完成"))

    def test_860rvnttw(self):
        """切換為全部後，查詢正確"""
        order_id = self.trade_api.order()
        self.trade_api.confirm(order_id)
        TradeHistory.search(self)
        self.assert_element(TradeHistory.RowData.format("TWD ➔ USDT", "300 TWD", "已完成"))

    def test_860rvntxu(self):
        """全部搜尋，顯示資料正確"""
        order_id = self.trade_api.order()
        self.trade_api.confirm(order_id)
        TradeHistory.search(self)
        self.assert_element(TradeHistory.RowData.format("TWD ➔ USDT", "300 TWD", "已完成"))

    def test_860rvnu0b(self):
        """檢視頁面資訊顯示正確"""
        order_id = self.trade_api.order()
        self.trade_api.confirm(order_id)
        TradeHistory.search(self)
        self.click(TradeHistory.Detail)
        for text in ["- 300 TWD", "已完成"]:
            self.assert_text(text)
