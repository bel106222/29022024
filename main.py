# a = int(input("Enter the first number: "))
# b = int(input("Enter the second number: "))
# if a > b:
#   print(f"The first number is greater, a = {a}")
# else:
#   print(f"The second number is greater, b = {b}")
#####################################################
# a = int(input('Введи время в секундах: '))
# secPerDay = 86400
# secLast = secPerDay - a 
# choise  = int(input('Выбери:\n1 - часы\n2 - минуты\n3 - секунды\n>'))
# if choise == 1:
#   print(f'до полуночи осталось {secLast/60/60} часов')
# elif choise == 2:
#   print(f'до полуночи осталось {secLast/60} минут')
# elif choise == 3:
#   print(f'до полуночи осталось {secLast} секунд')
# else:
#   print('неверный ввод')
######################################################
# D = int(input('Введи диаметр окружности: '))
# choise  = int(input('Выбери:\n1 - площадь окружности\n2 - периметр окружности\n>'))
# if choise == 1:
#   print(f'площадь = {3.14 * (D/2) ** 2}')
# elif choise == 2:
#   print(f'периметр = {3.14 * D}')
# else:
#   print('неверный ввод')
######################################################
# sum = int(input('Введи стоимость: '))
# kol = int(input('Введи количество: '))
# per = int(input('Введи % скидки: '))
# choise  = int(input('Выбери:\n1 - общая сумма заказа\n2 - стоимость одного товара\n>'))
# if choise == 1:
#   # рассчёт скидки:
#   # (100 - 5% скидки) / 100 = 0.95 - скидка, затем умножаем её на количество * стоимость
#   print(f'общая сумма заказа = {sum * kol - sum * kol * per / 100}')
# elif choise == 2:
#   print(f'стоимость одного товара = {sum - sum * per / 100}')
# else:
#   print('неверный ввод')
######################################################
######################################################
# AND - логическое умножение
# speed = int(input('Введи скорость: '))
# if speed > 50 and speed < 150:
#   print('В диапазоне')
# else:
#   print('Вне диапазона')
######################################################
# OR - логическое сложение
# answer = input('Какой язык мы изучаем? ')
# count  = 0

# if answer == 'python' or answer == 'Python':
#   print('Верно!')
#   count+=1
# else:
#   print('Неверно!')
  
#   answer = input('Сколько цветов у радуги? ')
# if answer == '7' or answer == 'семь' or answer == 'Семь':
#   print('Верно!')
#   count+=1
# else:
#   print('Неверно!')
######################################################
import random
print('Добро пожаловать в игру "Камень, ножницы, бумага !"')
print('Правила игры: камень бьёт ножницы, ножницы бьют бумагу, бумага бьёт камень')
answer = input('Выбери: камень, ножницы или бумага: ')
if answer == 'камень' or answer == 'Камень':
  answer = 'камень'
elif answer == 'ножницы' or answer == 'Ножницы':
  answer = 'ножницы'
elif answer == 'бумага' or answer == 'Бумага':
  answer = 'бумага'
else:
  print('Неверный ввод')
botAnswer = random.choice(["камень", "ножницы", "бумага"])
print(f'Мой ход - {botAnswer}')

if answer == botAnswer:
  print('Ничья!')
elif (answer == 'бумага' and botAnswer == 'камень') or (answer == 'ножницы' and botAnswer == 'бумага') or (answer == 'камень' and botAnswer == 'ножницы'):
  print('Ты победил!')
else:
  print('Ты проиграл!')