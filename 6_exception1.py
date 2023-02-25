"""

Домашнее задание №1

Исключения: KeyboardInterrupt

* Перепишите функцию hello_user() из задания while1, чтобы она 
  перехватывала KeyboardInterrupt, писала пользователю "Пока!" 
  и завершала работу при помощи оператора break
    
"""

def hello_user(msg):
    try:
        while True:
            msg = input("Как дела?")
            if msg == "Хорошо":
                break
            else:
                print('Ответ неверный')
    except KeyboardInterrupt:
        print('Пока!')
        break            
    