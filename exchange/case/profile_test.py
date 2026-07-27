from seleniumbase import BaseCase
from api.login import LoginAPI
from api.profile import ProfileAPI
from api.common import OTPAPI
from page.login import Login
from page.header import Header
from page.profile import Profile, VerifyLevel, AccountSafety, BankAccount, PreferenceSetting
from page.common import Common, OTP, MFA
from page.assets import Assets
from page.withdraw import Withdraw
from datetime import datetime, timedelta
import os
from dotenv import load_dotenv

load_dotenv()


class ProfileTest(BaseCase):
    def setUp(self):
        super().setUp()
        self.maximize_window()
        Login.login_and_otp_verify(self)
        Header.enter_profile(self)

    def test_860rutrnh(self):
        """會員等級、帳號顯示正確"""
        self.assert_element(Profile.Account.format(os.getenv("ACCOUNT")))
        self.assert_element(Profile.Level.format("LV2"))

    def test_860rutrp5(self):
        """目前權限為加密貨幣交易、日日生幣、新台幣交易"""
        for text in ["個人權限", "加密貨幣交易", "日日生幣", "新台幣交易"]:
            self.assert_text(text)

    def test_860rutujp(self):
        """最高等級為LV2"""
        self.click(Profile.LevelPermission)
        self.assert_text_not_visible("LV3")

    def test_860rutvrd(self):
        """目前密碼錯誤，修改失敗"""
        self.click(Profile.AccountSafety)
        AccountSafety.edit_password(self, "WrongPassword0")
        self.assert_text("變更密碼失敗，請檢查舊密碼是否正確或新密碼是否符合規則")

    def test_860rutvt3(self):
        """新密碼與確認新密碼不一致，修改失敗"""
        self.click(Profile.AccountSafety)
        AccountSafety.edit_password(self, os.getenv("PASSWORD"), "Inconsistent01")
        self.assert_text("密碼不一致")

    def test_860rutvtx(self):
        """各密碼欄位右側，顯示明碼功能正常"""
        self.click(Profile.AccountSafety)
        self.click(AccountSafety.LoginPasswordEdit)
        self.click(AccountSafety.PasswordShowPassword)
        Common.assert_type_is_text(self, AccountSafety.Password)
        self.click(AccountSafety.NewPasswordShowPassword)
        Common.assert_type_is_text(self, AccountSafety.NewPassword)
        self.click(AccountSafety.ConfirmPasswordShowPassword)
        Common.assert_type_is_text(self, AccountSafety.ConfirmPassword)

    def test_860rutw38(self):
        """目前資金密碼錯誤，修改失敗"""
        self.click(Profile.AccountSafety)
        AccountSafety.edit_pincode(self, "666666")
        self.assert_text("資金密碼錯誤")

    def test_860rutw3p(self):
        """新資金密碼與確認新資金密碼不一致，修改失敗"""
        self.click(Profile.AccountSafety)
        AccountSafety.edit_pincode(self, new_pincode="666666")
        self.assert_text("密碼不一致")

    def test_860rutw4d(self):
        """各密碼欄位右側，顯示明碼功能正常"""
        self.click(Profile.AccountSafety)
        self.click(AccountSafety.PincodeEdit)
        self.click(AccountSafety.PincodeShowPassword)
        Common.assert_type_is_text(self, AccountSafety.Pincode)
        self.click(AccountSafety.NewPincodeShowPassword)
        Common.assert_type_is_text(self, AccountSafety.NewPincode)
        self.click(AccountSafety.ConfirmPincodeShowPassword)
        Common.assert_type_is_text(self, AccountSafety.ConfirmPincode)

    def test_860rutwer(self):
        """設定時，雙重驗證碼輸入錯誤，設定失敗"""
        self.click(Profile.AccountSafety)
        AccountSafety.set_mfa(self, "000000")
        self.assert_text("驗證碼錯誤")

    def test_860rutwqd(self):
        """已登入過的裝置會顯示於頁面上"""
        time_local = datetime.now()
        self.click(Profile.AccountSafety)
        self.click(AccountSafety.MyDeviceView)
        time_login = self.get_text(AccountSafety.MyDeviceLoginTime)
        time_login = datetime.strptime(time_login, "%Y/%m/%d %H:%M:%S")
        assert time_local - timedelta(seconds=60) < time_login < time_local + timedelta(seconds=60)

    def test_860rutwrq(self):
        """點擊右側垃圾桶圖示可刪除裝置，並使當下使用該裝置登入的帳號被登出"""
        self.click(Profile.AccountSafety)
        self.click(AccountSafety.MyDeviceView)
        self.click(AccountSafety.MyDeviceDeleteIcon)
        self.click(AccountSafety.RemoveDeviceSubmit)
        self.click(AccountSafety.RemoveDeviceSuccess)
        self.assert_url(Login.URL)

    def test_860rutwze(self):
        """登入資訊顯示正確"""
        time_local = datetime.now()
        self.click(Profile.AccountSafety)
        time_login = self.get_text(AccountSafety.LastLoginTime)
        time_login = datetime.strptime(time_login, "%Y/%m/%d %H:%M:%S")
        assert time_local - timedelta(seconds=60) < time_login < time_local + timedelta(seconds=60)

    def test_860rutx20(self):
        """銀行帳戶綁定資訊顯示正確"""
        for text in ["銀行帳戶綁定", "銀行", "分行", "帳號"]:
            self.assert_text(text)

    def test_860rutxpr(self):
        """綁定載具成功"""
        self.click(Profile.PreferenceSetting)
        try:
            self.click(PreferenceSetting.BillCancel, timeout=1)
            self.click(PreferenceSetting.BillCancelSubmit)
        except:
            pass
        PreferenceSetting.bind_bill(self)
        self.assert_text("手機載具條碼綁定成功")
        self.assert_text("已綁定載具：/4ALH+JQ")

    def test_860rutuvg(self):
        """LV1擁有權限，新台幣入出金顯示無法使用"""
        self.click(Profile.LevelPermission)
        self.assert_element(VerifyLevel.LV1Deposit)
        self.assert_element(VerifyLevel.LV1Withdraw)

    def test_860rutuwm(self):
        """LV2擁有權限，新台幣入出金顯示金額正確"""
        self.click(Profile.LevelPermission)
        self.assert_element(VerifyLevel.LV2Deposit)
        self.assert_element(VerifyLevel.LV2Withdraw)


