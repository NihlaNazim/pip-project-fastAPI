from fastapi import fastapi

app = FastAPI()

@app.get("/hello")
def read_root():
    return {"message": "Hello, CI/CD World!"}
    