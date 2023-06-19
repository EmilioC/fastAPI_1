
#Python
from typing import Optional

#Pydantic
from pydantic import BaseModel

#FastAPI
from fastapi import FastAPI
from fastapi import Body

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