



def keyboard():
    keyboard = VkKeyboard(one_time = False)

    keyboard.add_button("Белый цвет", color = VkKeyboardColor.DEFAULT)
    keyboard.add_button("Зелёный цвет", color = VkKeyboardColor.POSITIVE)

    keyboard.add_line()

    keyboard.add_button("Красный цвет", color = VkKeyboardColor.NEGATIVE)
    keyboard.add_button("Синий цвет", color = VkKeyboardColor.PRIMARY)

    


    return keyboard.get_keyboard()

print(keyboard())





while True:
    messages = vk.method("messages.getConversations", {"count": 20, "filter":"unanswered"})
    if messages['count'] >= 1:
        id = messages["items"][0] ['last_message']['from_id']
        random_id = random.randint(1, 99999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999)
        message_text = messages['items'][0]['last_message']['text'] 
     

        if message_text.lower() == "курс":
            vk.method("messages.send", {"peer_id":id, "random_id": message_id, "message": "Привет" })
        elif message_text.lower() == 'начать':
            vk.method("messages.send", {"peer_id": id, "random_id": random_id, "message":"выбор команды","keyboard": keyboard() })

        else:
            vk.method("messages.send", {"peer_id":id, "random_id": random_id, "message": "неизвестная команда" })

