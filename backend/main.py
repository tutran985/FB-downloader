from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
import httpx

app = FastAPI(docs_url=None, redoc_url=None)
PORT = 8001

# Production CORS settings
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Replace with your domain
    allow_methods=["POST"],
    allow_headers=["*"],
)

@app.post("/fetch")
async def fetch_video(data: dict):
    url = data.get("url")
    headers = {
        "accept": "*/*",
        "content-type": "application/x-www-form-urlencoded; charset=UTF-8",
        "origin": "https://getsave.net",
        "referer": "https://getsave.net/en",
        "user-agent": "Mozilla/5.0 (X11; Linux x86_64)",
        "x-requested-with": "XMLHttpRequest"
    }
    payload = f"url={url}"
    async with httpx.AsyncClient() as client:
        response = await client.post(
            "https://getsave.net/proxy.php",
            data=payload,
            headers=headers
        )
    return response.json()
