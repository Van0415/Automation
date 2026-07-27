from api.login import LoginAPI
from api.common import CommonAPI


class AssetsAPI:
    def __init__(self) -> None:
        self.login_api = LoginAPI()
        self.login_api.login_and_otp_verify()

    def assets(self):
        res = self.login_api.request.get(f"{CommonAPI.URL}/wallet/assets")
        data = res.json()["data"]
        return data
