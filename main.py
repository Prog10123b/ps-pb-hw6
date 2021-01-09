ITEM_COST_MAX = 13000


def get_value_by_key(input_col, key, separator=':'):
    result = None
    for pair in input_col:
        content = pair.split(separator)

        if content[0] == key:
            result = content[1]
    
    return result


log = """name:Иван;gender:m;item:Часы;item_cost:9800
name:Иван;gender:m;item:Фитнес-браслет;item_cost:12300
name:Иван;gender:m;item:Кофемашина;item_cost:23500
name:Петр;gender:m;item:Часы;item_cost:9800
name:Петр;gender:m;item:Фитнес-браслет;item_cost:12300
name:Петр;gender:m;item:Айфон;item_cost:77900
name:Петр;gender:m;item:Чехол для телефона;item_cost:350
name:Петр;gender:m;item:Кофемашина;item_cost:23500
name:Дарья;gender:m;item:Айфон;item_cost:77900
name:Марья;gender:m;item:Кофемашина;item_cost:23500
name:Юлия;gender:m;item:Фитнес-браслет;item_cost:12300"""

out_elements = []


log_list = log.split('\n')

for record in log_list:
    record_elements = record.split(';')

    if int(get_value_by_key(record_elements, 'item_cost')) < ITEM_COST_MAX:
        found = False
        for element in out_elements:
            if element['item'] == get_value_by_key(record_elements, 'item'):
                found = True
        
        if not found:
            out_elements.append({'item':get_value_by_key(record_elements, 'item'), 'item_cost':get_value_by_key(record_elements, 'item_cost')})

print(f'Все предметы стоимость которых не превышает {ITEM_COST_MAX}:')
for element in out_elements:
    print(f'Предмет: {element["item"]}, стоимость: {element["item_cost"]}.')
