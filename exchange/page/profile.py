from page.common import Common, OTP, MFA
from seleniumbase import BaseCase
import pyperclip
import os
from dotenv import load_dotenv

load_dotenv()


class Profile:
    URL = f"{Common.URL}/profile"
    Account = '//*[@class="chakra-offset-slide"]//*[text()="{}"]'
    Level = '//*[@class="chakra-offset-slide"]//*[contains(@class,"font-bold")][text()="{}"]'
    GoToKycVerify = '//*[text()="前往身分驗證"]'
    GoToBankBind = '//*[text()="前往銀行綁定"]'
    LevelPermission = '//*[text()="等級權限"]'
    AccountSafety = '//*[text()="帳號安全"]'
    PreferenceSetting = '//*[text()="偏好設定"]'


class VerifyLevel:
    LV1Deposit = '//*[contains(@class,"chakra-offset-slide")][contains(.,"LV1")][contains(.,"新台幣入金")][contains(.,"無法使用")]'
    LV1Withdraw = '//*[contains(@class,"chakra-offset-slide")][contains(.,"LV1")][contains(.,"新台幣出金")][contains(.,"無法使用")]'
    LV2Deposit = '//*[contains(@class,"chakra-offset-slide")][contains(.,"LV2")][contains(.,"新台幣入金")][contains(.,"1,500,000")]'
    LV2Withdraw = '//*[contains(@class,"chakra-offset-slide")][contains(.,"LV2")][contains(.,"2,000,000")][contains(.,"5,000,000")]'


class AccountSafety(BaseCase):
    LoginPasswordEdit = '//*[@class="chakra-offset-slide"][contains(.,"登入密碼")]//*[text()="更改"]'
    Password = '//*[@id="password"]'
    NewPassword = '//*[@id="new_password"]'
    ConfirmPassword = '//*[@id="new_password_confirmation"]'
    LoginPasswordSubmit = '//*[@class="chakra-offset-slide"][contains(.,"登入密碼")]//*[text()="儲存"]'
    PasswordShowPassword = '//*[@id="password"]/..//*[contains(@class,"chakra-input__right-element")]'
    NewPasswordShowPassword = '//*[@id="new_password"]/..//*[contains(@class,"chakra-input__right-element")]'
    ConfirmPasswordShowPassword = (
        '//*[@id="new_password_confirmation"]/..//*[contains(@class,"chakra-input__right-element")]'
    )
    PincodeEdit = '//*[@class="chakra-offset-slide"][contains(.,"資金密碼")]//*[text()="更改"]'
    Pincode = '//*[@id="funds_password"]'
    NewPincode = '//*[@id="new_funds_password"]'
    ConfirmPincode = '//*[@id="new_funds_password_confirmation"]'
    PincodeSubmit = '//*[@class="chakra-offset-slide"][contains(.,"資金密碼")]//*[text()="儲存"]'
    PincodeShowPassword = '//*[@id="funds_password"]/..//*[contains(@class,"chakra-input__right-element")]'
    NewPincodeShowPassword = '//*[@id="new_funds_password"]/..//*[contains(@class,"chakra-input__right-element")]'
    ConfirmPincodeShowPassword = (
        '//*[@id="new_funds_password_confirmation"]/..//*[contains(@class,"chakra-input__right-element")]'
    )
    MfaSet = '//*[@class="chakra-offset-slide"][contains(.,"雙重驗證")]//*[text()="開啟"]'
    MfaClose = '//*[@class="chakra-offset-slide"][contains(.,"雙重驗證")]//*[text()="關閉"]'
    MfaCloseConfirm = '//*[text()="確認關閉"]'
    MfaToken = '//*[text()="content_copy"]'
    MfaSubmit = '//*[@class="chakra-offset-slide"][contains(.,"雙重驗證")]//*[text()="下一步"]'
    MyDeviceView = '//*[@class="chakra-offset-slide"][contains(.,"我的裝置")]//*[text()="檢視"]'
    MyDeviceLoginTime = '(//*[@class="chakra-offset-slide"][contains(.,"我的裝置")]//td)[5]'
    MyDeviceDeleteIcon = '//*[contains(@src,"delete")]'
    RemoveDeviceSubmit = '//*[@role="dialog"][contains(.,"移除此裝置")]//*[text()="確認移除"]'
    RemoveDeviceSuccess = '//*[@role="dialog"][contains(.,"裝置已從信任列表中移除")]//*[text()="完成"]'
    LastLoginTime = '//*[@class="chakra-offset-slide"][contains(.,"最近登入")][not(contains(.,"我的裝置"))]//td'

    def edit_password(self, password, new_password="EditPassword0", confirm_password="EditPassword0"):
        self.click(AccountSafety.LoginPasswordEdit)
        self.type(AccountSafety.Password, password)
        self.type(AccountSafety.NewPassword, new_password)
        self.type(AccountSafety.ConfirmPassword, confirm_password)
        self.click(AccountSafety.LoginPasswordSubmit)

    def edit_pincode(self, pincode="123123", new_pincode="111111", confirm_pincode="111111"):
        self.click(AccountSafety.PincodeEdit)
        self.type(AccountSafety.Pincode, pincode)
        self.type(AccountSafety.NewPincode, new_pincode)
        self.type(AccountSafety.ConfirmPincode, confirm_pincode)
        self.click(AccountSafety.PincodeSubmit)

    def set_mfa(self, mfa_key=None):
        self.click(AccountSafety.MfaSet)
        self.click(AccountSafety.MfaToken)
        mfa_token = pyperclip.paste()
        mfa_key = self.get_mfa_code(mfa_token) if mfa_key is None else mfa_key
        self.click(AccountSafety.MfaSubmit)
        OTP.verify(self)
        self.sleep(1)  # 等待畫面轉變為MFA驗證
        MFA.verify(self, mfa_key)
        return mfa_token

    def close_mfa(self, mfa_token, mfa_key=None):
        self.click(AccountSafety.MfaClose)
        self.click(AccountSafety.MfaCloseConfirm)
        mfa_key = self.get_mfa_code(mfa_token) if mfa_key is None else mfa_key
        OTP.verify(self)
        self.sleep(1)  # 等待畫面轉變為MFA驗證
        MFA.verify(self, mfa_key)
        return mfa_token


