from seleniumbase import BaseCase
from page.login import Login
from page.forget_password import ForgetPassword, ResetPassword
from page.common import Common, OTP


class ForgetPasswordTest(BaseCase):
    def setUp(self):
        super().setUp()
        self.maximize_window()
        self.open(ForgetPassword.URL)

    def test_860ru9pqv(self):
        """重設密碼後24小時內禁止出金提示文案正確"""
        self.assert_text("為維護帳戶安全，重設密碼後的 24 小時內將禁止出金與提幣")

    def test_860ru9prg(self):
        """會員帳號格式錯誤，顯示提示正確"""
        self.type(ForgetPassword.Account, "wrong_format")
        self.click(ForgetPassword.Submit)
        self.assert_text("格式不符")

    def test_860ru9pxr(self):
        """會員帳號未填，無法送出"""
        Common.assert_disabled(self, ForgetPassword.Submit)

    def test_860ru9prv(self):
        """輸入不存在的會員帳號，送出後顯示提示正確"""
        self.type(ForgetPassword.Account, "not_exist@hoyabit.com")
        self.click(ForgetPassword.Submit)
        self.assert_text("無效的電子信箱或手機號碼，請重新輸入")

    def test_860ru9ptg(self):
        """返回登入導向頁面正確"""
        self.click(ForgetPassword.BackToLogin)
        self.assert_url(Login.URL)

    def test_860rygx1n(self):
        """重置密碼，設置新密碼不符合規則，無法送出"""
        ForgetPassword.send_member_account(self)
        OTP.verify(self)
        self.type(ResetPassword.SetNewPassword, "wrong_format")
        self.type(ResetPassword.ConfirmPassword, "wrong_format")
        Common.assert_disabled(self, ResetPassword.Submit)

    def test_860rygx3k(self):
        """重置密碼，再次確認未填，顯示提示正確"""
        ForgetPassword.send_member_account(self)
        OTP.verify(self)
        self.click(ResetPassword.ConfirmPassword)
        self.click(ResetPassword.SetNewPassword)
        self.assert_text("請輸入密碼")

    def test_860rygx4w(self):
        """重置密碼，再次確認與設置新密碼不一致，顯示提示正確"""
        ForgetPassword.send_member_account(self)
        OTP.verify(self)
        self.type(ResetPassword.SetNewPassword, "Inconsistent01")
        self.type(ResetPassword.ConfirmPassword, "Inconsistent02")
        self.click(ResetPassword.Submit)
        self.assert_text("密碼不一致，請再次檢查")

    def test_860rygx5t(self):
        """重置密碼，各密碼欄位右側，顯示明碼功能正常"""
        ForgetPassword.send_member_account(self)
        OTP.verify(self)
        self.click(ResetPassword.SetNewPasswordShowPassword)
        Common.assert_type_is_text(self, ResetPassword.SetNewPassword)
        self.click(ResetPassword.ConfirmPasswordShowPassword)
        Common.assert_type_is_text(self, ResetPassword.ConfirmPassword)
