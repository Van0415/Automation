from page.common import Common
from seleniumbase import BaseCase


class WalletHistory(BaseCase):
    URL = f"{Common.URL}/assets/wallet-history"
    CryptoTender = '//*[text()="加密貨幣"]'
    FiatTender = '//*[text()="法定貨幣"]'
    FilterCurrency = '//*[contains(@class,"chakra-stack")][contains(.,"幣種")]//select'
    FilterCurrencyOption = '//*[contains(@class,"chakra-stack")][contains(.,"幣種")]//option[text()="{}"]'
    FilterType = '//*[contains(@class,"chakra-stack")][contains(.,"類型")]//select'
    FilterTypeOption = '//*[contains(@class,"chakra-stack")][contains(.,"類型")]//option[text()="{}"]'
    FilterStatus = '//*[contains(@class,"chakra-stack")][contains(.,"狀態")]//select'
    FilterStatusOption = '//*[contains(@class,"chakra-stack")][contains(.,"狀態")]//option[text()="{}"]'
    FilterSearch = '//button[text()="查詢"]'
    RowData = '//*[@role="rowgroup"]//*[@role="row"][contains(.,"{}")][contains(.,"{}")][contains(.,"{}")]'
    Detail = '//*[text()="description"]'

    def search(self, currency="全部", _type="提幣", status="全部"):
        self.click(WalletHistory.FilterCurrency)
        self.click(WalletHistory.FilterCurrencyOption.format(currency))
        self.click(WalletHistory.FilterType)
        self.click(WalletHistory.FilterTypeOption.format(_type))
        self.click(WalletHistory.FilterStatus)
        self.click(WalletHistory.FilterStatusOption.format(status))
        self.click(WalletHistory.FilterSearch)
