import requests

# Requests is a HTTP library in Python.

import requests
r = requests.get('https://httpbin.org/basic-auth/user/pass', auth=('user', 'pass'))
r.status_code

r.headers['content-type']
r.encoding
r.text
r.json()

# Return image of request binary info
from PIL import Image
from io import BytesIO

i = Image.open(BytesIO(r.content))
