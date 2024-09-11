from fastapi import FastAPI #importa la libreria
from fastapi.responses import HTMLResponse #importa la libreria
app = FastAPI() #crea una instancia de la clase FastAPI
app.title = 'Mi app con FastAPI - Movies' #asigna un valor a la variable title
app.version = "0.0.1" #asigna un valor a la variable version

movies_list = [
    
    {
        "id": 1,
        "title": "The Matrix",
        "overview": "pelicula de ficcion",
        "year": "1999",
        "rating": 8.7
    },
    {
        "id": 2,
        "title": "The Matrix 2",
        "overview": "pelicula de ficcion 2",
        "year": "2000",
        "rating": 8.7
    }
    
]

@app.get('/', tags=["Home"]) #definimos una ruta
def message(): #definimos una función
    return  HTMLResponse ('<h1>HELLO WORLD</h1>') #devolvemos un mensaje

@app.get ('/movies', tags=["Movies"]) #definimos una ruta
def movies(): #definimos una función
    return movies_list

@app.get ('/movies/{id}', tags=["Movies"])
def get_movies (id:int): #definimos una función
    for item in movies_list:
        if item["id"] == id:
            return item
    return []

# Cuando no se puede escribir en la terminal se da ctrl+c y el programa se detiene

