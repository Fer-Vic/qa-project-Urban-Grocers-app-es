# En este archivo se almacenan todas las solicitudes
import configuration
import requests
import data
from data import kit_body

def get_users_table():
    return requests.get(configuration.URL_SERVICE + configuration.USERS_TABLE_PATH)

response = get_users_table()
print(response.status_code)

def post_new_user(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_USER_PATH,
                         json=body, # hala el body
                         headers=data.headers)  # Hala los encabezados

response = post_new_user(data.user_body)
print(response.status_code)
print(response.json())

def get_kit_body():
    return requests.get(configuration.URL_SERVICE + configuration.KITS_PATH,
                         json=kit_body, # Datos que se envian en la solicitud.
                         headers=data.headers)
response = get_kit_body()
print(response.status_code)
print(response.json())

def post_new_client_kit(kit_body):
    return requests.post(configuration.URL_SERVICE + configuration.KITS_PATH,
                         json=kit_body, # Datos que se envían en la solicitud.
                         headers=data.headers) # Encabezados de la solicitud.

response = post_new_client_kit(data.kit_body)
print(response.status_code)
print(response.json())
