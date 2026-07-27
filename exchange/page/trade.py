from page.common import Common
from seleniumbase import BaseCase


class Trade(BaseCase):
    URL = f"{Common.URL}/trade"
    Buy = '//button[text()="買入"]'
    Sell = '//button[text()="賣出"]'
    Payment = '//*[text()="支付" or text()="出售"]/..//*[contains(@class,"chakra-select__wrapper")]'
    Get = '//*[text()="獲得"]/../..//*[contains(@class,"chakra-select__wrapper")]'
    PaymentType = (
        '//*[text()="支付" or text()="出售"]/..//*[contains(@class,"chakra-select__wrapper")]//option[text()="{}"]'
    )
    GetType = '//*[text()="獲得"]/../..//*[contains(@class,"chakra-select__wrapper")]//option[text()="{}"]'
    PaymentAmount = '//input[@inputmode="decimal"][not(@readonly)]'
    OrderPreview = '//*[text()="訂單預覽"]'
    OrderConfirm = '//*[text()="確認送出"]'
    ContinueTrade = '//*[text()="繼續買賣"]'
    ViewMyAssets = '//*[text()="查看我的資產"]'
    TradeHistory = '//*[text()="交易紀錄"]'
    Img = '//img[@alt="{}"]'

    def buy(self, payment_type="TWD", get_type="USDT", amount=300):
        self.click(Trade.Buy)
        self.assert_text("支付")
        self.click(Trade.Payment)
        self.click(Trade.PaymentType.format(payment_type))
        self.click(Trade.Get)
        self.click(Trade.GetType.format(get_type))
        self.type(Trade.PaymentAmount, amount)
        self.click(Trade.OrderPreview)
        self.click(Trade.OrderConfirm)
        self.click(Trade.ContinueTrade)

    def sell(self, payment_type="USDT", get_type="TWD", amount=10):
        self.click(Trade.Sell)
        self.assert_text("出售")
        self.click(Trade.Payment)
        self.click(Trade.PaymentType.format(payment_type))
        self.click(Trade.Get)
        self.click(Trade.GetType.format(get_type))
        self.type(Trade.PaymentAmount, amount)
        self.click(Trade.OrderPreview)
        self.click(Trade.OrderConfirm)
        self.click(Trade.ContinueTrade)
