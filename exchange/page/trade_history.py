from page.common import Common
from seleniumbase import BaseCase


class TradeHistory(BaseCase):
    URL = f"{Common.URL}/trade/trade-history"
    FilterPayment = '//*[contains(@class,"chakra-stack")][contains(.,"付出幣種")]//select'
    FilterPaymentOption = '//*[contains(@class,"chakra-stack")][contains(.,"付出幣種")]//option[text()="{}"]'
    FilterGet = '//*[contains(@class,"chakra-stack")][contains(.,"換入幣種")]//select'
    FilterGetOption = '//*[contains(@class,"chakra-stack")][contains(.,"換入幣種")]//option[text()="{}"]'
    FilterStatus = '//*[contains(@class,"chakra-stack")][contains(.,"狀態")]//select'
    FilterStatusOption = '//*[contains(@class,"chakra-stack")][contains(.,"狀態")]//option[text()="{}"]'
    FilterSearch = '//button[text()="查詢"]'
    RowData = '//*[@role="rowgroup"]//*[@role="row"][contains(.,"{}")][contains(.,"{}")][contains(.,"{}")]'
    Detail = '//*[text()="description"]'

    def search(self, payment="全部", get="全部", status="全部"):
        self.click(TradeHistory.FilterPayment)
        self.click(TradeHistory.FilterPaymentOption.format(payment))
        self.click(TradeHistory.FilterGet)
        self.click(TradeHistory.FilterGetOption.format(get))
        self.click(TradeHistory.FilterStatus)
        self.click(TradeHistory.FilterStatusOption.format(status))
        self.click(TradeHistory.FilterSearch)
