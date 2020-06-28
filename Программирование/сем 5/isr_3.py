from urllib.request import urlopen
from xml.etree import ElementTree as ET


class CurrencyBoard:
    __instance = None

    @staticmethod
    def getInstance():
        if CurrencyBoard.__instance == None: # проверка наличия данных
            CurrencyBoard()
        return CurrencyBoard.__instance

    def __init__(self):
        if CurrencyBoard.__instance == None:
            currencies_ids_lst = ['R01239', 'R01235', 'R01035', 'R01010', 'R01090', # список id валют
                                  'R01335', 'R01350', 'R01535', 'R01625', 'R01700']
            cur_res_str = urlopen("http://www.cbr.ru/scripts/XML_daily.asp") # загрузка данных с сервера Ценрального Банка РФ
            result = {} # создаём словарь
            cur_res_xml = ET.parse(cur_res_str) # парсинг данных
            root = cur_res_xml.getroot() # корневой элемент
            valutes = root.findall('Valute') # поиск элементов по тэгу
            for el in valutes:
                valute_id = el.get('ID') # все id
                if str(valute_id) in currencies_ids_lst: # поиск необхоdимых id в списке всех id
                    valute_cur_val = el.find('Value').text # запись значения курса валют
                    valute_cur_n = el.find('Name').text # названия соответствующих курсов валют
                    result[valute_id] = valute_cur_n, valute_cur_val # запись данных в словарь
            CurrencyBoard.__instance = result # __instance - словарь


a = CurrencyBoard()
#print(a)

b = CurrencyBoard.getInstance()
#print(b)

c = CurrencyBoard.getInstance()
print(c)
assert id(b) == id(c) # сверка значений адресов переменных
#print(id(b), id(c))
