# FastSpringAPI Base


from abc import ABC
from typing import Any, Mapping
from pyparsing import abstractmethod

import requests

from fast_spring_api.main.logger import FastSpringLogger
from fast_spring_api.main.auth import FastSpringAuth
from fast_spring_api.main.exceptions import AuthError

class FastSpringAPI(ABC):
        
    def __init__(self, auth: FastSpringAuth):
        self.auth = auth.auth_header if auth.check else {}
        self.logger = FastSpringLogger()
        if not self.auth:
            self.logger.fatal("Unnable to Authenticate the request, please check credentials.")
            raise AuthError
        
    @property
    def _base_url(self) -> str:
        return "https://api.fastspring.com"
    
    @property
    @abstractmethod
    def endpoint(self) -> str:
        """Endpoint Path"""
    
    @property
    @abstractmethod
    def http_method(self) -> str:
        """GET, POST, PUT, DELETE"""
    
    @property
    def _headers(self) -> Mapping[str, Any]:
        return {'Content-Type': 'application/json', "accept": "application/json", **self.auth}
    
    def _request_kwargs(
        self, 
        url: str, 
        headers: Mapping[str, Any], 
        json: Mapping[str, Any] = None, 
        data: Mapping[str, Any] = None,
    ) -> Mapping[str, Any]:
        
        request_kwargs = {
            "method": self.http_method, 
            "url": url, 
            "headers": headers,
        }
        if json:
            request_kwargs.update({"json": json})
        if data:
            request_kwargs.update({"data": data})
            
        return request_kwargs
    
    def _send_request(self, payload: Mapping[str, Any], id: str = None):
        """
        @ payload: the list of JSON formated params to send to the endpoint
        """
        url = f"{self._base_url}/{self.endpoint}/"
        if id:
            url = url + id
        request_kwargs = self._request_kwargs(url, self._headers, payload)
        response = requests.request(**request_kwargs)
        if self.http_method == "POST":
            self._get_post_request_result(response)
        else:
            raise NotImplementedError(f"HTTP_METHOD: {self.http_method} was used, but the result could not be parsed, because it's not implemented.")
           
    def _get_post_request_result(self, response: requests.Response):
        if response.status_code == 200:
            result = response.json().get(self.endpoint)
            self.logger.success(result)
        elif response.status_code == 400:
            result = response.json().get(self.endpoint)
            self.logger.error(result)
        else:
            status = response.status_code
            reason = str(response.reason)
            self.logger.error(f'Status: {status}, Reason: {reason}')
