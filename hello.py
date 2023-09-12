# backpack = ['chainsaw', 'hoe', 'book', 'ladder', 'gun', 'lighter',
#             'gun', 'book', 'ladder', 'gun', 'lighter', 'gun', 'book']

# if backpack.count(item for item in backpack) > 1:
#     backpack.remove(item for item in backpack)

# print(backpack)


import os
from dotenv import load_dotenv
load_dotenv()

print({'NAME': os.environ.get('DB_NAME'),
       'HOST': os.environ.get('DB_HOST'),
       'PORT': os.environ.get('DB_PORT'),
       'USER': os.environ.get('DB_USER'),
       'PASSWORD': os.environ.get('DB_PASSWORD'),
       'OPTIONS': {'ssl': {'ca': os.environ.get('MYSQL_ATTR_SSL_CA')}}})
