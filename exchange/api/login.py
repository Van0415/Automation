import requests
from api.common import CommonAPI, OTPAPI
import os
from dotenv import load_dotenv

load_dotenv()


class LoginAPI:
    def __init__(self):
        self.request = requests.session()

    def email_login(self, account, password):
        body = {"email": account, "password": password}
        res = self.request.post(f"{CommonAPI.URL}/user/email-login", json=body)
        mfa_id = res.json()["data"]["mfa_id"]
        return mfa_id

    def confirm(self, mfa_id):
        body = {"mfa_id": mfa_id}
        res = self.request.post(f"{CommonAPI.URL}/user/login/confirm", json=body)
        token = res.json()["data"]["token"]
        return token

    def login_and_otp_verify(self, account=os.getenv("ACCOUNT"), password=os.getenv("PASSWORD")):
        otp_api = OTPAPI()
        mfa_id = self.email_login(account, password)
        otp_api.verify(mfa_id)
        token = self.confirm(mfa_id)
        return token
