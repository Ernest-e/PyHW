import telebot
from telebot import types
from random import randint
from random import choice

bot = telebot.TeleBot("5832412002:AAGFELT3j3-lMoWJxXzRyPWwN7SGvUhBysQ")

quantity = 117
max_grab = 28
game = False


def handle_game_proc(message):
    global game
    if game and 1 <= int(message.text) <= 28:
        return True
    else:
        return False

    
def handle_game_warning(message):
    global game
    if game and (28 < int(message.text) or int(message.text) < 1):
        return True
    else:
        return False


@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, """Привет, это игра бот для игры в конфеты.
    Правила игры: На столе лежит 117 конфета.
    Играют два игрока делая ход друг после друга. За один ход можно забрать не более чем 28 конфет.
    Все конфеты оппонента достаются сделавшему последний ход.""")
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("/Go")
    btn2 = types.KeyboardButton("/Stop")
    markup.add(btn1, btn2)
    bot.send_message(message.chat.id,'Нажмите Go, чтобы начать',reply_markup=markup)


@bot.message_handler(commands=['Go'])
def go(message):
    global quantity, max_grab, game
    game = True
    quantity = 117
    bot.reply_to(message, "Начинаем")
    turn = choice(['Bot', 'User'])
    bot.send_message(message.chat.id, f'Начинает {turn}')
    if turn == 'Bot':
        grab = randint(1, max_grab)
        quantity -= grab
        bot.send_message(message.chat.id, f'Бот взял {grab}')
        bot.send_message(message.chat.id,
                        f'Осталось {quantity}')
        bot.send_message(message.chat.id, 'Ход игрока. Сколько конфет взять?')
    

@bot.message_handler(commands=['Stop'])
def stop(message):
    global quantity, max_grab, game
    game = False
    bot.send_message(message.chat.id, 'Остановка игры')




@bot.message_handler(func=handle_game_proc)
def gamePvB (message):
    global quantity, max_grab, game
    if game:
        if quantity > 28:
            user_grab = int(message.text)        
            quantity -= user_grab
            bot.send_message(message.chat.id, f'Осталось {quantity}')

            if quantity > 28:
                grab = randint(1, max_grab)
                bot.send_message(message.chat.id, f'Бот берет {grab} конфет')
                quantity -= grab
                bot.send_message(message.chat.id, f'Осталось {quantity}')

                if quantity <28:
                    bot.send_message(message.chat.id, 'Выиграл пользователь')
                    quantity = 0
                    game = False
                else:
                    bot.send_message(message.chat.id, 'Ход игрока. Сколько конфет взять?')
            else:
                bot.send_message(message.chat.id, 'Выиграл бот')
                quantity = 0
                game = False
        else:
            bot.send_message(message.chat.id, 'Выиграл пользователь')
            quantity = 0
            game = False




@bot.message_handler(func=handle_game_warning)
def gameWarning (message):
    bot.send_message(message.chat.id, 'Необходимо выбрать от 1 до 28 конфет')






bot.infinity_polling()
