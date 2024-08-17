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

# -----------------

# تحديد المسار الرأيسي
# Definieren den Hauptpfad
@app.get("/calculate_bmi")

def calculate_bmi(weight: float, height:float):
    bmi = weight / (height ** 2)

    return {'Your bmi': bmi}

# http://127.0.0.1:8000/calculate_bmi?weight=80&height=1.7
# weight=in kg &height= in m
# outpot: {"Your bmi":27.68166089965398}