import telebot
from telebot import types
bot=telebot.TeleBot('5960872717:AAFOX4BgRlX4yaDpvtfZHM-KMHtC118ZwSU')
users = dict()

def empty_user(id):
    '''обнуляет пользователя'''
    global users
    users[id] = dict()
    users[id]['blum'] = 0
    users[id]['stella'] = 0
    users[id]['flora'] = 0
    users[id]['muza'] = 0
    users[id]['tekhna'] = 0
    users[id]['vedma'] = 0
    return users[id]

def create_hello_msg(username: str) -> str:
    '''
    Строит преветственную строку для заданного пользователя
    '''
    return f'Привет, {username}! давай узнаем , кто ты из феечек Винкс'

@bot.message_handler(commands=['start']) # '''запускает работу бота'''
def start(message):
    empty_user(message.from_user.id)
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("давай начнём")
    markup.add(btn1)
    bot.send_message(message.chat.id, text=create_hello_msg(message.from_user.username), reply_markup=markup)

@bot.message_handler(content_types=['text'])    #'''обрабатывает сообщения'''
def func(message):
    global users
    if message.from_user.id not in users or message.text == 'Снова':
        start(message)
        return
    us = users[message.from_user.id]
    '''обрабатывает первое сообщение и начинает тест'''
    if (message.text == "давай начнём"):
        '''оздает кнопочки для 1 вопроса'''
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Зельеваренье")
        btn2 = types.KeyboardButton("История магии")
        back = types.KeyboardButton("Магический анализ")
        markup.add(btn1, btn2, back)
        '''ыводит сообщение перед кнопочками'''
        bot.send_message(message.chat.id, text="На какое занятие ты бы ходил в Алфее: \n 1) Зельеваренье \n 2) История магии \n 3) Магический анализ", reply_markup=markup)

    elif (message.text == "Зельеваренье") or (message.text == "История магии") or (message.text == "Магический анализ") :
        '''создаёт кнопочки для 2 вопроса'''
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Всё что угодно, только не учеба")
        btn2 = types.KeyboardButton("Рисую")
        back = types.KeyboardButton("Залипаю в компухтере")
        back1 = types.KeyboardButton('слушаю музыку')
        markup.add(btn1, btn2, back, back1)
        '''пишет 2 вопрос'''
        bot.send_message(message.chat.id, text="Как проводишь свое свободное время? \n 1) Всё что угодно,"
                                               "только не учеба \n 2) Рисую \n 3)Залипаю в компухтере\n 4)слушаю музыку", reply_markup=markup)
        '''обрабатывает ответ на 1 вопрос, запускает счетчик'''
        if (message.text == 'Зельеваренье'):
            us['blum']+=1
            us['flora']+=1
        elif (message.text == 'История магии'):
            us['blum']+=1
            us['stella']+=1
        elif (message.text == 'Магический анализ'):
            us['tekhna']+=1
            us['muza']+=1

    elif (message.text == "Всё что угодно, только не учеба") or (message.text == "Рисую") or (message.text == "Залипаю в компухтере") or (message.text == "слушаю музыку") :
        '''создаёт кнопки для ответа на 3 вопрос'''
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("добрым и отзывчивым")
        btn2 = types.KeyboardButton("злым и грубым")
        back = types.KeyboardButton("умным")
        markup.add(btn1, btn2, back)
        '''задаёт 3 вопрос'''
        bot.send_message(message.chat.id, text="Каким ты видишь себя?\n 1) добрым и отзывчивым \n 2) злым и грубым \n 3)умным", reply_markup=markup)
        '''обрабатывает ответ на 2 вопрос'''
        if (message.text =='Всё что угодно, только не учеба'):
            us['stella']+=1
        elif (message.text =='Рисую'):
            us['flora']+=1
            us['blum']+=1
        elif (message.text=='Залипаю в компухтере'):
            us['tekhna']+=1
        elif (message.text =='слушаю музыку'):
            us['muza']+=1

    elif (message.text == "добрым и отзывчивым") or (message.text == "злым и грубым") or (message.text == "умным") :
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("телепатия")
        btn2 = types.KeyboardButton("телекинез")
        back = types.KeyboardButton("телепортация")
        back1 = types.KeyboardButton('понимать животных')
        markup.add(btn1, btn2, back, back1)
        bot.send_message(message.chat.id, text="Какими способностями хочешь обладать?\n 1) телепатия \n 2)"
                                               "телекинез \n 3)телепортация \n 4) понимать животных", reply_markup=markup)
        if (message.text=='добрым и отзывчивым'):
            us['blum']+=1
            us['stella']+=1
            us['flora']+=1
            us['muza']+=1
        elif (message.text=='злым и грубым'):
            us['vedma']+=100
        elif (message.text=='умным'):
            us['tekhna']+=1


    elif (message.text == "телепатия") or (message.text == "телекинез") or (message.text == "телепортация") or (message.text == "понимать животных"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("овен, скорпион, телец")
        btn2 = types.KeyboardButton("лев, козерог, рыбы")
        back = types.KeyboardButton("дева, близнецы, стрелец️")
        back1= types.KeyboardButton('водолей, рак, весы')
        markup.add(btn1, btn2, back, back1)
        bot.send_message(message.chat.id,
                             text="Какого знака зодика ты?\n 1) овен, скорпион, телец  \n 2) лев, козерог, рыбы \n 3)дева,"
                                  "близнецы, стрелец \n 4) водолей, рак, весы",
                             reply_markup=markup)
        if (message.text=='телепатия'):
            us['muza']+=1
        elif (message.text=='телекинез'):
            us['blum']+=1
            us['stella']+=1
        elif (message.text =='телепортация'):
            us['tekhna']+=1
        elif (message.text=='понимать животных'):
            us['flora']+=1

    elif (message.text == "овен, скорпион, телец") or (message.text == "лев, козерог, рыбы") or (message.text == "дева, близнецы, стрелец️") or (message.text == "водолей, рак, весы") :
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("хочу")
        markup.add(btn1)
        bot.send_message(message.chat.id, text="Хочешь узнать свой результат?", reply_markup=markup)
        if (message.text=='овен, скорпион, телец'):
            us['blum']+=1
            us['flora']+=1
        elif (message.text == 'лев, козерог, рыбы'):
            us['stella'] += 1
        elif (message.text == 'дева, близнецы, стрелец'):
            us['tekhna']+=1
        elif (message.text == 'водолей, рак, весы'):
            us['muza']+=1

    elif (message.text=='хочу'):
        if (us['vedma']<us['stella'] and us['stella'] >= us['blum'] and us['stella'] >= us['flora'] and us['stella'] >= us['tekhna'] and us['stella'] >= us['muza']):
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            btn1 = types.KeyboardButton("/start")
            markup.add(btn1)
            photo=open('stella.jpg','rb')
            bot.send_photo(message.chat.id, photo)
            bot.send_message(message.chat.id,
                             text=f"Поздравляем! Ты {us['stella']}Стелла - артистичная и творческая фея, чьи силы исходят от Солнца, Луны и звезд. Она предпочла бы бездельничать, ходить по магазинам или гулять с мальчиками, чем выполнять свои школьные задания.Она учится признавать, что любовь и дружба гораздо важнее королевской власти, моды и красоты.  ")


        elif(us['vedma'] > us['tekhna'] and us['vedma'] > us['stella'] and us['vedma'] > us['muza'] and us['vedma'] > us['blum'] and us['vedma'] > us['flora']):
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            btn1 = types.KeyboardButton("/start")
            markup.add(btn1)
            photo1 = open('ведьма.jpg', 'rb')
            bot.send_photo(message.chat.id, photo1)
            bot.send_message(message.chat.id,
                                 text=f"Ой, к сожалению, ты не феечка, а ведьма, ведь феечки злыми не бывают.")

        elif (us['blum']>=us['stella'] and us['blum']>=us['flora'] and us['blum']>=us['muza'] and us['blum']>=us['tekhna'] and us['blum']>=us['vedma']):
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            btn1 = types.KeyboardButton("/start")
            markup.add(btn1)
            photo2 = open('блум.jpg', 'rb')
            bot.send_photo(message.chat.id, photo2)
            bot.send_message(message.chat.id,
                                 text="Поздравляем! Ты Блум - храбрая, честная, щедрая и обладающая харизмой девушка,"
                                      "и по сути является неформальным лидером Клуба Винкс. К тому же она еще и самая"
                                      "сильная из фей. Блум является хранительницей силы Огненного Дракона - мощнейшей магии всех миров.")

        elif (us['flora']>=us['blum'] and us['flora']>=us['stella'] and us['flora']>=us['muza'] and us['flora']>=us['tekhna'] and us['flora']>=us['vedma']):
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            btn1 = types.KeyboardButton("/start")
            markup.add(btn1)
            photo3 = open('флора.jpg', 'rb')
            bot.send_photo(message.chat.id, photo3)
            bot.send_message(message.chat.id,

                                 text="Поздавляем, ты Флора -добрая, милая, нежная девочка, романтичная натура, студентка, на которую можно положиться, миролюбивая, легкоранимая и большая скромница. ")

        elif (us['muza']>=us['blum'] and us['muza']>=us['stella'] and us['muza']>=us['flora'] and us['muza']>=us['tekhna'] and us['muza']>=us['vedma']):
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            btn1 = types.KeyboardButton("/start")
            markup.add(btn1)
            photo4 = open('муза.jpg', 'rb')
            bot.send_photo(message.chat.id, photo4)
            bot.send_message(message.chat.id,
                                 text="Поздравляем, тф Муза - фея музыки и гармонии с планеты Мелодия.Характер: ранимый и вспыльчивый, вместе с тем - оптимистичный.")
        elif (us['tekhna']>=us['blum'] and us['tekhna']>=us['stella'] and us['tekhna']>=us['flora'] and us['tekhna']>=us['muza'] and us['tekhna']>=us['vedma']):
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            btn1 = types.KeyboardButton("/start")
            markup.add(btn1)
            photo5 = open('техна.jpg', 'rb')
            bot.send_photo(message.chat.id, photo5)
            bot.send_message(message.chat.id,
                                 text="Поздравляем, ты Техна -  просто невероятно умная фея. Она очень любит технологию и все что с ней связано. Иногда она просто с головой уходит в различные технологические моменты и тогда бывает скучной. Техна очень практична и всегда логична, иногда чересчур, ведь любовь и другие эмоции не поддаются логики")
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn = types.InlineKeyboardButton(text='Снова', callback_data='start')
        markup.add(btn)
        bot.send_message(message.chat.id, text='Хочешь ответить на вопросы снова?', reply_markup=markup)
    else:
        bot.send_message(message.chat.id,
                         text='Пожалуйста, выберите вариант ответа из меню')
if __name__ == '__main__':
    bot.polling(none_stop=True)


