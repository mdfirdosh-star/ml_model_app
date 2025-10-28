import json 
from fastapi import FastAPI
from fastapi.responses import JSONResponse
from schema.user_input import UserInput
from data.predict import predict_output,MODEL_VERSION,model
from schema.prediction_responce import predictionresponce




app=FastAPI()


# human readable         
@app.get("/")
def home():
    return {"message":"insurance premium prediction api"}

# machine readable
@app.get("/health")
def health_check():
    return {"status":"ok",
            "vesion":MODEL_VERSION,
            "model_load":model is not None}
@app.get("/predict",response_model=predictionresponce)
def predict_p(data:UserInput):
    user_input={
        'bmi': data.bmi,
        'age_group': data.age_group,
        'life_risk': data.life_risk,
        'city_tier': data.city_tier,
        'income_lpa': data.income_lpa,
        'occupation': data.occupation}
    try:
         prediction=predict_output(user_input)
         return JSONResponse(status_code=200,content={"Responce":prediction})
    except Exception as e:
        return JSONResponse(status_code=500,content=str(e))
@app.post("/predict",response_model=predictionresponce)
def predict_primium(data:UserInput):
    user_input={
        'bmi': data.bmi,
        'age_group': data.age_group,
        'life_risk': data.life_risk,
        'city_tier': data.city_tier,
        'income_lpa': data.income_lpa,
        'occupation': data.occupation}
    try:
         prediction=predict_output(user_input)
         return JSONResponse(status_code=200,content={"Responce":prediction})
    except Exception as e:
        return JSONResponse(status_code=500,content=str(e))
