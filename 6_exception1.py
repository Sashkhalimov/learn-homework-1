"""

Домашнее задание №1

Исключения: KeyboardInterrupt

* Перепишите функцию hello_user() из задания while1, чтобы она 
  перехватывала KeyboardInterrupt, писала пользователю "Пока!" 
  и завершала работу при помощи оператора break
    
"""

def hello_user():
    msg = ''
    while msg != "Хорошо":
        try:
            msg = input('Как дела?')
        except KeyboardInterrupt:
            print('Пока!')
                   
    
hello_user()
