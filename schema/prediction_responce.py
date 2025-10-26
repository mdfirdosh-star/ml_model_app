from pydantic import BaseModel,Field
from typing import Dict,Annotated

class predictionresponce(BaseModel):
    predicted_category:Annotated[str,Field(...,description="predicted_category name",example="High")]
    confidience:float=Field(...,description="model prediction_categiry confidience range(0,1)",example=1)
    class_probablities:Dict[str,float]=Field(...,description="probablity disdributions score all possible classes ",example={"High": 0.41,
      "Low": 0.13,
      "Medium": 0.46})
