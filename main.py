from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse

app = FastAPI()

# Allow your local frontend to talk to the backend without blocking
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Serves your HTML page when you visit http://127.0.0.1:8000
@app.get("/")
async def read_index():
    return FileResponse("index.html")

# Triggers when the HTML button sends a request
@app.post("/api/action")
async def trigger_button():
    print("Button was clicked! Executing Python logic in terminal...")
    return {"status": "success", "message": "Python operation completed successfully!"}