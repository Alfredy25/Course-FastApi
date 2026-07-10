from fastapi import FastAPI

from course.alfredo.fastapi.webapi.routers import messages

app = FastAPI()

app.include_router(messages.router, prefix="/messages", tags=["messages"])

@app.get("/")
def read_data():
    return {"Message": "Hola Mundo! con FastApi mi primer endpoint!!!"}