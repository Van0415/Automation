from page.common import Common
from seleniumbase import BaseCase
import os
from dotenv import load_dotenv

load_dotenv()


class WithdrawCrypto(BaseCase):
    URL = f"{Common.URL}/withdraw-crypto"
    Address = '//*[@id="target_address"]'
    Name = '//*[@id="target_name"]'
    Submit = '//*[text()="繼續"]'
    Amount = '//*[@id="amount"]'
    Pincode = '//*[@id="pincode"]'
    PincodeView = '//*[@id="pincode"]/..//*[contains(@class,"chakra-input__right-element")]'
    Fee = '//*[contains(@class,"chakra-text")][text()="手續費："]'
    Confirm = '//*[text()="回到我的資產"]'

    def withdraw(self, address=os.getenv("CRYPTO_ADDRESS"), name="automation", amount=20, pincode=os.getenv("PINCODE")):
        self.type(WithdrawCrypto.Address, address)
        self.type(WithdrawCrypto.Name, name)
        self.click(WithdrawCrypto.Submit)
        self.type(WithdrawCrypto.Amount, amount)
        self.type(WithdrawCrypto.Pincode, pincode)
        self.click(WithdrawCrypto.Submit)
