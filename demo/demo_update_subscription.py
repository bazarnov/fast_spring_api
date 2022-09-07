
from fast_spring_api.subscription import Subscription
from fast_spring_api.auth import FastSpringAuth

# declare the list of subscriptions to update
input_data: list = [
        # should fail, because subs is Canceled
        {"end":"2023-10-30","next":"2023-10-31","subscription":"7w4_gDbJQMeKotwi6pxNzA"},
        # should success
        {"end":"2023-11-30","next":"2023-11-31","subscription": "JgqQCVRHSYiqcd_m9IFvwA"},
    ]

# credentials
# FastSpring API User
user = "user"
# FastSpring API Password
password = "password"

# authenticate
fs_auth = FastSpringAuth(user, password)

# update subscription
Subscription(fs_auth).update(input_data)
    