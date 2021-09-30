import json

with open('json_tarifas.json', 'r') as tarifas:  # con esto se cierra el archivo al acabarse el código indentado
    content = json.load(tarifas)  # lee el archivo y lo convierte en un diccionario
# tarifas.close()

family = [{1: 'Alicia', 'age': 53, 'status': 'mother'},
          {'name': 'Aaron', 'age': 19, 'status': 'brother'},
          {'name': 'Mariana', 'age': 25, 'status': 'cousin'}]

with open('family_record.json', 'w') as family_record:
    json.dump(family, family_record)
# family_record.close()

# json.loads()  # el json a deserializar está contenido en un string
tarifa1 = '[{"carrier": "CCH", "code": "DEX (terrestre)", "transit_days": 4, "price": 10006}]'
dict_tarifa1 = json.loads(tarifa1)
