# IMPORT DEPENDENCIES
from fast_spring_api.modules.accounts import UpdateAccounts
from fast_spring_api.main.auth import FastSpringAuth


# account ids are stored in file for convinience
with open("~/accounts.json", "r") as input_file:
    # local import
    import json
    
    accounts = json.load(input_file).get("accounts")
    all_accounts_to_update = len(accounts)


# SET CREDENTIALS

## FastSpring API User
user = "api_user"
## FastSpring API Password
password = "api_passowrd"

# AUTHENTICATE
fs_auth = FastSpringAuth(user, password)

# REPLACE `Phone` for each account listed in the file
processed_number = all_accounts_to_update
for account in accounts:
    UpdateAccounts(fs_auth).update(id = account.get("account"), input_data = {"phone": "non-available"})
    processed_number =- 1
    print(f"Progress: {processed_number}/{all_accounts_to_update}")
   