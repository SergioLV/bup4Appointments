import requests

centros_santiago = [{
  '_id': 'BSP',
  'direccion': 'Av. Las condes 8840, Las Condes ',
  'nombre': ' Bupa Sport - Las Condes'
}, {
  '_id': 'CBS',
  'direccion': 'Av. Departamental 01455, La florida',
  'nombre': 'Clinica Bupa Santiago'
}, {
  '_id': 'MMO',
  'direccion': 'Av. AmΘrico Vespucio 1501, Mall Plaza Oeste, Cerrillos, Santiago',
  'nombre': 'Clφnica del deporte'
}, {
  '_id': 'BAP',
  'direccion': ' Apoquindo 4062, Las Condes, Santiago',
  'nombre': 'Integramedica Apoquindo - Las Condes'
}, {
  '_id': 'IAL',
  'direccion': "Av. Libertador Bernardo O'Higgins 654, Santiago Centro",
  'nombre': 'IntegraMΘdica Alameda - Santiago Centro'
}, {
  '_id': 'ICO',
  'direccion': 'Av. Kennedy 9001, Acceso Principal 3 Piso Mall Alto Las Condes, Santiago',
  'nombre': 'IntegraMΘdica Alto Las Condes - Las Condes'
}, {
  '_id': 'IBN',
  'direccion': 'Bandera 168, Santiago Centro',
  'nombre': 'IntegraMΘdica Bandera - Santiago Centro'
}, {
  '_id': 'IBA',
  'direccion': 'Barcelona 2116, Providencia, Santiago',
  'nombre': 'IntegraMΘdica Barcelona - Providencia'
}, {
  '_id': 'ICY',
  'direccion': 'Coyancura 2270 piso 9 depto 910, Providencia',
  'nombre': 'IntegraMΘdica Coyancura'
}, {
  '_id': 'DPV',
  'direccion': 'San Carlos de Ancud 402, Local N░ 30, 8240000 La Florida, Regi≤n Metropolitana',
  'nombre': 'IntegraMΘdica Dental La Florida'
}, {
  '_id': 'IEC',
  'direccion': 'Av. Libertador Bernardo O┤Higgins 3466, Estaci≤n Central, Santiago',
  'nombre': 'IntegraMΘdica Estaci≤n Central - Mall Plaza Alameda'
}, {
  '_id': 'IFS',
  'direccion': 'Av. Vicu±a Mackenna Oriente 6969, La Florida, Santiago',
  'nombre': 'IntegraMΘdica Florida Vicu±a Mackenna'
}, {
  '_id': 'ICE',
  'direccion': 'HuΘrfanos 1147, Santiago Centro',
  'nombre': 'IntegraMΘdica HuΘrfanos - Santiago Centro'
}, {
  '_id': 'IND',
  'direccion': 'Profesor Za±artu 1121, Independencia, Santiago',
  'nombre': 'IntegraMΘdica Independencia - Independencia'
}, {
  '_id': 'IMP',
  'direccion': 'Av. Los Pajaritos 1790, esquina 5 de abril, Mall Espacio Urbano, Maip·.',
  'nombre': 'IntegraMΘdica Maip·'
}, {
  '_id': 'IMQ',
  'direccion': 'Av. Manquehue Sur 329 , Las Condes, Santiago',
  'nombre': 'IntegraMΘdica Manquehue - Las Condes'
}, {
  '_id': 'IMN',
  'direccion': "Av. Libertador Bernardo O'higgins 1529, Santiago",
  'nombre': 'IntegraMΘdica Moneda'
}, {
  '_id': 'IPL',
  'direccion': 'Av.Consistorial 2100',
  'nombre': 'IntegraMΘdica Pe±alolΘn'
}, {
  '_id': 'IPE',
  'direccion': 'Av. Larraφn 5862, La Reina, Santiago. Piso 4, 5, 6 y 7, Entrega de Exßmenes Piso 5.',
  'nombre': 'IntegraMΘdica Plaza Ega±a - ╤u±oa'
}, {
  '_id': 'IPD',
  'direccion': 'Padre Hurtado Sur 785, Las Condes',
  'nombre': 'IntegraMΘdica Plaza Los Dominicos - Las Condes'
}, {
  '_id': 'INO',
  'direccion': 'Av. AmΘrico Vespucio 1737, Mall Plaza Norte, Huechuraba, Santiago',
  'nombre': 'IntegraMΘdica Plaza Norte - Huechuraba'
}, {
  '_id': 'IMO',
  'direccion': 'Av. AmΘrico Vespucio 1501, Mall Plaza Oeste, Cerrillos, Santiago',
  'nombre': 'IntegraMΘdica Plaza Oeste - Cerrillos'
}, {
  '_id': 'IPA',
  'direccion': 'Av. Concha y Toro 26, Puente Alto, Santiago',
  'nombre': 'IntegraMΘdica Plaza Puente Alto'
}, {
  '_id': 'IPS',
  'direccion': 'Av. Jorge Alessandri 20040, Mall Plaza Sur, San Bernardo',
  'nombre': 'IntegraMΘdica Plaza Sur - San Bernardo'
}, {
  '_id': 'ITO',
  'direccion': 'Av. Camilo Henriquez 3296, Mall Plaza Tobalaba, Puente Alto, Santiago',
  'nombre': 'IntegraMΘdica Plaza Tobalaba - Puente Alto'
}, {
  '_id': 'IPV',
  'direccion': 'Av. Vicu±a Mackenna 7110, La Florida, Santiago',
  'nombre': 'IntegraMΘdica Plaza Vespucio - La Florida'
}, {
  '_id': 'ISM',
  'direccion': 'Llano Subercaseaux 3965, Metro San Miguel, San Miguel,  Santiago',
  'nombre': 'IntegraMΘdica San Miguel'
}, {
  '_id': 'ISL',
  'direccion': 'Av.Victoria 411, San Bernardo',
  'nombre': 'IntegraMΘdica Santa Lucφa - San Bernardo'
}, {
  '_id': 'ISA',
  'direccion': '-',
  'nombre': 'IntegramΘdica Video Consulta'
}, {
  '_id': 'IVT',
  'direccion': 'Avenida Vitacura 4705, Vitacura, Santiago',
  'nombre': 'IntegraMΘdica Vitacura - Vitacura'
}, {
  '_id': 'SAL',
  'direccion': 'Libertador Bernardo Ohiggins 1529, Santiago',
  'nombre': 'Sonorad Alameda - Santiago Centro'
}, {
  '_id': 'SIR',
  'direccion': 'Irarrazaval 2401 local 15, ╤u±oa',
  'nombre': 'Sonorad Irarrazaval - ╤u±oa'
}, {
  '_id': 'SFS',
  'direccion': 'Vicu±a Mackenna 7255, La Florida',
  'nombre': 'Sonorad La Florida'
}, {
  '_id': 'SMA',
  'direccion': 'Avenida Los Pajaritos 1605, Maip·',
  'nombre': 'Sonorad Maip·'
}]

