# Dapatkan html dengan python

import requests as re

response = re.get ('https://www.swedbank.com/')
html = response.text

print(html) 