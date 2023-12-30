# env_vars are sensitive variables like passwords and tokens
# sample -> export password "db@123"

import os

print(os.getenv("password")) # using getenv calling the password

