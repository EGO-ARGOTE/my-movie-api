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
    },
    {
        "id": 3,
        "title": "The Matrix 3",
        "overview": "pelicula de ficcion 3",
        "year": "2001",
        "rating": 8.7
    },
    {
        "id": 4,
        "title": "The Matrix 4",
        "overview": "pelicula de ficcion 4",
        "year": "2021",
        "rating": 8.7
    },
    {
        "id": 5,
        "title": "shreck",
        "overview": "pelicula de ficcion 5",
        "year": "2003",
        "rating": 8.7
    },
    {
        "id": 6,
        "title": "shreck 2",
        "overview": "pelicula de ficcion 6",
        "year": "2004",
        "rating": 8.7
    },
    {
        "id": 7,
        "title": "shreck 3",
        "overview": "pelicula de ficcion 7",
        "year": "2005",
        "rating": 8.7
    },
    {
        "id": 8,
        "title": "shreck para siempre",
        "overview": "pelicula de ficcion 8",
        "year": "2006",
        "rating": 8.7
    },
    {
        "id": 9,
        "title": "castigador",
        "overview": "pelicula de ficcion 9",
        "year": "2007",
        "rating": 8.7
    },
    {
        "id": 10,
        "title": "castigador zona de guerra",
        "overview": "pelicula de ficcion 10",
        "year": "2008",
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

