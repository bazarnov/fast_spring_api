# subscription module

from typing import Any, Iterable, Mapping, Union

from fast_spring_api.main.api import FastSpringAPI


class Subscription(FastSpringAPI):
    
    @property
    def endpoint(self) -> str:
        return "subscriptions"
    
    @property
    def http_method(self) -> str:
        return "POST"
    
    def update(self, input_data: Union[Mapping[str, Any], Iterable[Mapping[str, Any]]]):
        if isinstance(input_data, dict):
            payload = {self.endpoint: [input_data]}
            self._send_request(payload)
        elif isinstance(input_data, list):
            for item in input_data:
                payload = {self.endpoint: [item]}
                self._send_request(payload)
        else:
            self.logger.error(f"arg: `input_data` should be either List or Dict, provided: {type(input_data)}")
            