# class ProfileTest_LV0(BaseCase):
#     def setUp(self):
#         super().setUp()
#         self.maximize_window()
#         Login.login_and_otp_verify(self, os.getenv("ACCOUNT_LV0"), os.getenv("PASSWORD_LV0"))
#         Header.enter_profile(self)

#     def test_860ruttd0(self):
#         """無法前往銀行綁定"""
#         Common.assert_disabled(self, Profile.GoToBankBind)


# class ProfileTest_LV1(BaseCase):
#     def setUp(self):
#         super().setUp()
#         self.maximize_window()
#         Login.login_and_otp_verify(self, os.getenv("ACCOUNT_LV1"), os.getenv("PASSWORD_LV1"))
#         Header.enter_profile(self)

#     def test_860rutu7g(self):
#         """個人權限為加密貨幣交易、日日生幣"""
#         for text in ["個人權限", "加密貨幣交易", "日日生幣"]:
#             self.assert_text(text)

#     def test_860rutxa6(self):
#         """開戶銀行可下拉選擇各個銀行"""
#         self.click(Profile.GoToBankBind)
#         self.click(BankAccount.SelectBank)
#         self.click(BankAccount.Bank.format("004 臺灣銀行"))
#         self.assert_text("004 臺灣銀行")

#     def test_860rutxcb(self):
#         """開戶分行依據選擇的銀行，可選擇該銀行之分行"""
#         self.click(Profile.GoToBankBind)
#         self.click(BankAccount.SelectBankBranch)
#         self.assert_element_not_visible(BankAccount.BankBranch.format("0037 營業部"))
#         self.click(BankAccount.SelectBank)
#         self.click(BankAccount.Bank.format("004 臺灣銀行"))
#         self.click(BankAccount.SelectBankBranch)
#         self.assert_element(BankAccount.BankBranch.format("0037 營業部"))

#     def test_860rutxed(self):
#         """資金密碼驗證輸入錯誤密碼，送出後錯誤"""
#         BankAccount.bind_bank_account(self, "004 臺灣銀行", "0037 營業部", "123123123", "automation", "111111")
#         self.click(BankAccount.BankAccountConfirm)
#         self.assert_text("資金密碼錯誤")

#     def test_860rutxfd(self):
#         """資金密碼驗證右側，顯示明碼功能正常"""
#         self.click(Profile.GoToBankBind)
#         self.click(BankAccount.ShowPincode)
#         Common.assert_type_is_text(self, BankAccount.Pincode)

#     def test_860rutxge(self):
#         """確認送出視窗，檢視資訊顯示正確"""
#         BankAccount.bind_bank_account(self, "004 臺灣銀行", "0037 營業部", "123123123", "automation")
#         for text in ["004 臺灣銀行", "0037 營業部", "123123123", "automation"]:
#             self.assert_text(text)


# class ProfileTest_EDPW(BaseCase):
#     def setUp(self):
#         super().setUp()
#         self.maximize_window()
#         Login.login_and_otp_verify(self, os.getenv("ACCOUNT_EDPW"), os.getenv("PASSWORD_EDPW"))
#         Header.enter_profile(self)

