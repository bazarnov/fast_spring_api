# Wrapper to FastSpring API

## Example Usage
```python
# IMPORT DEPENDENCIES
from fast_spring_api.modules.subscription import Subscription
from fast_spring_api.main.auth import FastSpringAuth

# SET THE LIST OF THE SUBS TO BE UPDATED
input_data_list: list = [
        # should fail, because subs is Canceled
        {
            "end":"2023-10-30",
            "next":"2023-10-31",
            "subscription":"7w4_gDbJQMeKotwi6pxNzA",
        },
        # should success
        {
            "end":"2023-11-30",
            "next":"2023-11-31",
            "subscription": "JgqQCVRHSYiqcd_m9IFvwA",
        },
    ]

# SET SINGLE SUBS TO BE UPDATED
input_data: dict = {
    "end":"2023-11-30",
    "next":"2023-11-31",
    "subscription": "JgqQCVRHSYiqcd_m9IFvwA",
}

# SET CREDENTIALS
## FastSpring API User
user = "user"
## FastSpring API Password
password = "password"

# AUTHENTICATE
fs_auth = FastSpringAuth(user, password)

# UPDATE SUBS using list of entities
Subscription(fs_auth).update(input_data_list)

# UPDATE SUBS using single entity
Subscription(fs_auth).update(input_data)
```