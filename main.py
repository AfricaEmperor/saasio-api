import os
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "SaaSIO MVP API Online"}

@app.get("/health")
async def health_check():
    return {"status": "ok"}

# For Railway deployment
if __name__ == "__main__":
    import uvicorn
    port = int(os.environ.get("PORT", 8000))
    uvicorn.run("main:app", host="0.0.0.0", port=port, reload=True)