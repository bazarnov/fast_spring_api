# FastSpring Auth

import base64
import requests
from typing import Mapping, Union

from fast_spring_api.main.logger import FastSpringLogger


class FastSpringAuth:
    
    def __init__(
        self, 
        user: str = None,
        password: str = None,
    ):
        """
        @ user: FastSpring API username
        @ password: FastSpring API password
        """
        self.logger: FastSpringLogger = FastSpringLogger()
        self.user = user
        self.password = password
        self.check: bool = self._check_connection()
        if self.check:
            self.auth_header = self.get_auth_header()
    
    def _check_connection(self):
        """
        Check whether credentials are valid by requesting the Accounts endpoint.
        """
        url = "https://api.fastspring.com/accounts"
        try:
            response = requests.get(url=url, headers=self.get_auth_header())
            response.raise_for_status()
            return True
        except requests.exceptions.HTTPError as e:
            self.logger.error(f"Connection failed, more info: {e}")
            return False
    
    def get_auth_header(self) -> Union[Mapping[str, str], Mapping]:
        """
        Returns Base64 Authentication Header from user:password pair.
        """
        token = None
        
        if self.user and self.password:
            auth_string = f"{self.user}:{self.password}".encode("utf8")
            token = base64.b64encode(auth_string).decode("utf8")
                     
        return {'Authorization': f'Basic {token}'} if token else {}
    
    