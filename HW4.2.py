# Предусловие.
# Задачи 3 и 4 выполнить в 2 - х вариантах:
# 1) В процедурном виде(весь код в одной процедуре).
# 2) В виде функций - код разбит на функции.Отдельные функции можно вынести в другие.py файлы и вызывать их в main.py
# предвварительно импортируя в main.py.
# Задача №1
# Обменник.
# Создать скрипт который будет запускаться из консоли 1 раз, выдавать результат и зарываться.
# 1. На вход обменнику вводишь количество денег int.
# 2. На выходе в консоль выводится ответ в таком виде:
# "Ты ввёл int (Валюта)"
# "конвертированная сумма в USD = int"
# 3.Валюту пользователя определите сами.


rub_item = "rub"
usd_rub_rate = 91.75

usd_item = "usd"
usd_usd_rate = 1

while True:
    action = input("Пожалуйста, введите количество валюты:")
    if action.startswith('_'):
        print('Введите положительное число.')
    else:
        action = int(action)

        print("Ты ввёл ", action, rub_item)

        if action > 0:
            currency = action/usd_rub_rate
            print("конвертированная валюта в USD =", currency)



# Задача №2
# Обменник.Создать скрипт который будет запускаться из консоли 1 раз из консоли, выдавать результат и зарываться.
# 1.На вход обменнику вводишь количество денег int.
# 2. На выходе в консоль выводится ответ в таком виде:
# "Ты ввёл int (Валюта)"
# "Конвертированная сумма в USD = int"
# "Конвертированная сумма в EUR = int"
# "Конвертированная сумма в CHF = int"
# "Конвертированная сумма в GBP = int"
# "Конвертированная сумма в CNY = int"
# 3.
# Валюту пользователя определите сами.

currency = ['USD','EUR','CHF','GBR','CNY']

rub_item = "rub"
usd_rub_rate = 91.75

usd_item = "usd"
usd_usd_rate = 1

eur_item = "eur"
rub_eur_rate = 102.91

chf_item = "chf"
rub_chf_rate = 100.2

gbr_item = "gbr"
rub_gbr_rate = 123.14

cny_item = "cny"
rub_cny_rate = 14.53

while True:
    action = input("Пожалуйста, введите количество валюты:")
    if action.startswith('_'):
        print('Введите положительное число.')
    else:
        action = int(action)

        print("Ты ввёл",action, rub_item)

        if action > 0:
            currency = action/usd_rub_rate
            print("конвертированная валюта в USD =", currency)
            currency = action/rub_eur_rate
            print('конвертированная валюта в EUR =', currency)
            currency = action/rub_chf_rate
            print('конвертированная валюта в CHF =', currency)
            currency = action/rub_gbr_rate
            print('конвертированная валюта в GBR =', currency)
            currency = action / rub_cny_rate
            print('конвертированная валюта в CNY =', currency)

# Задача №3
# Обменник.Создать скрипт который будет запускаться из консоли 1 раз из консоли, выдавать результат и зарываться.
# 1.
# На вход обменнику вводишь количество денег int.
# 2.
# На выходе в консоль выводится ответ в таком виде:
# "Ты ввёл int (Валюта)"
# "конвертированная сумма в USD = int"
# "конвертированная сумма в EUR = int"
# "конвертированная сумма в CHF = int"
# "конвертированная сумма в GBP = int"
# "конвертированная сумма в CNY = int"
#
# 3.
# Скрипт должен выдать сообщение
# "Введите положительное число."Если число меньше 0.
# "Вы ввели не число. Введите число."Если введены буквы.
# "Вы ввели пустое поле. Введите число."Если введено пустое значение.
# 4.
# Валюту пользователя определите сами.

import re

currency = ['USD','EUR','CHF','GBR','CNY']

rub_item = "rub"
usd_rub_rate = 91.75

usd_item = "usd"
usd_usd_rate = 1

eur_item = "eur"
rub_eur_rate = 102.91

