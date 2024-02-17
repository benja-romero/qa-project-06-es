# Benjamin Romero QA cohort 07 Sprint 6
## _Pruebas de API en Urban Grocers_



En este proyecto se crea un usuario nuevo en Urban Grocers y a partir de ello se hacen pruebas para el campo "name" de un kit nuevo; obteniendo como resultado 6 de las 9 preubas como aprobadas; las pruebas donde se pasa un string vacío, un número de caracteres mayor al permitido y un valor de tipo numérico son las pruebas que no son aprobadas.

La lista de comprobación usada es la siguiente:


- 1	El número permitido de caracteres (1): 
-- kit_body = { "name": "a"} /	Código de respuesta: 201 El campo "name" del cuerpo de la respuesta coincide con el campo "name" del cuerpo de la solicitud
- 2	El número permitido de caracteres (511): 
--kit_body = { "name":"El valor de prueba para esta comprobación será inferior a"}	/ Código de respuesta: 201 El campo "name" en el cuerpo de la respuesta coincide con el campo "name" en el cuerpo de la solicitud
- 3	El número de caracteres es menor que la cantidad permitida (0): 
--kit_body = { "name": "" } /	Código de respuesta: 400
- 4	El número de caracteres es mayor que la cantidad permitida (512): 
--kit_body = { "name":"El valor de prueba para esta comprobación será inferior a” } /	Código de respuesta: 400
- 5	Se permiten caracteres especiales: 
--kit_body = { "name": ""№%@"," }	/ Código de respuesta: 201 El campo "name" del cuerpo de la respuesta coincide con el campo "name" del cuerpo de la solicitud
- 6	Se permiten espacios: 
--kit_body = { "name": " A Aaa " }	/ Código de respuesta: 201 El campo "name" del cuerpo de la respuesta coincide con el campo "name" del cuerpo de la solicitud
- 7	Se permiten números: 
--kit_body = { "name": "123" }	/ Código de respuesta: 201 El campo "name" del cuerpo de la respuesta coincide con el campo "name" del cuerpo de la solicitud
- 8	El parámetro no se pasa en la solicitud: 
--kit_body = { }	/ Código de respuesta: 400
- 9	Se ha pasado un tipo de parámetro diferente (número): 
--kit_body = { "name": 123 }	/ Código de respuesta: 400

Primero hay que agregar los siguientes endpoints al archivo configuration.py: 

- /api/v1/users/
- /api/v1/kits
- /api/db/resources/kit_model.csv
- /api/db/resources/user_model.csv

Se crea un archivo llamado data.py donde se deben agregar los datos que se pasarán por las solicitudes.

Una vez teneindo los endpoints y los datos de los cuerpos de las solicitudes, se crea un archivo llamado sender_stand_request.py donde se importará el contenido de ambos archivos, asi com la librería de solicitudes "requests":

```sh
import configuration
import requests
import data
```

Dentro del archivo sender_stand_request.py se escribe la solicitud para crear un nuevo usuario, en la cual obtendermos el token de autorización

```sh
# solicitud para crear un usuario nuevo
def post_new_user(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_USER_PATH,  # inserta la dirección URL completa
                         json=body,  # inserta el cuerpo de solicitud
                         headers=data.headers)  # inserta los encabezados
```

Una vez creado el usuario nuevo y teniendo el token de autorización se procede a mandar la solicitud para crear un nuevo kit dentro del mismo archivo sender_stand_request.py :

```sh
#solicitud para crear un kit nuevo
def post_new_client_kit(kit):
    return requests.post(configuration.URL_SERVICE + configuration.KITS_PATH,  # inserta la dirección URL completa
                        json=kit,  # inserta el cuerpo de solicitud
                        headers=data.headers)  # inserta los encabezados
```

Teniendo la solicitud para crear un kit nuevo se procede a añadir las funciones para realizar las pruebas de la lista de comprobación dentro del archivo create_kit_name_kit_test.py 

Primero hay que importar los datos de los archivos data.py y sender_stand_request.py; la primer función que se va a declarar es para hacer el cambio del valor que contiene el campo "name" del kit nuevo, que es el campo sobre el que se van a estar realizando las pruebas: 

```sh
# esta función cambia los valores en el parámetro "name" del kit
def get_kit_body(name):
    # se copia el diccionario para conservar los datos originales
    current_kit = data.kit_body.copy()
    # Se cambia el valor del parámetro name
    current_kit["name"] = name
    # Se devuelve un nuevo diccionario con el valor name nuevo
    return current_kit
```

Después se declara la función para las pruebas positivas:

```sh
# Función de prueba positiva
def positive_assert(name):
    # El cuerpo de la solicitud actualizada se guarda en la variable kit_body
    kit_body = get_kit_body(name)
    # El resultado de la solicitud se guarda en la variable kit_response
    kit_response = sender_stand_request.post_new_client_kit(kit_body)
    # Comprueba si el código de estado es 201
    assert kit_response.status_code == 201
    # Comprueba que el resultado de la solicitud se guarda en kits_table_response
    kits_table_response = sender_stand_request.get_kits_table()
```

La siguiente función a declarar es la de las pruebas negativas:

```sh
# Función de prueba negativa
def negative_assert_code_400(name):
    # El cuerpo de la solicitud actualizada se guarda en la variable kit_body
    kit_body = get_kit_body(name)
    # El resultado se guarda en la variable kit_response
    kit_response = sender_stand_request.post_new_client_kit(kit_body)
    # Comprueba si el código de estado es 400
    assert kit_response.status_code == 400
    # Comprueba que el atributo code en el cuerpo de respuesta es 400
    assert kit_response.json()["code"] == 400
```

También se tiene que declarar una función para el caso en el que no se pasa ningun valor dentro del campo "name":

```sh
# Función de prueba negativa para cuando no se pasa el parámetro a la solicitud
def negative_assert_no_parameter(name):
    # Guarda el resultado de llamar a la función a la variable "response"
    kit_response = sender_stand_request.post_new_user(name)
    # Comprueba si la respuesta contiene el código 400
    assert kit_response.status_code == 400
    # Comprueba si el atributo "code" en el cuerpo de respuesta es 400
    assert kit_response.json()["code"] == 400
```

Teniendo las funciones declaradas podemos proceder con las pruebas de la lista de comprobación.


