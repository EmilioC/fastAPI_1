
#Python
from typing import Optional

#Pydantic
from pydantic import BaseModel

#FastAPI
from fastapi import FastAPI

app = FastAPI() 

# Models

class Person(BaseModel):
    first_name: str
    last_name: str
    age: int
    hair_color: Optional (str)
    is_married: Optional (bool)

""" En el home vamos a ejecutar la aplicación """
@app.get("/") 
def home():
    return{"Hell":"friend"}

#Request and Respond

@app.post("/person/new")
def create_person