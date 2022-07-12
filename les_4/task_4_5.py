# from sys import argv

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


# act = currency_rates_decimal(argv[1])
# print(act[0] + ', ' + act[1])