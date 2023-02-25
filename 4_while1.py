"""

Домашнее задание №1

Цикл while: hello_user

* Напишите функцию hello_user(), которая с помощью функции input() спрашивает 
  пользователя “Как дела?”, пока он не ответит “Хорошо”
   
"""


def hello_user(msg):
    while True:
        msg = input("Как дела?")
        if msg == "Хорошо":
            break
        else:
            print('Ответ неверный')
  