def get_token():
    url = "https://api.bupa.cl/api/login"

    headers = {
        "Sec-Ch-Ua": '"Not?A_Brand";v="8", "Chromium";v="108"',
        "Sec-Ch-Ua-Mobile": "?0",
        "Authorization": "Bearer null",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.5359.125 Safari/537.36",
        "Access-Control-Allow-Methods": "GET",
        "Content-Type": "application/json",
        "Access-Control-Allow-Origin": "*",
        "Accept": "application/json, text/plain, */*",
        "X-Authorization-Type": "plain",
        "X-System-Type": "public",
        "Sec-Ch-Ua-Platform": '"Windows"',
        "Origin": "https://agendaclinicas.bupa.cl",
        "Sec-Fetch-Site": "same-site",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Dest": "empty",
        "Referer": "https://agendaclinicas.bupa.cl/",
        "Accept-Encoding": "gzip, deflate",
        "Accept-Language": "en-US,en;q=0.9"
    }

    response = requests.get(url, headers=headers)

    if response.ok:
        return response.json()['token']
    else:
        response.raise_for_status()

import requests

# {
# 				"_id": "2100",
# 				"estado": "",
# 				"videoconsulta": "X",
# 				"prestaciones": [
# 					{
# 						"centros": [
# 							{
# 								"codigo": "CBS"
# 							}
# 						],
# 						"id": "11810B",
# 						"nombre": "Consulta Dermatologia",
# 						"videoconsulta": ""
# 					}
# 				],
# 				"clasificacion": "01",
# 				"nombre": " Dermatología",
# 				"favorito": False
# 			}

def get_available_hours(centro):
    url = 'https://api.bupa.cl/agenda/ms-sap/horarios/listardisponibleespecialidad2nv'
    token = "Bearer " + get_token();
    headers = {
        'Host': 'api.bupa.cl',
        'Content-Length': '244',
        'Sec-Ch-Ua': '"Not?A_Brand";v="8", "Chromium";v="108"',
        'Accept': 'application/json, text/plain, */*',
        'Content-Type': 'application/json; charset=UTF-8',
        'Sec-Ch-Ua-Mobile': '?0',
        'Authorization': token,
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.5359.125 Safari/537.36',
        'Sec-Ch-Ua-Platform': '"Windows"',
        'Origin': 'https://agendaclinicas.bupa.cl',
        'Sec-Fetch-Site': 'same-site',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Dest': 'empty',
        'Referer': 'https://agendaclinicas.bupa.cl/',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'en-US,en;q=0.9'
    }
# En este caso, el la especialidad es _id y la categoria para buscar la hora es el id del json
    data = {
        "BupaHorasDisponibleMedicoRequest": {
            "Categoria": "11810B",
            "RutProfesional": "",
            "FechaDesde": "2023-04-01",
            "FechaHasta": "2023-05-05",
            "CentroSanitario": "RED",
            "Especialidad": "2100",
            "Prevision": "0000900003",
            "CentroMedico": centro,
            "Clasificacion": "01"
        }
    }
    
    return requests.post(url, headers=headers, json=data)

for centro in centros_santiago:
    fileLocation = "results/" + centro["nombre"]
    # response = get_available_hours(centro["_id"]).json()["data"]["Dia"][0]
    
    with open(fileLocation, 'w') as file:
        file.write(get_available_hours(centro["_id"]).text)
    