# -------------Core packages------------------------------------
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# -------------Other packages------------------------------------
from json import loads

# -------------Own logics------------------------------------
from logic import FindRate

# -------------------------------------------------

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
    )

@app.get("/", tags=["Rate"])
def index():
    obj = FindRate()

    return {
        "gold": obj.gold(),
        "silver": obj.silver(),
        "platinum": obj.platinum()
        }


@app.get("/gold", tags=["Rate"])
def gold():
    obj = FindRate()
    return {"gold": obj.gold()}

@app.get("/silver", tags=["Rate"])
def silver():
    obj = FindRate()
    return {"silver": obj.silver()}

@app.get("/platinum", tags=["Rate"])
def platinum():
    obj = FindRate()
    return {"platinum": obj.platinum()}