# IMPORTANTE: NO borrar los comentarios
import json
import requests


if __name__ == '__main__':
    print("Bienvenidos a otra clase de Inove con Python")
    
    # URL a la API de jsonplaceholder
    url = "https://jsonplaceholder.typicode.com/todos"

    # Alumno:
    # El primer paso es que copien esa URL en su explorador web
    # y analicen los datos en general:
    # 1) Observando la URL se puede ver que en total hay 200 entradas,
    # del id=1 al id=200
    # 2) Observando la URL se puede ver que en total hay 10 usuarios,
    # del userId=1 al userId=10
    # 3) En cada entrada se especifica si el usuario completó ese título,
    # mediante el campo "completed".

    # 1) API request
    # Deberá obtener el JSON de la API request
    # y almacenarlo en una variable llamada data

    # 2) Contar títulos
    # Deberá recorrar la variable data
    # y contar cuántos títulos completó el usuario
    # con userId=5
    # Deberá alcenar la cantidad de títulos
    # en una variable llamada "cantidad_titulos"

    # Comienza aquí su código
    response = requests.get(url)
    data = response.json()
    print(json.dumps(data, indent=4))

    cantidad_titulos = 0
    for user in data:
        
        if user["userId"] == 5:
            if user["completed"] == True:
                cantidad_titulos += 1
    
    print(cantidad_titulos)



    print("terminamos")