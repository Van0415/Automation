from page.common import Common


class Assets:
    URL = f"{Common.URL}/assets"
    Deposit = '//button[text()="入金"]'
    Withdraw = '//button[text()="出金"]'
    WalletHistory = '//*[text()="錢包紀錄"]'
    DepositCrypto = '//*[@role="row"][contains(.,"{}")]//button[text()="入幣"]'
    WithdrawCrypto = '//*[@role="row"][contains(.,"{}")]//button[text()="提幣"]'
    MyAssetsView = '//*[@aria-label="viewable-btn"]'
    NoPermissionTooltip = '//*[contains(@aria-describedby,"tooltip")]'