#     def tearDown(self):
#         login_api = LoginAPI()
#         token = login_api.login_and_otp_verify(os.getenv("ACCOUNT_EDPW"), "EditPassword0")
#         profile_api = ProfileAPI(token)
#         otp_api = OTPAPI(token)

#         mfa_id = profile_api.edit_password("EditPassword0", os.getenv("PASSWORD_EDPW"))
#         otp_api.verify(mfa_id)
#         profile_api.edit_password_confirm(mfa_id)
#         super().tearDown()

#     def test_860rutvku(self):
#         """修改成功，可以新密碼登入"""
#         self.click(Profile.AccountSafety)
#         AccountSafety.edit_password(self, os.getenv("PASSWORD_EDPW"))
#         OTP.verify(self)
#         self.assert_text("請重新登入")
#         Login.login_and_otp_verify(self, os.getenv("ACCOUNT_EDPW"), "EditPassword0")
#         self.assert_url(Assets.URL)

#     def test_860rutvmd(self):
#         """修改成功，無法以舊密碼登入"""
#         self.click(Profile.AccountSafety)
#         AccountSafety.edit_password(self, os.getenv("PASSWORD_EDPW"))
#         OTP.verify(self)
#         self.assert_text("請重新登入")
#         Login.login(self, os.getenv("ACCOUNT_EDPW"), os.getenv("PASSWORD_EDPW"))
#         Common.assert_text_contains(self, "帳號或密碼不相符")

#     def test_860rutvv7(self):
#         """修改成功，24小時內，無法出金與提幣"""
#         self.click(Profile.AccountSafety)
#         AccountSafety.edit_password(self, os.getenv("PASSWORD_EDPW"))
#         OTP.verify(self)
#         self.assert_text("請重新登入")
#         Login.login_and_otp_verify(self, os.getenv("ACCOUNT_EDPW"), "EditPassword0")
#         self.click(Assets.Withdraw)
#         Withdraw.withdraw(self)
#         self.assert_text("為維護帳戶安全性，修改密碼後的 24 小時將暫時禁止出金/提幣")


# class ProfileTest_MFA(BaseCase):
#     @classmethod
#     def setUpClass(cls):
#         cls.login_api = LoginAPI()
#         token = cls.login_api.login_and_otp_verify(os.getenv("ACCOUNT_MFA"), os.getenv("PASSWORD_MFA"))
#         cls.profile_api = ProfileAPI(token)
#         cls.otp_api = OTPAPI(token)

#     def setUp(self):
#         super().setUp()
#         self.maximize_window()
#         Login.login_and_otp_verify(self, os.getenv("ACCOUNT_MFA"), os.getenv("PASSWORD_MFA"))
#         Header.enter_profile(self)

#     def tearDown(self):
#         mfa_id = self.profile_api.close_mfa()
#         self.otp_api.verify(mfa_id)
#         mfa_key = self.get_mfa_code(self.mfa_token)
#         self.otp_api.totp_verify(mfa_id, mfa_key)
#         self.profile_api.close_mfa_confirm(mfa_id)
#         super().tearDown()

#     def test_860rutwd8(self):
#         """設定成功，登入時會以雙重驗證取代OTP驗證，且可成功登入"""
#         self.click(Profile.AccountSafety)
#         self.mfa_token = AccountSafety.set_mfa(self)
#         Header.logout(self)
#         Login.login(self, os.getenv("ACCOUNT_MFA"), os.getenv("PASSWORD_MFA"))
#         mfa_key = self.get_mfa_code(self.mfa_token)
#         MFA.verify(self, mfa_key)
#         self.assert_url(Assets.URL)

#     def test_860rutwdz(self):
#         """設定成功，登入時輸入錯誤雙重驗證碼，登入失敗"""
#         self.click(Profile.AccountSafety)
#         self.mfa_token = AccountSafety.set_mfa(self)
#         Header.logout(self)
#         Login.login(self, os.getenv("ACCOUNT_MFA"), os.getenv("PASSWORD_MFA"))
#         MFA.verify(self, "000000")
#         self.assert_text("驗證碼錯誤")

#     def test_860rutwhc(self):
#         """已開啟時，可關閉功能，登入時變回OTP驗證"""
#         self.click(Profile.AccountSafety)
#         self.mfa_token = AccountSafety.set_mfa(self)
#         AccountSafety.close_mfa(self, self.mfa_token)
#         Header.logout(self)
#         Login.login_and_otp_verify(self, os.getenv("ACCOUNT_MFA"), os.getenv("PASSWORD_MFA"))
#         self.assert_url(Assets.URL)

#     def test_860rutwhv(self):
#         """關閉功能時，輸入錯誤雙重驗證碼，關閉失敗"""
#         self.click(Profile.AccountSafety)
#         self.mfa_token = AccountSafety.set_mfa(self)
#         AccountSafety.close_mfa(self, self.mfa_token, "000000")
#         self.assert_text("驗證碼錯誤")
