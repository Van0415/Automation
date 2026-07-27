from seleniumbase import BaseCase
from page.home import Home
from page.login import Login
from page.signup import Signup


class HomeTest(BaseCase):
    def setUp(self):
        super().setUp()
        self.maximize_window()
        self.open(Home.URL)

    def test_860ru8hm5(self):
        """頁面文案顯示正確"""
        for text in ["最友善加密貨幣交易所", "就是 HOYA BIT", "從新手到專業者，都能輕鬆使用！"]:
            self.assert_text(text)

    def test_860ru8hmx(self):
        """註冊導向頁面正確"""
        self.click(Home.TopBlockRegister)
        self.assert_url(Signup.URL)

    def test_860ru8hq7(self):
        """點擊買入，各幣種資訊顯示正確"""
        self.click(Home.MarketBuy)
        for text in ["幣別", "買入價格(TWD)", "24H 漲跌", "7日價格走勢", "BTC", "ETH", "USDT", "DOGE", "MATIC"]:
            self.assert_text(text)

    def test_860ru8hqa(self):
        """點擊賣出，各幣種資訊顯示正確"""
        self.click(Home.MarketSold)
        for text in ["幣別", "賣出價格(TWD)", "24H 漲跌", "7日價格走勢", "BTC", "ETH", "USDT", "DOGE", "MATIC"]:
            self.assert_text(text)

    def test_860ru8ht0(self):
        """立即註冊導向頁面正確"""
        self.click(Home.MidBlockRegister)
        self.assert_url(Signup.URL)

    def test_860ru8hvh(self):
        """頁面文案顯示正確"""
        for text in ["合法合規", "學習認證", "化繁為簡", "資安升級", "電子信箱", "身分驗證", "入金交易"]:
            self.assert_text(text)

    def test_860ru8hw4(self):
        """立即註冊導向頁面正確"""
        self.click(Home.DownBlockRegister)
        self.assert_url(Signup.URL)

    def test_860ru8hxy(self):
        """點擊我的資產，導向登入頁"""
        self.click(Home.MyAssets)
        self.assert_url(Login.URL)

    def test_860ru8hy8(self):
        """點擊現貨買賣，導向登入頁"""
        self.click(Home.SpotTrading)
        self.assert_url(Login.URL)

    def test_860ru8hyb(self):
        """點擊日日生幣，導向登入頁"""
        self.click(Home.DailyCoins)
        self.assert_url(Login.URL)
