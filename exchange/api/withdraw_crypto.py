import requests
from api.common import CommonAPI
import os
from dotenv import load_dotenv

load_dotenv()


class WithdrawCryptoAPI:
    def __init__(self, token) -> None:
        self.request = requests.session()
        self.request.headers["X-Authorization"] = token

    def withdraw(self, address, name="automation", amount=20, pincode=os.getenv("PINCODE")):
        body = {
            "symbol_id": 4,
            "blockchain_protocol_id": 2,
            "target_address": address,
            "target_name": name,
            "amount": amount,
            "fee": 2,
            "decimals": 0,
            "pin_code": pincode,
        }
        res = self.request.post(f"{CommonAPI.URL}/wallet/cryptos/withdraw", json=body)
        mfa_id = res.json()["data"]["mfa_id"]
        return mfa_id

    def withdraw_confirm(self, mfa_id):
        body = {"mfa_id": mfa_id}
        self.request.post(f"{CommonAPI.URL}/wallet/cryptos/withdraw/confirm", json=body)
