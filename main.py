import os
from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def root():
    return {"message": "SaaSIO MVP API Online"}

# Add this block
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=int(os.environ.get("PORT", 8000)))