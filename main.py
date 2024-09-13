from fastapi import FastAPI, Body #importa la libreria
from fastapi.responses import HTMLResponse #importa la libreria
from movies_list import movies_list #importa la libreria

app = FastAPI() #crea una instancia de la clase FastAPI
app.title = 'Mi app con FastAPI - Movies' #asigna un valor a la variable title
app.version = "0.0.1" #asigna un valor a la variable version

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

@app.get ('/movies/', tags=["Movies"])
def get_movies_by_category (category: str, year: int): 
    return [item for item in movies_list if item["year"] == year]

@app.post ('/movies/', tags=["Movies"])
def create_movie (
    id: int = Body(), 
    title: str = Body(), 
    overview: str = Body(), 
    year: int = Body(), 
    rating: float = Body(), 
    category: str = Body()):
    movies_list.append ({
        "id": id, 
        "title": title, 
        "overview": overview, 
        "year": year, 
        "rating": rating, 
        "category": category
        })
    return movies_list

@app.put ('/movies/fid)', tags=['Movies'])
def update_movie (id: int, title: str = Body(), overview: str = Body(), year: int = Body(), rating: float = Body(), category: str = Body()):
    for item in movies_list:
        if item["id"] == id: 
            item['title'] = title,
            item['overview'] = overview,
            item['year'] = year,
            item['rating'] = rating,
            item[' category'] = category,
            return movies_list

@app.delete('/movies/(id)', tags=['Movies'])
def delete_movie(id: int):
    for item in movies_list:
        if item["id"] == id:
            movies_list.remove(item)
            return movies_list

