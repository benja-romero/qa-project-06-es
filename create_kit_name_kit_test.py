import sender_stand_request
import data


# esta función cambia los valores en el parámetro "name" del kit
def get_kit_body(name):
    # se copia el diccionario para conservar los datos originales
    current_kit = data.kit_body.copy()
    # Se cambia el valor del parámetro name
    current_kit["name"] = name
    # Se devuelve un nuevo diccionario con el valor name nuevo
    return current_kit



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





# Función de prueba negativa para cuando no se pasa el parámetro a la solicitud
def negative_assert_no_parameter(name):
    # Guarda el resultado de llamar a la función a la variable "response"
    kit_response = sender_stand_request.post_new_user(name)
    # Comprueba si la respuesta contiene el código 400
    assert kit_response.status_code == 400
    # Comprueba si el atributo "code" en el cuerpo de respuesta es 400
    assert kit_response.json()["code"] == 400



# Prueba 1 - El número permitido de caracteres (1)
def test_create_1_letter_name_new_kit():
    positive_assert("a")

# Prueba 2 - El número permitido de caracteres (511)
def test_create_511_letter_name_new_kit():
    positive_assert("AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabC")

# Prueba 3 - El número de caracteres es menor que la cantidad permitida (0)
def test_create_0_letter_name_new_kit():
    negative_assert_code_400("")

# Prueba 4 - El número de caracteres es mayor que la cantidad permitida (512)
def test_create_512_letter_name_new_kit():
    negative_assert_code_400("AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcD")

# Prueba 5 - Se permiten caracteres especiales
def test_create_special_character_name_new_kit():
    positive_assert("\"№%@\",")

# Prueba 6 - Se permiten espacios
def test_create_name_with_space_new_kit():
    positive_assert(" A Aaa ")

# Prueba 7 - Se permiten números
def test_create_name_with_numbers_new_kit():
    positive_assert("123")

# Prueba 8 - El parámetro no se pasa en la solicitud
def test_create_new_kit_without_name_parameter():
    # Se copia el diccionario del archivo data en la variable kit_body, para no afectar el contenido original
    kit_body = data.kit_body.copy()
    # El parámetro "name" se elimina de la solicitud
    kit_body.pop("name")
    # Comprueba la respuesta
    negative_assert_no_parameter(kit_body)

# Prueba 9 - Se ha pasado un tipo de parámetro diferente (número)
def test_create_new_kit_with_number_type_name_parameter():
    negative_assert_code_400(123)