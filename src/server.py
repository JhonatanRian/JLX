from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from src.routers import products as products_router,users as users_router, requests as requests_router  

### API
app = FastAPI()

### CORS
origins = ["http://localhost:8000", "https://localhost:8000"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

### Routers Products
app.include_router(products_router.router)

### Routers_Users
app.include_router(users_router.router)

### Routers Requests
app.include_router(requests_router.router)