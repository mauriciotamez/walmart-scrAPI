from fastapi import FastAPI
import get_departments

app = FastAPI()


@app.get("/departments")
async def root():
    return get_departments.departmentsArray
