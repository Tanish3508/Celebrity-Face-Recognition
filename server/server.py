from fastapi import FastAPI, Form
from pydantic import BaseModel
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
import util

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], 
    allow_credentials=True,
    allow_methods=["*"], 
    allow_headers=["*"],
)
class ImageData(BaseModel):
    image_data: str

@app.post("/classify_image")
async def classify_image(image_data: str = Form(...)):
    result = util.classify_image(image_data)
    return JSONResponse(content=result)

if __name__ == "__main__":
    print("Starting Python FastAPI Server For Sports Celebrity Image Classification")
    util.load_saved_artifacts()
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=5000)