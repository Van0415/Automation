from seleniumbase import BaseCase
import os
from dotenv import load_dotenv

load_dotenv()


class Common(BaseCase):
    URL = f'https://web-canary1.{os.getenv("URL")}.hoya-cex.hoyabit.studio'
    ContainsText = '//*[contains(text(),"{}")]'
    Disabled = "{}[@disabled]"
    TypeIsText = '{}[@type="text"]'

    def assert_text_contains(self, text):
        self.assert_element(Common.ContainsText.format(text))

    def assert_disabled(self, element):
        self.assert_element(Common.Disabled.format(element))

    def assert_type_is_text(self, element):
        self.assert_element(Common.TypeIsText.format(element))


class OTP(BaseCase):
    Input0 = '//*[@data-testid="verify-input-0"]'
    Input1 = '//*[@data-testid="verify-input-1"]'
    Input2 = '//*[@data-testid="verify-input-2"]'
    Input3 = '//*[@data-testid="verify-input-3"]'
    Input4 = '//*[@data-testid="verify-input-4"]'
    Input5 = '//*[@data-testid="verify-input-5"]'
    Resend = '//*[text()="重新發送"]'

    def verify(self, otp_code="220323"):
        for otp_input in [OTP.Input0]:
            self.add_text(otp_input, otp_code)


class MFA(BaseCase):
    Input0 = '//*[@data-testid="verify-input-0"]'
    Input1 = '//*[@data-testid="verify-input-1"]'
    Input2 = '//*[@data-testid="verify-input-2"]'
    Input3 = '//*[@data-testid="verify-input-3"]'
    Input4 = '//*[@data-testid="verify-input-4"]'
    Input5 = '//*[@data-testid="verify-input-5"]'

    def verify(self, mfa_code):
        i = 0
        for mfa_input in [OTP.Input0, OTP.Input1, OTP.Input2, OTP.Input3, OTP.Input4, OTP.Input5]:
            self.add_text(mfa_input, mfa_code[i])
            i = i+1
