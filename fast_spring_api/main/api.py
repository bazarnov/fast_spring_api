# FastSpringAPI Base


from abc import ABC
from typing import Any, Mapping
from pyparsing import abstractmethod

import requests

from fast_spring_api.main.logger import FastSpringLogger
from fast_spring_api.main.auth import FastSpringAuth

class FastSpringAPI(ABC):
        
    def __init__(self, auth: FastSpringAuth):
        self.auth = auth.get_auth_header()
        self.logger = FastSpringLogger()
    
    @property
    def _base_url(self) -> str:
        return "https://api.fastspring.com"
    
    @property
    @abstractmethod
    def endpoint(self) -> str:
        """Endpoint Path"""
    
    @property
    def _headers(self) -> Mapping[str, Any]:
        """
        Authentication Headers
        """
        headers = {'Content-Type': 'application/json'}
        if not self.auth:
            self.logger.error("Authorization is not provided.")
        else:
            headers.update(self.auth)
            return headers
        
    def _send_post_request(self, payload: Mapping[str, Any]) -> requests.Response:
        """
        @ payload: the list of JSON formated params to send to the endpoint
        """
        url = f"{self._base_url}/{self.endpoint}/"
        response = requests.post(url=url, headers=self._headers, json=payload)
        self._parse_response(response)
            
    def _parse_response(self, response: requests.Response) -> Mapping[str, Any]:
        pased_response = response.json().get(self.endpoint)
        if response.status_code == 200:
            self.logger.success(pased_response)
        else:
            self.logger.error(pased_response)
        
