from fastapi import FastAPI
from pydantic import BaseModel
import numpy as np
from joblib import load
import pathlib
from fastapi.middleware.cors import CORSMiddleware


origins = ["*"]


app = FastAPI(title = 'Machine failure Prediction')

app.add_middleware(
   CORSMiddleware,
   allow_origins=origins,
   allow_credentials=True,
   allow_methods=["*"],
   allow_headers=["*"]
)
model = load(pathlib.Path('model/machine-failure.csv-v1.joblib'))

class InputData(BaseModel):
    UDI:int=1
    Product:int=14860
    Type:int=0
    AirTeperature:float=298.1
    ProcessTeperature:float=308.6
    Rotationa1speed:int=1551
    Too1wear:int=0
    ac2inefai1ure:int=0
    TWF:int=0
    DF:int=0
    PWF:int=0
    OSF:int=0
    RNF:int=0

class OutputData(BaseModel):
    score:float=0.80318881046519

@app.post('/score', response_model = OutputData)
def score(data:InputData):
    model_input = np.array([v for k,v in data.dict().items()]).reshape(1,-1)
    result = model.predict(model_input)

    return {'score':result}
