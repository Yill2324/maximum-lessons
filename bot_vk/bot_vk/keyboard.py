from vk_api.keyboard import VkKeyboard, VkKeyboardColor



def keyboard():
    keyboard = VkKeyboard(one_time = False)

    keyboard.add_button("мемы", color = VkKeyboardColor.DEFAULT)
    keyboard.add_button("мызыка", color = VkKeyboardColor.POSITIVE)

    keyboard.add_line()

    keyboard.add_button("Красный цвет", color = VkKeyboardColor.NEGATIVE)
    keyboard.add_button("Синий цвет", color = VkKeyboardColor.PRIMARY)

    


    return keyboard.get_keyboard()