class BankAccount(BaseCase):
    SelectBank = '//*[@id="bank_no"]'
    Bank = '//*[@id="react-select-2-listbox"]//*[text()="{}"]'
    SelectBankBranch = '//*[@id="bank_branch_no"]'
    BankBranch = '//*[@id="react-select-3-listbox"]//*[text()="{}"]'
    BankAccount = '//*[@id="bank_account"]'
    AccountName = '//*[@id="account_name"]'
    Pincode = '//*[@id="funds_password"]'
    ShowPincode = '//*[@id="funds_password"]/..//*[contains(@class,"chakra-input__right-element")]'
    BankAccountSubmit = '//*[text()="下一步"]'
    BankAccountConfirm = '//*[text()="送出"]'

    def bind_bank_account(self, bank, bank_branch, account, name, pincode=os.getenv("PINCODE")):
        self.click(Profile.GoToBankBind)
        self.click(BankAccount.SelectBank)
        self.click(BankAccount.Bank.format(bank))
        self.click(BankAccount.SelectBankBranch)
        self.click(BankAccount.BankBranch.format(bank_branch))
        self.type(BankAccount.BankAccount, account)
        self.type(BankAccount.AccountName, name)
        self.type(BankAccount.Pincode, pincode)
        self.click(BankAccount.BankAccountSubmit)


class PreferenceSetting(BaseCase):
    BillBind = '//*[@class="chakra-offset-slide"][contains(.,"手機載具綁定")]//*[text()="綁定"]'
    CarrierNumber = '//*[contains(@placeholder,"請輸入手機載具條碼")]'
    BillSubmit = '//*[@class="chakra-offset-slide"][contains(.,"手機載具綁定")]//*[text()="儲存"]'
    BillCancel = '//*[@class="chakra-offset-slide"][contains(.,"手機載具綁定")]//*[text()="取消綁定"]'
    BillCancelSubmit = '//div[contains(@class,"justify-center")][text()="取消綁定"]'

    def bind_bill(self, carrier="4ALH+JQ"):
        self.click(PreferenceSetting.BillBind)
        self.type(PreferenceSetting.CarrierNumber, carrier)
        self.click(PreferenceSetting.BillSubmit)
