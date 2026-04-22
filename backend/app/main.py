from fastapi import FastAPI

app = FastAPI(title="F1 Hub API")

@app.get("/health")
def health():
    return {"status": "ok"}