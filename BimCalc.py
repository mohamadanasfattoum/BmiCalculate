from fastapi import FastAPI

# create api app
app = FastAPI()

# تحديد المسار الرأيسي
# Definieren den Hauptpfad
@app.get("/calculate_bmi")

def calculate_bmi(weight: float, height:float):
    bmi = weight / (height ** 2)

    if bmi < 18.5:
        message = 'Sie sind untergewichtig, essen Sie mehr'
    elif 18.5 <= bmi < 25 :
        message = 'Sie haben ein normales Gewicht, behalten Sie es bei'
    elif 25 <= bmi <30:
        message = 'Sie sind übergewichtig, treiben Sie mehr Sport'
    else:
        message = 'Sie leiden an Fettleibigkeit, suchen Sie daher bitte einen Arzt auf'

    return {
        'bmi': bmi,
        'message': message
        }
# ohne docs#
# http://127.0.0.1:8000/calculate_bmi?weight=77&height=1.78
# outpot:
# {
#   "bmi": 24.3024870597147,
#   "message": "Sie haben ein normales Gewicht, behalten Sie es bei"
# }

# mit docs#
# http://127.0.0.1:8000/docs#/
