"""
2. Написать функцию currency_rates(), принимающую в качестве аргумента код валюты
(например, USD, EUR, GBP, ...) и возвращающую курс этой валюты по отношению к рублю.
Использовать библиотеку requests. В качестве API можно использовать
http://www.cbr.ru/scripts/XML_daily.asp. Рекомендация: выполнить предварительно запрос
к API в обычном браузере, посмотреть содержимое ответа. Можно ли, используя только
методы класса str, решить поставленную задачу? Функция должна возвращать результат
числового типа, например float. Подумайте: есть ли смысл для работы с денежными величинами
использовать вместо float тип Decimal? Сильно ли усложняется код функции при этом? Если в
качестве аргумента передали код валюты, которого нет в ответе, вернуть None. Можно ли
сделать работу функции не зависящей от того, в каком регистре был передан аргумент?
В качестве примера выведите курсы доллара и евро.
"""

# def currency_rates_decimal(code_money):
#     """Возвращает значение кода введенной валюты (в любом регистре)
#     по отношению к RUB в рублях с округлением до десятых,
#     None если валюта отсутствует"""
#     import requests
#     from decimal import Decimal
#     code_money = code_money.upper()
#     url_cbr = 'http://www.cbr.ru/scripts/XML_daily.asp'
#     info = requests.get(url_cbr)
#     print("Status code:", info.status_code)
#     info_text = info.text
#     st = info_text.find(code_money)
#     if st > 0:
#         st_num = (info_text.find('<Value>', st)) + 7
#         fsh_num = info_text.find('</Value>', st_num)
#         final_num = info_text[st_num:fsh_num]
#         f_value = final_num.replace(',', '.')
#         d_value = Decimal(f_value)
#         d_value = d_value.quantize(Decimal("1.00"))
#         return d_value
#     else:
#         return None
#
# print(currency_rates_decimal('usd'))
# print(currency_rates_decimal('gbP'))


def currency_rates_decimal(code_money):
    """Возвращает значение кода введенной валюты (в любом регистре)
    по отношению к RUB в рублях с округлением до десятых,
    None если валюта отсутствует"""
    import requests
    from decimal import Decimal
    import datetime
    code_money = code_money.upper()
    url_cbr = 'http://www.cbr.ru/scripts/XML_daily.asp'
    info = requests.get(url_cbr)
    print("Status code:", info.status_code)
    info_text = info.text
    date = datetime.datetime.now()
    date_text = str(date)
    date_value = date_text.find(' ')
    final_date = date_text[:date_value] # date
    # print(final_date)
    st = info_text.find(code_money) # money
    if st > 0:
        st_num = (info_text.find('<Value>', st)) + 7
        fsh_num = info_text.find('</Value>', st_num)
        final_num = info_text[st_num:fsh_num]
        f_value = final_num.replace(',', '.')
        d_value = Decimal(f_value)
        d_value = d_value.quantize(Decimal("1.00"))
        d_value = str(d_value)
        result = [d_value, final_date]
        return result
    else:
        return None

act = currency_rates_decimal('gbP')
print(act[0] + ', ' + act[1])

