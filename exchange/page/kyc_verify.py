from page.common import Common
from seleniumbase import BaseCase


class KycVerify(BaseCase):
    URL = f"{Common.URL}/kyc-verify"
    Identity = '//*[@id="identity_card"]'
    Mobile = '//*[@id="mobile"]'
    Pincode = '//*[@id="pin_code"]'
    PincodeShowPassword = '//*[@id="pin_code"]/..//*[contains(@class,"chakra-input__right-element")]'
    ConfirmPincode = '//*[@id="pin_code_confirm"]'
    ConfirmPincodeShowPassword = '//*[@id="pin_code_confirm"]/..//*[contains(@class,"chakra-input__right-element")]'
    Submit = '//*[text()="繼續"]'

    def twid_verify(self, id, mobile, pincode="111111", confirm_pincode="111111"):
        self.type(KycVerify.Identity, id)
        self.type(KycVerify.Mobile, mobile)
        self.type(KycVerify.Pincode, pincode)
        self.type(KycVerify.ConfirmPincode, confirm_pincode)
        self.click(KycVerify.Submit)
