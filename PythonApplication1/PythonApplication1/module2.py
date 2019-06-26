import json

str = '{"Hi":["python", "py", 2]}'

jsoneDate = json.dumps(str)


print(jsoneDate)


import vk_api
import time
import random 

from vk_api.keyboard import VkKeyboard, VkKeyboardColor

from module1 import * 


token = "bef13dbdbef13dbdbef13dbd14be9a767dbbef1bef13dbde3e1a110f5593b26fec23961"


vk = vk_api.VkApi(token = token)  



vk._auth_token() 


posts = vk.method("wall.get", {"owner_id": "-183679641", "offset": "1", "count": "99" })

print(posts['items'][0]['text'])