from page.common import Common
from seleniumbase import BaseCase


class Deposit(BaseCase):
    URL = f"{Common.URL}/deposit-fiat"
    BankAccount = '//*[contains(@class,"chakra-input__group")]//input'
    CopyBankAccount = '//*[text()="content_copy"]'
