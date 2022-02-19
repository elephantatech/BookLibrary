import uvicorn
from config import get_settings

from fastapi import FastAPI, status
from fastapi.responses import JSONResponse

app = FastAPI()
app.settings = get_settings()


@app.get("/")
def home():
    return JSONResponse(
        content={"message": "This is the home page"}, status_code=status.HTTP_200_OK
    )


@app.get("/vars/")
def vars():
    variables = dict(app.settings)
    return JSONResponse(
        content={"variables": variables}, status_code=status.HTTP_200_OK
    )


def main():
    """Launch Uvicorn with poetry"""
    uvicorn.run(
        "fastapi-backend.main.app:app",
        host="0.0.0.0",
        port=8000,
        reload=True
        )
