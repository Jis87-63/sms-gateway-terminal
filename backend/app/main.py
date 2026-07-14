from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes import auth, gateways, messages, queue, campaigns, logs, stats

app = FastAPI(title="SMS Gateway Platform API", version="1.0.0")
app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_credentials=True, allow_methods=["*"], allow_headers=["*"])
app.include_router(auth.router)
app.include_router(gateways.router)
app.include_router(messages.router)
app.include_router(queue.router)
app.include_router(campaigns.router)
app.include_router(logs.router)
app.include_router(stats.router)

@app.get("/health")
def health():
    return {"status": "ok", "service": "sms-gateway-platform"}
