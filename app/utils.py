import json
from datetime import datetime
from operator import itemgetter

from settings import OPEARTION_PATH


def get_operations(path):
    with open(OPEARTION_PATH, 'r', encoding='utf8') as file:
        return json.load(file)


def executed_operations():
    data_list = []
    for txt in get_operations(OPEARTION_PATH):
        if txt.get('state') == 'EXECUTED':
            data_list.append(txt)
    return data_list


def last_five_operations():
    work_list = executed_operations()[-5:]
    return work_list


def sort_time_operation():
    sort_work_list = last_five_operations()
    sort_work_list.sort(key=itemgetter('date'), reverse=True)
    return sort_work_list


def convert_date(str_date: str):
    date_time = datetime.strptime(str_date, '%Y-%m-%dT%H:%M:%S.%f')
    return datetime.strftime(date_time, '%d.%m.%Y')


def convert_from(data: dict):
    if data != None and len(data.split(' ').pop(-1)) == 16:
        card_count = data.split(' ').pop(-1)
        card_name = data.split(' ').pop(0)
        info_card = card_name + ' ' + card_count[0:4] + ' ' + card_count[4:6] + '** **** ' + card_count[12:16]
    elif data != None and len(data.split(' ').pop(-1)) == 20:
        card_count = data.split(' ').pop(-1)
        card_name = data.split(' ').pop(0)
        info_card = card_name + ' ' + card_count[0:4] + ' ' + card_count[4:6] + '** **** **** ' + card_count[16:20]
    else:
        info_card = 'Внесение депозита'
    return info_card


def convert_to(data: dict):
    card_count = data.split(' ').pop(-1)
    information_card = data.split(' ').pop(0) + ' **' + card_count[16:20]
    return information_card


def display_information():
    list_new = []
    for data in sort_time_operation():
        str_description = data['description']
        str_amount = data['operationAmount']['amount']
        str_currency = data['operationAmount']['currency']['name']
        last_five = f"{convert_date(data['date'])} {str_description}\n{''.join(convert_from(data.get('from')))} -> {''.join(convert_to(data['to']))}\n{str_amount} {str_currency}\n"
        list_new.append(last_five)
    return list_new
