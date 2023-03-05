"""

Домашнее задание №1

Цикл for: Продажи товаров

* Дан список словарей с данными по колличеству проданных телефонов
  [
    {'product': 'iPhone 12', 'items_sold': [363, 500, 224, 358, 480, 476, 470, 216, 270, 388, 312, 186]}, 
    {'product': 'Xiaomi Mi11', 'items_sold': [317, 267, 290, 431, 211, 354, 276, 526, 141, 453, 510, 316]},
    {'product': 'Samsung Galaxy 21', 'items_sold': [343, 390, 238, 437, 214, 494, 441, 518, 212, 288, 272, 247]},
  ]
* Посчитать и вывести суммарное количество продаж для каждого товара
* Посчитать и вывести среднее количество продаж для каждого товара
* Посчитать и вывести суммарное количество продаж всех товаров
* Посчитать и вывести среднее количество продаж всех товаров
"""

products = [
    {
    'product': 'iPhone 12', 
    'items_sold': [363, 500, 224, 358, 480, 476, 470, 216, 270, 388, 312, 186]
     }, 
    {
    'product': 'Xiaomi Mi11', 
    'items_sold': [317, 267, 290, 431, 211, 354, 276, 526, 141, 453, 510, 316]
     },
    {
    'product': 'Samsung Galaxy 21', 
    'items_sold': [343, 390, 238, 437, 214, 494, 441, 518, 212, 288, 272, 247]
     },
  ]
general_sales = 0
general_average = 0
for product in products:
    phone = product['product']
    product_sales = product['items_sold']
    items_sold_sum = sum(product_sales)
    product_sales_average = int(items_sold_sum / len(product_sales))
    
    print(f'Суммарное количество продаж {phone}: {items_sold_sum}')
    print(' ')
    print(f'Среднее количество продаже {phone}: {product_sales_average}')
    print(' ')

    general_sales += items_sold_sum
    general_average += general_sales / len(products)


print(f'Суммарное количество продаж всех товаров: {general_sales}')
print(' ')
print(f'Среднее количество продаж всех товаров: {int(general_average)}')
