import configuration
import requests
import data

'''Se eliminan todos los print del archivo sender_stand_request.py'''

# solicitud para crear un usuario nuevo
def post_new_user(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_USER_PATH,  # inserta la dirección URL completa
                         json=body,  # inserta el cuerpo de solicitud
                         headers=data.headers)  # inserta los encabezados

response_new_user = post_new_user(data.user_body);


#función para obtener un token nuevo
def get_new_user_token(authToken):
    return requests.get(configuration.URL_SERVICE + configuration.CREATE_USER_PATH,
                        headers=authToken)

data.headers["Authorization"] = "Bearer " + response_new_user.json()["authToken"]
authToken = data.headers.copy();

#solicitud para crear un kit nuevo
def post_new_client_kit(kit):
    return requests.post(configuration.URL_SERVICE + configuration.KITS_PATH,  # inserta la dirección URL completa
                        json=kit,  # inserta el cuerpo de solicitud
                        headers=authToken) # inserta los encabezados

