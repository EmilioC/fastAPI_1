from fastapi import FastAPI

app = FastAPI() 

""" En el home vamos a ejecutar la aplicación """
@app.get("/") 
def home():
    return{"Hello friend"}