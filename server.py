from fastapi import FastAPI
import uvicorn

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "FastAPI on Vercel!"}

if _name_ == "_main_":
    uvicorn.run(app, host="0.0.0.0", port=8000)