# test code
from fastapi import FastAPI

# create api app
app = FastAPI()

# تحديد المسار الرأيسي
# Definieren den Hauptpfad
@app.get("/")

# Definieren die Funktion für den Pfad

def Hi():
    return {"message":"Marhaba"}

# uvicorn Hello:app --reload 
# Hello name von code
# app name von app
# reload, damit die Anwendung weiterhin funktioniert