chf_item = "chf"
rub_chf_rate = 100.2

gbr_item = "gbr"
rub_gbr_rate = 123.14

cny_item = "cny"
rub_cny_rate = 14.53

while True:
    action = input("Пожалуйста, введите количество валюты:")
    if action.startswith('-'):
        print('Введите положительное число.')
    elif re.search(r'[!@#$%^&*()\[\]=+;\'{}\"/A-Za-z]', action):
        print("Вы ввели не число.Введите число.")
    elif action == '':
        print('Вы ввели пустое поле.Введите число.')
    else:
        action = int(action)

        print("Ты ввёл",action, rub_item)

        if action > 0:
            currency = action/usd_rub_rate
            print("конвертированная валюта в USD =", currency)
            currency = action/rub_eur_rate
            print('конвертированная валюта в EUR =', currency)
            currency = action/rub_chf_rate
            print('конвертированная валюта в CHF =', currency)
            currency = action/rub_gbr_rate
            print('конвертированная валюта в GBR =', currency)
            currency = action / rub_cny_rate
            print('конвертированная валюта в CNY =', currency)


# Задача №4
# Обменник.Скрипт запускается в консоли и работает постоянно.Остановится нажатием ctrl + c.
# 1.
# Скрипт сначала выводит "Выберите валюту из ['USD','EUR','CHF','GBP','CNY']"
# 2.
# Пользователь вводит один из 5 вариантов['USD', 'EUR', 'CHF', 'GBP', 'CNY']
# 3.
# Потом Скрипт выводит "Введите сумму"
# 4.
# Пользователь вводит сумму int
# 5.
# Скрипт выводит:
# "Вы ввели сумму int и валюту " Валюта " "
# "конвертированная сумма в " Валюта " = int"
# 6.
# Скипт должен выдать сообщение "Введите положительное число."
# Если число меньше  0.
# "Вы ввели не число. Введите число."
# Если введены буквы.
# "Вы ввели пустое поле. Введите число."
# Если введено пустое значение.
# 7.
# После сообщеня об ошибке, скрипт должен автоматом вернуться к шагу 1.
# 8.
# Валюту пользователя определите сами.
import re

currency = ['USD','EUR','CHF','GBR','CNY']

rub_item = "rub"
usd_rub_rate = 91.75

usd_item = "usd"
usd_usd_rate = 1

eur_item = "eur"
rub_eur_rate = 102.91

chf_item = "chf"
rub_chf_rate = 100.2

gbr_item = "gbr"
rub_gbr_rate = 123.14

cny_item = "cny"
rub_cny_rate = 14.53

while True:
    currencyyour = input("Выберите валюту из ['USD','EUR','CHF','GBP','CNY']: ")
    if currencyyour in currency:
        currencymany = input("Введите сумму (RUB): ")
        if currencymany.startswith('-'):
            print("Введите положительное число.")
        elif re.search(r'[!@#$%^&*()\[\]=+;\'{}\"/A-Za-z]', currencymany):
            print("Вы ввели не число. Введите число.")
        elif currencymany == '':
            print("Вы ввели пустое поле. Введите число.")
        else:
            currencymany = int(currencymany)

            print("Вы ввели сумму", currencymany, rub_item)

            if currencyyour== 'USD':
                curUSD = currencymany / usd_rub_rate
                print("конвертированная сумма в USD =",curUSD)
            elif currencyyour == 'EUR':
                curEUR = currencymany / rub_eur_rate
                print("конвертированная сумма в EUR =",curEUR)
            elif currencyyour == 'CHF':
                curCHF = currencymany / rub_chf_rate
                print("конвертированная сумма в CHF =",curCHF)
            elif currencyyour == 'GBR':
                curGBR = currencymany / rub_gbr_rate
                print("конвертированная сумма в GBR =",curGBR)
            else:
                curCNY = currencymany / rub_cny_rate
                print("конвертированная сумма в CNY =",curCNY)
    else:
        print("Валюта не поддерживается.")
