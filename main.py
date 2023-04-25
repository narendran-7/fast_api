from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# -------------------------------------------------
from logic import FindRate


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
    )

@app.get("/")
def index():
    obj = FindRate()

    return {
        "gold": obj.gold(),
        "silver": obj.silver(),
        "platinum": obj.platinum()
        }


@app.get("/gold")
def gold():
    obj = FindRate()
    return {"gold": obj.gold()}

@app.get("/silver")
def silver():
    obj = FindRate()
    return {"silver": obj.silver()}

@app.get("/platinum")
def platinum():
    obj = FindRate()
    return {"platinum": obj.platinum()}