"""
Домашнее задание №1

Использование библиотек: ephem

* Установите модуль ephem
* Добавьте в бота команду /planet, которая будет принимать на вход
  название планеты на английском, например /planet Mars
* В функции-обработчике команды из update.message.text получите
  название планеты (подсказка: используйте .split())
* При помощи условного оператора if и ephem.constellation научите
  бота отвечать, в каком созвездии сегодня находится планета.

"""
import logging, ephem

from datetime import datetime

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

logging.basicConfig(format='%(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename='bot.log')




def greet_user(update, context):
    text = 'Вызван /start'
    print(text)
    update.message.reply_text("О, привет!")




def planet_pos(update, context):
    user_text = update.message.text.split()
    planet = getattr(ephem, user_text, None)(datetime.datetime.now())
    constellation = ephem.constellation(planet)[1]
    update.message.reply_text(constellation)


def talk_to_me(update, context):
   user_text = update.message.text
   print(user_text)
   update.message.reply_text(text)


def main():
    mybot = Updater("API_KEY", use_context=True)

    dp = mybot.dispatcher
    dp.add_handler(CommandHandler('start', greet_user))
    dp.add_handler(CommandHandler('planet', planet_pos))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))
  
    # logging.info("Бот запущен")
    mybot.start_polling()
    mybot.idle()



    




if __name__ == "__main__":
    main()
