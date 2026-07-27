from seleniumbase import BaseCase
from page.login import Login
from page.header import Header
from page.common import Common, OTP
from page.profile import Profile
from page.kyc_verify import KycVerify
import os
from dotenv import load_dotenv

load_dotenv()


# class KycVerifyTest(BaseCase):
#     def setUp(self):
#         super().setUp()
#         self.maximize_window()
#         Login.login_and_otp_verify(self, os.getenv("ACCOUNT_LV0"), os.getenv("PASSWORD_LV0"))
#         Header.enter_profile(self)
#         self.click(Profile.GoToKycVerify)

#     def test_860ruttk2(self):
#         """各資金密碼欄位右側，顯示明碼功能正常"""
#         self.click(KycVerify.PincodeShowPassword)
#         Common.assert_type_is_text(self, KycVerify.Pincode)
#         self.click(KycVerify.ConfirmPincodeShowPassword)
#         Common.assert_type_is_text(self, KycVerify.ConfirmPincode)

#     def test_860ruttm6(self):
#         """手機號碼輸入不符合規定的值，送出後顯示身分驗證錯誤"""
#         KycVerify.twid_verify(self, "A111111111", "0935002541")
#         OTP.verify(self)
#         self.assert_text("請再次檢查你的『身分證號碼』或『手機號碼』是否填寫正確")
