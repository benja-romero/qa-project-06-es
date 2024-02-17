import configuration
import requests
import data

# solicitud para crear un usuario nuevo
def post_new_user(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_USER_PATH,  # inserta la dirección URL completa
                         json=body,  # inserta el cuerpo de solicitud
                         headers=data.headers)  # inserta los encabezados

response = post_new_user(data.user_body);
print(response.status_code)
print(response.json())

#solicitud para crear un kit nuevo
def post_new_client_kit(kit):
    return requests.post(configuration.URL_SERVICE + configuration.KITS_PATH,  # inserta la dirección URL completa
                        json=kit,  # inserta el cuerpo de solicitud
                        headers=data.headers)  # inserta los encabezados

response = post_new_client_kit(data.kit_body);
print(response.status_code)
print(response.json())

#solicitud para obtener la tabla de kits
def get_kits_table():
    return requests.get(configuration.URL_SERVICE + configuration.KITS_TABLE_PATH) # inserta la dirección URL completa
# guarda la tabla obtneida en la variable response
response = get_kits_table()
print(response.status_code)

#solicitud para obtener la tabla de usuarios
def get_users_table():
    return requests.get(configuration.URL_SERVICE + configuration.USERS_TABLE_PATH) # inserta la dirección URL completa
# guarda la tabla obtenida en la variable response
response = get_users_table()
print(response.status_code)
