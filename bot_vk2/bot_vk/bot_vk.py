import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
from vk_api.utils import get_random_id 
from memes import get_memes
from valute import get_course 

def main():
    TOKEN = "c12be4a98e9a4b2621483784265704c9a8a6d387af43864143b3646e55e7c7b312dd4dbf412cca4d2ceb6"
    
    vk_session = vk_api.VkApi(token = TOKEN)
    vk = vk_session.get_api()


    hello = """
    Привет! Я бот! Если ты напишешь мне следующие то:
    -курс доллара - Я кину курс доллара.
    -мем - Я кину тебе мем.
    -Топ-Чарт - Ты получишь топовые песни.
    -Погода - Я расскажу тебе погоду в твоём городе.
    В дальнейшем бот будет дорабатываться <З
    """

 


    longpoll = VkLongPoll(vk_session)
    for event in longpoll.listen():
        if event.type == VkEventType.MESSAGE_NEW and event.to_me:
            msg_text = event.text.lower()

            if msg_text == "мемы":
                vk.messages.send(user_id=event.user_id, random_id=get_random_id(),attachment=get_memes ("-147286578")) 
            elif msg_text == "курс доллара":
                valute_id = ["R01235"]
                valutes = [get_course(id) for id in valute_id]
                vk.messages.send(user_id=event.user_id, random_id=get_random_id(),message="\n".join(valutes) ) 

            elif msg_text == "топ-чарт":
                vk.messages.send(user_id=event.user_id, random_id=get_random_id(),message="https://music.yandex.ru/chart")

            elif msg_text == "погода":
                vk.messages.send(user_id=event.user_id, random_id=get_random_id(),message="https://yandex.ru/pogoda")



            else: 
                vk.messages.send(user_id=event.user_id, random_id=get_random_id(),message=hello ) 


main()
