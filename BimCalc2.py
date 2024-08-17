# uvicorn BimCalc2:app --reload 
# Verbessern Sie den Code, Code Optimization

from fastapi import FastAPI, Query
# pydantic # Bibliothek zur Eingabevalidierung # مكتبة للتحقق من المدخلات
from pydantic import BaseModel

# CORSMiddleware: Erlauben Sie die Kommunikation mit dem Browser und Anfragen vom Browser zulassen 
# السماح بطلبات من المتصفح, السماح بالتواصل مع المتصفح
from fastapi.middleware.cors import CORSMiddleware


# create api app
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# تحديد المسار الرأيسي
# Definieren den Hauptpfad

class BMIOutput(BaseModel):
    bmi: float
    message: str

@app.get("/calculate_bmi")

def calculate_bmi(
    weight: float= Query(... , gt=20, lt=200, description='Gewicht in Kg:'),
    height:float= Query(... , gt=1, lt=3, description='Länge in m:')
    ):

    bmi = weight / (height ** 2)

    if bmi < 18.5:
        message = 'Sie sind untergewichtig, essen Sie mehr'
    elif 18.5 <= bmi < 25 :
        message = 'Sie haben ein normales Gewicht, behalten Sie es bei'
    elif 25 <= bmi <30:
        message = 'Sie sind übergewichtig, treiben Sie mehr Sport'
    else:
        message = 'Sie leiden an Fettleibigkeit, suchen Sie daher bitte einen Arzt auf'

    return BMIOutput(bmi=bmi, message=message)
