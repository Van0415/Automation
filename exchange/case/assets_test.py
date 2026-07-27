from seleniumbase import BaseCase
from page.login import Login
from page.assets import Assets
from page.common import Common
import os
from dotenv import load_dotenv

load_dotenv()


class AssetsTest(BaseCase):
    def setUp(self):
        super().setUp()
        self.maximize_window()
        Login.login_and_otp_verify(self)
        self.open(Assets.URL)

    def test_860rvgzaf(self):
        """我的資產右側，顯示資金功能正常"""
        self.click(Assets.MyAssetsView)
        self.assert_text_not_visible("********")


# class AssetsTest_LV0(BaseCase):
#     def setUp(self):
#         super().setUp()
#         self.maximize_window()
#         Login.login_and_otp_verify(self, os.getenv("ACCOUNT_LV0"), os.getenv("PASSWORD_LV0"))
#         self.open(Assets.URL)

#     def test_860rvgzd2(self):
#         """LV.0 - 入金、出金按鈕Disable，Hover後Tooltips顯示正確"""
#         Common.assert_disabled(self, Assets.Deposit)
#         Common.assert_disabled(self, Assets.Withdraw)
#         self.hover(Assets.Deposit)
#         self.assert_element(Assets.NoPermissionTooltip)
#         self.hover(Assets.Withdraw)
#         self.assert_element(Assets.NoPermissionTooltip)

#     def test_860rvh5j6(self):
#         """LV.0 - 入幣、提幣、買賣按鈕Disable，Hover後Tooltips顯示正確"""
#         Common.assert_disabled(self, Assets.DepositCrypto.format("USDT"))
#         Common.assert_disabled(self, Assets.WithdrawCrypto.format("USDT"))
#         self.hover(Assets.DepositCrypto.format("USDT"))
#         self.assert_element(Assets.NoPermissionTooltip)
#         self.hover(Assets.WithdrawCrypto.format("USDT"))
#         self.assert_element(Assets.NoPermissionTooltip)


# class AssetsTest_LV1(BaseCase):
#     def setUp(self):
#         super().setUp()
#         self.maximize_window()
#         Login.login_and_otp_verify(self, os.getenv("ACCOUNT_LV1"), os.getenv("PASSWORD_LV1"))
#         self.open(Assets.URL)

#     def test_860rvgzda(self):
#         """LV.1 - 入金、出金按鈕Disable，Hover後Tooltips顯示正確"""
#         Common.assert_disabled(self, Assets.Deposit)
#         Common.assert_disabled(self, Assets.Withdraw)
#         self.hover(Assets.Deposit)
#         self.assert_element(Assets.NoPermissionTooltip)
#         self.hover(Assets.Withdraw)
#         self.assert_element(Assets.NoPermissionTooltip)
