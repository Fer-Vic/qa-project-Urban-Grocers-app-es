#En este archivos se almacenan la lista de comprobaciones
import sender_stand_request
import data

# Cambiar el nombre en el body de la solicitud
def get_kit_body(name):
    current_body = data.kit_body.copy() # hala el body que está en data.py
    current_body["name"] = name # Cambia el valor del parámetro name
    return current_body # regresa un diccionario con el name requerido

# Prueba positiva
def positive_assert(name):
    kit_body = get_kit_body(name) # El body se almacena en kit_body
    kit_response = sender_stand_request.post_new_client_kit(kit_body) # El resultado se almacena en response
    assert kit_response.status_code == 201 # Prueba que el código de estado es 201

# Pueba negativa
def negative_assert(name):
    kit_body = get_kit_body(name) # El body se almacena en kit_body
    response = sender_stand_request.post_new_client_kit(kit_body) # El resultado se almacena en response
    assert response.status_code == 400 # Prueba que el código de estado es 400

# Prueba 1: 1 caracter permitido en el campo name
def test_1_create_kit_1_character_in_name_get_success_response():
    positive_assert(data.kit_body_prueba1) #hala body de data.py

# Prueba 2: 511 caracteres permitidos en el campo name
def test_2_create_kit_511_characters_in_name_get_success_response():
    positive_assert(data.kit_body_prueba2) #hala body de data.py

# Prueba 3. 0 Caracteres en el campo name - string vacío
def test_3_create_kit_0_characters_in_name_get_error_response():
    negative_assert(data.kit_body_prueba3)

# Prueba 4. 512 caracteres no permitidos en el campo name
def test_4_create_kit_512_characters_in_name_get_error_response():
    negative_assert(data.kit_body_prueba4)

# Prueba 5. caracteres especiales en el campo name
def test_5_create_kit_special_symbol_in_name_get_success_response():
    positive_assert(data.kit_body_prueba5)

# Prueba 6. espacios en el campo name
def test_6_create_kit_has_spaces_in_name_get_success_response():
    positive_assert(data.kit_body_prueba6)

# Prueba 7. strings y números en el campo name
def test_7_create_kit_has_number_in_first_name_get_success_response():
    positive_assert(data.kit_body_prueba7)

# Prueba 8. El parametro name no se pasa en la solicitud
def test_8_create_kit_no_name_get_error_response():
    kit_body = data.kit_body.copy()
    kit_body.pop("name")
    negative_assert(kit_body) #Respuesta

# Prueba 9. Error. Se ha pasado un tipo de parámetro diferente en name: número
def test_9_create_kit_number_type_name_get_error_response():
    kit_body = data.kit_body_prueba9 # El body se almacena en kit_body
    response = sender_stand_request.post_new_client_kit(kit_body) # El resultado se almacena en response

    assert response.status_code == 400 # Prueba que el código de estado = 400