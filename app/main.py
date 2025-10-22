from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.get("/", response_class=HTMLResponse)
def read_root():
    return """
    <html>
        <head>
            <title>Deployment Successful 🚀</title>
            <style>
                body {
                    font-family: Arial, sans-serif;
                    background: #0d1117;
                    color: #e6edf3;
                    display: flex;
                    flex-direction: column;
                    align-items: center;
                    justify-content: center;
                    height: 100vh;
                }
                h1 {
                    color: #3fb950;
                }
                p {
                    margin-top: 10px;
                    color: #8b949e;
                }
            </style>
        </head>
        <body>
            <h1>✅ Deployment Successful!</h1>
            <p>Your FastAPI app is running via Docker & Nginx.</p>
        </body>
    </html>
    """
