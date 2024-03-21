from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.get("/", response_class=HTMLResponse)
async def read_root():
    return """
    <html>
        <head>
            <title>FastAPI Application</title>
        </head>
        <body>
            <h1 style='color: red;'>Hello World V2</h1>
        </body>
    </html>
    """

if __name__ == "__main__":
    import uvicorn
    port = int(os.environ.get("PORT", 8080))  # Use PORT environment variable if it's there
    uvicorn.run(app, host="0.0.0.0", port=port)
