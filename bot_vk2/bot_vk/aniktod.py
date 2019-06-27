import vk_api
import random 

def get_ani(id):
    TOKEN = "ffd99a39ffd99a39ffd99a3963ffb2cfb1fffd9ffd99a39a2caae634976c0251348d9d6"


    vk_session = vk_api.VkApi(token = TOKEN)
    vk = vk_session.get_api()

    posts = vk.wall.get(owner_id=id, count=10, offset=random.randint(1,500))


    ani = []


    for post in posts["items"]:
        attachment = post.get("attachments")
        if attachment and attachment[0]["type"] == "text":
            memes.append(attachment[0]["text"]["id"])
    
    return "wall{}_{}".format(id,random.choice(ani))
