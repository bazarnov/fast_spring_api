# accounts module

from typing import Any, Mapping
from fast_spring_api.main.api import FastSpringAPI


class UpdateAccounts(FastSpringAPI):
    
    @property
    def endpoint(self) -> str:
        return "accounts"
    
    @property
    def http_method(self) -> str:
        return "POST"
    
    def update(self, id: str, input_data: Mapping[str, Any]):
        payload = {"contact": input_data}
        return self._send_request(payload, id)
            