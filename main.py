
#Python
from typing import Optional

#Pydantic
from pydantic import BaseModel

#FastAPI
from fastapi import FastAPI
from fastapi import Body, Query, Path

# Activar entorno virtual .\venv\Scripts\activate
# Lanzar aplicación: uvicorn main:app --reload

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
        name: Optional[str] = Query (
            None, 
            min_length=1, 
            max_length=50,
            title= "Person Name",
            description="This is the person name. It's between 1 and 50 characters"
            ),
        age: str = Query(
            ...,
            title="Person Age",
            description="This is the person age. It's required"
            ),
        
):
    return {name: age}

# Validaciones: Path Parameters

@app.get("/person/detail/{person_id}")
def show_person(
    person_id: int = Path(
        ...,
        gt=0,
        title="Person Id",
        description="This is the person id. It's required"
        )
):
    return {person_id: "It exists¡"}

# Validaciones: Request Body

@app.put("/person/{person_id}")
def update_person(
    person_id: int = Path (
        ..., 
        title="Person ID",
        description="This is the person ID",
        gt=0
    ),
        person: Person = Body (...)
):
    return person
