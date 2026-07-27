import requests
from api.common import CommonAPI


class ProfileAPI:
    def __init__(self, token) -> None:
        self.request = requests.session()
        self.request.headers["X-Authorization"] = token

    def edit_password(self, password, new_password):
        body = {"old_password": password, "new_password": new_password}
        res = self.request.post(f"{CommonAPI.URL}/user/password/update", json=body)
        mfa_id = res.json()["data"]["mfa_id"]
        return mfa_id

    def edit_password_confirm(self, mfa_id):
        body = {"mfa_id": mfa_id}
        self.request.put(f"{CommonAPI.URL}/user/password/update/confirm", json=body)

    def close_mfa(self):
        res = self.request.post(f"{CommonAPI.URL}/user/totp/unbinding")
        mfa_id = res.json()["data"]["mfa_id"]
        return mfa_id

    def close_mfa_confirm(self, mfa_id):
        body = {"mfa_id": mfa_id}
        self.request.post(f"{CommonAPI.URL}/user/totp/unbinding/confirm", json=body)
