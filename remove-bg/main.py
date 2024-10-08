from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import logging
from dotenv import load_dotenv
from resources import download_resource, remove_bg_resource

load_dotenv()

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(threadName)s - %(levelname)s - %(message)s')

app = FastAPI(title="remove-bg-api", version="0.1.0")
origins = [
    "*",  # Allows requests from any origin (use with caution in production)
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
    expose_headers=['Content-Disposition']
)

# Register your routes
app.include_router(prefix="/api", router=remove_bg_resource.router)
app.include_router(prefix="/api", router=download_resource.router)
 



