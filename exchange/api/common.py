import requests
import os
from dotenv import load_dotenv

load_dotenv()


class CommonAPI:
    URL = f'https://apis-{os.getenv("URL")}.hoyabit.com/apis/v2'


class OTPAPI:
    def __init__(self, token=None):
        self.request = requests.session()
        self.request.headers["X-Authorization"] = token

    def verify(self, mfa_id, type_number=1, code="000000"):
        body = {"mfa_id": mfa_id, "type": type_number, "code": code}
        self.request.post(f"{CommonAPI.URL}/common/otp/verify", json=body)

    def totp_verify(self, mfa_id, code):
        body = {"mfa_id": mfa_id, "code": code}
        self.request.post(f"{CommonAPI.URL}/common/totp/verify", json=body)
