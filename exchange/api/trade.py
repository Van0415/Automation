import requests
from api.common import CommonAPI


class TradeAPI:
    def __init__(self, token) -> None:
        self.request = requests.session()
        self.request.headers["X-Authorization"] = token

    def order(self, payment=1, get=4, amount=300, _type=1):
        body = {"type": _type, "base_symbol_id": payment, "target_symbol_id": get, "amount": amount, "decimals": 0}
        res = self.request.post(f"{CommonAPI.URL}/trades/order", json=body)
        order_id = res.json()["data"]["id"]
        return order_id

    def confirm(self, order_id, _type=1):
        body = {"id": order_id, "type": _type}
        self.request.put(f"{CommonAPI.URL}/trades/order/confirm", json=body)
