headers = {
    "Content-Type": "application/json" #se eliminó el token del archivo data.py para generar uno automático en sender_stand_request.py
}

user_body = {
    "firstName": "Andrea",
    "phone": "+11234567890",
    "address": "123 Elm Street, Hilltop"
}

kit_body = {
       "name": "Mi conjunto",
       "card": {
           "id": 1,
           "name": "Para la situación"
       }
   }
