import string
import random

user_name = "".join(random.sample((string.ascii_lowercase),8))
print(user_name)
user_pass = "".join(random.sample((string.ascii_lowercase+string.ascii_uppercase+string.digits+string.punctuation),8))
print(user_pass)
