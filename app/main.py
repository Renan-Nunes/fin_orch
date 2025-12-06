from fastapi import FastAPI
from app.routes import init_routes
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
app.include_router()
init_routes(app)


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def root():
    return {"message": "Hello World"}
