from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError
from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel
from sklearn.linear_model import LinearRegression
import numpy as np

app = FastAPI()

# Model regresji
X = np.array([[1], [2], [3], [4], [5]])
y = np.array([2, 4, 6, 8, 10])  # y = 2 * x

model = LinearRegression()
model.fit(X, y)

class InputData(BaseModel):
    x: float

# Obsługa błędów wejściowych
@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    return JSONResponse(
        status_code=422,
        content={
            "error": "Nieprawidłowe dane wejściowe",
            "details": jsonable_encoder(exc.errors())
        },
    )

# Endpoint stratowy
@app.get("/")
def read_root():
    return JSONResponse(content={"message": "Siema bratku!"})

@app.post("/predict")
def predict(data: InputData):
    prediction = model.predict(np.array([[data.x]]))
    return JSONResponse(content={"prediction": prediction[0]})

@app.get("/health")
def health():
    return JSONResponse(content={"status": "ok"})

@app.get("/info")
def model_info():
    info = {
        "model_type": "LinearRegression",
        "n_features": int(model.coef_.shape[0]),
        "coefficients": model.coef_.tolist(),
        "intercept": model.intercept_.item()
    }
    return JSONResponse(content=info)