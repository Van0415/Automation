from page.common import Common
from seleniumbase import BaseCase
import os
from dotenv import load_dotenv

load_dotenv()


class Withdraw(BaseCase):
    URL = f"{Common.URL}/withdrawal-fiat"
    Amount = '//*[@id="amount"]'
    Pincode = '//*[@id="pin_code"]'
    PincodeView = '//*[@id="pin_code"]/..//*[contains(@class,"chakra-input__right-element")]'
    TotalAmount = '//*[contains(@class,"font-bold")][text()="{}"]'
    Submit = '//*[text()="繼續"]'
    Finish = '//*[text()="完成"]'

    def withdraw(self, amount=100, pincode=os.getenv("PINCODE")):
        self.type(Withdraw.Amount, amount)
        self.type(Withdraw.Pincode, pincode)
        self.click(Withdraw.Submit)
