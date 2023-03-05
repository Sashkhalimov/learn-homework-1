"""

Домашнее задание №1

Условный оператор: Сравнение строк

* Написать функцию, которая принимает на вход две строки
* Проверить, является ли то, что передано функции, строками. 
  Если нет - вернуть 0
* Если строки одинаковые, вернуть 1
* Если строки разные и первая длиннее, вернуть 2
* Если строки разные и вторая строка 'learn', возвращает 3
* Вызвать функцию несколько раз, передавая ей разные праметры 
  и выводя на экран результаты

"""

def difference(string1, string2):
    if not isinstance(string1, str) or not isinstance(string2, str):
        return 0
    elif string1 == string2:
        return 1
    elif len(string1) > len(string2):
        return 2
    elif string1 != string2 and string2 == "learn":
        return 3
         
            
print(difference(3, 2))
print(difference("00123", "321"))
print(difference("123", "1234"))
print(difference("двадцать", "два"))
print(difference("", ""))
print(difference("asdf", "learn"))
