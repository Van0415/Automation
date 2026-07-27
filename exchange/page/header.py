from seleniumbase import BaseCase


class Header(BaseCase):
    TransferMoney = '//*[text()="轉帳"]'
    Deposit = '//*[@role="dialog"]//button[text()="入金"]'
    Withdraw = '//*[@role="dialog"]//button[text()="出金"]'
    CryptosDeposit = '//*[@role="dialog"]//button[text()="入幣"]'
    CryptosWithdraw = '//*[@role="dialog"]//button[text()="提幣"]'
    Account = '//*[@aria-haspopup="dialog"]//*[@role="img"]'
    Profile = '//*[text()="會員中心"]'
    Logout = '//*[text()="登出"]'

    def logout(self):
        self.click(Header.Account)
        self.click(Header.Logout)

    def enter_profile(self):
        self.click(Header.Account)
        self.click(Header.Profile)
