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

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

logging.basicConfig(format='%(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename='bot.log')




def greet_user(update, context):
    text = 'Вызван /start'
    print(text)
    update.message.reply_text("О, привет!")


def talk_to_me(update, context):
    user_text = update.message.text
    print(user_text)
    update.message.reply_text(text)

def planet_pos(update, context):
    planets = {
        'Mercury': ephem.Mercury(),
        'Venus': ephem.Venus(),
        'Mars': ephem.Mars(),
        'Jupiter': ephem.Jupiter(),
        'Saturn': ephem.Saturn(),
        'Neptune': ephem.Neptune()
    }

    user_text = update.message.text
    planet_name = user_text.split(' ')
    from datatime import date
    now = date.today()
    if planet_name in planets.keys():
        planet_p = planets.get(planet_name)
        planet_p.cumpute(now)
        constellation = ephem.constellation()
        return update.message.reply_text(planet_name)(constellation)
    else:
        return update.message.reply_text()
    



def main():
    mybot = Updater("API_KEY", use_context=True)

    dp = mybot.dispatcher
    dp.add_handler(CommandHandler('planet', planet_pos))
  
    logging.info("Бот запущен")
    mybot.start_polling()
    mybot.idle()



    




if __name__ == "__main__":
    main()
