
import pickle
import pandas as pd
#import ml model
with open("data/modelapi.pkl","rb") as f:
    model=pickle.load(f)

#mlflow find the version 
MODEL_VERSION="1.0.0"


class_labels=model.classes_.tolist()
def predict_output(user_input:dict):
    data=pd.DataFrame([user_input])
    predict_class=model.predict(data)[0]

    # probabilites for all categoryes 
    probabilities=model.predict_proba(data)[0]
    confidence=max(probabilities)

    #create mapping(class name :probabilites)
    class_probs=dict(zip(class_labels,map(lambda p:round(p,4),probabilities)))
    return {"predicted_category":predict_class,
            "confidience":round(confidence),
            "class_probablities":class_probs}