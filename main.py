
#Python
from typing import Optional

#Pydantic
from pydantic import BaseModel

#FastAPI
from fastapi import FastAPI
from fastapi import Body, Query, Path

app = FastAPI() 

# Models
class Person(BaseModel):
    first_name: str
    last_name: str
    age: int
    hair_color: Optional [str] = None
    is_married: Optional [bool] = None

""" En el home vamos a ejecutar la aplicación """
@app.get("/") 
def home():
    return{"Hell":"friend"}

#Request and Respond Body

@app.post("/person/new")
# ... indica que es obligatorio
def create_person( person: Person = Body(...)): 
    return person

# Validaciones: Query Parameters

@app.get("/person/detail")
def show_person( 
                #User no podrá enviar nunca menos de 1 y máximo 50 caracteres
        name: Optional[str] = Query (None, min_length=1, max_length=50),
        age: str = Query(...),
        
):
    return {name: age}

# Validaciones: Path Parameters

@app.get("/person/detail/{person_id}")
def show_person(
    person_id: int = Path(...,gt=0)
):
    return {person_id: "It exists¡"}
